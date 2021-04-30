import random
import wsnsimpy.wsnsimpy_tk as wsp
 
def runsim(seed,prob,source):
    random.seed(seed)
    sim = wsp.Simulator(
        until=50,
        visual=True,
        terrain_size=(600,600),
        timescale=5)
 
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
    sim.run()
    
    num_success = sum(n.success for n in sim.nodes)
    num_tx = sum(n.tx for n in sim.nodes)
    num_rx = sum(n.rx for n in sim.nodes)
 
    return num_success, num_tx, num_rx
 
class GossipNode(wsp.Node):
 
    tx_range = 100
 
    def run(self):
        self.rx = 0
        self.tx = 0
        self.logging = False
        if self.id == self.sim.source:
            self.success = True
            yield self.timeout(2)
            self.broadcast()
        else:
            self.success = False
 
 

    def broadcast(self):
        if self.id == self.sim.source or random.random() <= self.sim.gossip_prob:
            self.log(f"Broadcast message")
            self.send(wsp.BROADCAST_ADDR)
            self.scene.nodewidth(self.id, 3)
            self.tx += 1
 
    def on_receive(self, sender, **kwargs):
        self.rx += 1
        self.scene.nodecolor(self.id, 1,0,0)
        self.log(f"Receive message from {sender}")
        if self.success:
            self.log(f"Message seen; reject")
            return
        self.log(f"New message; prepare to rebroadcast")
        self.success = True
        yield self.timeout(random.uniform(0.5,1.0))
        self.broadcast()

import sys
runsim(1, float(sys.argv[1]), 60)