import random
import wsnsimpy.wsnsimpy_tk as wsp
import numpy as np
 
def runsim(seed,prob,source, logging = True):
    
    random.seed(seed)
    sim = wsp.Simulator(
        until=50,
        visual=True,
        terrain_size=(600,600),
        timescale=1)
 
    # place nodes in 100x100 grids 
    for x in range(10):
        for y in range(10):
            px = 50 + x*60 + random.uniform(-20,20)
            py = 50 + y*60 + random.uniform(-20,20)
            node = sim.add_node(GossipNode, (px,py))
 
    # save simulation-wide variables in the 'sim' object
    sim.gossip_prob = prob
    sim.source = source
	
    # start simulation
    sim.run(logging=logging)
    
    num_success = sum(n.success for n in sim.nodes)
    num_tx = sum(n.tx for n in sim.nodes)
    num_rx = sum(n.rx for n in sim.nodes)
    for n in sim.nodes:
        n.print_route_table()
    return num_success, num_tx, num_rx
 
class GossipNode(wsp.Node):
 
    tx_range = 70
 
    def run(self, logging):
        self.hop = 0
        self.count = 0
        self.rx = 0
        self.tx = 0
        self.logging = logging
        self.route_table = {}
        self.style = wsp.LineStyle(color=(0,0.5,0), dash=(), width=3, arrow="head")
        self.links = []
        self.path = []
        if self.id == self.sim.source:
            self.success = True
            yield self.timeout(2)
            self.route_request()
        else:
            self.success = False

    def update_route_table(self, route):
        for i in range(self.hop)
            dest = route[i]
            via = route[self.hop-1]
            if dest not in self.route_table:
                self.route_table.[dest] = via

    def print_route_table(self, route):
        self.log(f"Route table of {self.id} is {self.route_table}")

    def unicast(self, dest):
        self.log(f"Unicast to {dest}")
        self.send(dest)
        self.tx += 1

    def route_reply(self, dest):
        srcPos = self.sim.nodes[self.id].pos
        destPos = self.sim.nodes[dest].pos
        self.scene.nodecolor(self.id, 0,0.5,0)
        link_obj = self.scene.line(srcPos[0], srcPos[1], destPos[0], destPos[1], line=self.style)
        self.links.append(link_obj)
        self.unicast(dest)

    def route_request(self):
        if self.id == self.sim.source or random.random() <= self.sim.gossip_prob:
            self.log(f"Finding route")
            self.path.append(self.id)
            self.send(wsp.BROADCAST_ADDR, flag='RRQ', hop=self.hop, path=self.path)
            self.scene.nodewidth(self.id, 3)
            # self.sim.env.process(self.booth("Booth 1",self.sim.env))
            self.tx += 1
    
    def route_process(self, sender, **kwargs):
        max_hop = kwargs['max_hop']
        self.hop = kwargs['hop']+1
        if self.hop <= max_hop:
            print(self.hop)
            self.rx += 1
            self.scene.nodecolor(self.id, 1,0,0)
            self.log(f"Receive message from {sender}")
            if self.success:
                self.log(f"Message seen; reject")
                return
            self.log(f"New message; prepare to rebroadcast")
            self.success = True
            yield self.timeout(random.uniform(0.5,1.0))
            self.route_reply(sender)
            self.route_request()

    def process_data(self, data):
        print(data)
        pass

    def pass_data(self):
        pass

    def reply_data(self):
        pass
 
    def on_receive(self, sender, **kwargs):
        # RRQ = Route ReQuest
        # RRP = Route RePly
        # PDT = Passing DaTa
        # RDT = Reply DaTa
        flag = kwargs['flag'] if kwargs else ''
        if flag == 'RRQ':
            self.route_process(sender, **kwargs)
        elif flag == 'RRP':
            self.log(f"Receive route from {sender}")
        elif flag == 'PDT':
            self.log(f"Passing Data to {sender}")
            self.pass_data()
    
    def clearlinks(self):
        for _id in self.links:
            self.scene.delshape(_id)

    def booth(self, name,env):
        
        while True:
            yield env.timeout(2)
            self.count += 1
            # print(f"At {env.now:3.0f} seconds, car #{self.count} arrives at {self.id}")



import sys
runsim(1, float(sys.argv[1]), 60)