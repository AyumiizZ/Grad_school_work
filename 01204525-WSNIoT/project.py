import random
import wsnsimpy.wsnsimpy_tk as wsp


def finish(nodes):
    for node in nodes:
        node.print_table()


def runsim(source, probability=1, seed=2021, logging=True, n_processor=-1, max_hop=30):
    random.seed(seed)
    MAX_PROCESSOR = 99
    if n_processor == -1 or n_processor == MAX_PROCESSOR:
        processors = [i for i in range(MAX_PROCESSOR+1) if i != source]
    elif n_processor < MAX_PROCESSOR:
        processors = random.sample(range(MAX_PROCESSOR+1), n_processor + 1)
        if source in processors:
            processors = sorted([i for i in processors if i != source])
        else:
            processors = sorted(processors[:-1])
    else:
        raise 'n_processor is more than MAX_PROCESSOR'
    sim = wsp.Simulator(
        until=100,
        timescale=1,
        visual=True,
        terrain_size=(625, 625),
        title="Distribute Processor")

    # define a line style for parent links
    sim.scene.linestyle("parent", color=(.8, .8, .8), arrow="head", width=2)

    # place nodes over 100x100 grids
    for x in range(10):
        for y in range(10):
            px = 50 + x*60 + random.uniform(-20, 20)
            py = 50 + y*60 + random.uniform(-20, 20)
            node = sim.add_node(ProcessorNode, (px, py))
            node.tx_range = 75
            node.logging = logging

    # save simulation-wide variables in the 'sim' object
    sim.probability = probability
    sim.source = source
    sim.processors = processors
    sim.max_hop = max_hop

    # start the simulation
    sim.run()

    sim.finish = finish
    sim.finish(sim.nodes)


def delay():
    return random.uniform(.2, .5)


class ProcessorNode(wsp.Node):
    tx_range = 100

    def init(self):
        super().init()
        self.prev_hop = None
        self.hop = 0
        self.route_table = {}
        self.busy = False

    def run(self):
        if self.id is self.sim.source:
            self.prev_hop = self.sim.source
            self.scene.nodecolor(self.id, 0, 0, 1)
            self.scene.nodewidth(self.id, 2)
            yield self.timeout(5)
            self.send_rreq(self.id, route=[])
            yield self.timeout(self.hop_delay()*1.05)
            self.start_process(self.start_send_data())
        if self.id in self.sim.processors:
            self.scene.nodecolor(self.id, 0, 0.7, 0)
            self.scene.nodewidth(self.id, 2)

    def update_route_table(self, route):
        via = route[-1]
        if via not in self.route_table:
            self.route_table[via] = []
        for dest in route:
            if ((dest in self.sim.processors or dest is self.sim.source)
                 and (dest not in self.route_table[via])):
                self.route_table[via].append(dest)

    def print_table(self):
        if self.route_table != {} and self.id in self.sim.processors or self.id == self.sim.source:
            print(f"Node: {self.id} - {self.route_table}")

    def send_rreq(self, src, route):
        self.send(wsp.BROADCAST_ADDR, flag='rreq',
                  src=src, route=route + [self.id])

    def send_rreply(self, src, route):
        self.send(self.prev_hop, flag='rreply',
                  src=src, route=route + [self.id])

    def start_send_data(self):
        self.scene.clearlinks()
        seq = 0
        while True:
            yield self.timeout(1)
            for via in self.route_table:
                self.send_data(self.id, via, seq)
        seq += 1

    def send_data(self, src, via, seq):
        # self.log(f"Forward data with seq {seq} via {self.next}")
        # print((via, dest))
        dest_list = self.route_table[via]
        self.log(f"Send data to {dest_list} via {via} with seq {seq}")
        # self.log(f'Send data via {via}: dest = {dest_list}')
        self.send(via , flag='data', src=src, dest_list=dest_list, seq=seq)

    def send_result(self, src, res):

        self.send(self.prev_hop, flag='res', res=1)

    def hop_delay(self):
        return (self.sim.max_hop - self.hop) * 0.71

    # def find_via(self, dest):
    #     for via in self.route_table:
    #         # print(f'f:{self.route_table[via]}-{via}-{self.route_table}-{self.id}')
    #         if dest in self.route_table[via]:
    #             return via

    def on_receive(self, sender, flag, src, **kwargs):
        if flag == 'rreq':
            if self.prev_hop is not None:
                return
            route = kwargs['route']
            self.hop = len(route)
            if self.hop > self.sim.max_hop:
                return
            self.prev_hop = sender
            self.scene.addlink(sender, self.id, "parent")
            self.update_route_table(route)
            yield self.timeout(delay())
            self.send_rreq(src, route)
            if self.id in self.sim.processors:
                self.log(f"Receive RREQ from {src} via {sender}")
                yield self.timeout(self.hop_delay())
                self.log(f"Send RREP to {src} via {sender}")
                self.send_rreply(self.id, [])

        elif flag == 'rreply':
            self.next = sender
            route = kwargs['route']
            self.update_route_table(route)
            if self.id != self.sim.source:
                yield self.timeout(.2)
                self.send_rreply(src, route)

        elif flag == 'data':
            dest_list = kwargs['dest_list']
            seq = kwargs['seq']
            yield self.timeout(.2)
            self.scene.addlink(sender, self.id, "parent")
            # self.log(f'1-{self.route_table}')
            for via in self.route_table:
                # self.log(f'2-{via}-{self.route_table[via]}')
                if via != sender:
                    # self.log(f'3-{via}-{self.route_table[via]}')
                    # self.log(f'found via {via}: dest = {dest_list}')
                    self.send_data(self.id, via, seq)
            
            if self.id in dest_list:
                pass
                # self.log(f'Get data')
                # yield self.timeout(1)
                # self.log(f'finish process')
            #     yield self.timeout(.2)
            #     seq = kwargs['seq']
            #     via = self.find_via(dest)
            #     self.send_data(self.id, dest, via, seq)
            # else:
            #     seq = kwargs['seq']
            #     self.busy = True
            #     self.scene.nodecolor(self.id, 1, 0, 0)
            #     self.scene.nodewidth(self.id, 2)
            #     self.log(f"Got data from {src} with seq {seq}")


if __name__ == "__main__":
    runsim(90, seed=1, n_processor=40, max_hop=20)
