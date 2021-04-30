import numpy as np
import simpy
 
def booth(name,env):
    count = 0
    while True:
        r = np.random.exponential(30)
        yield env.timeout(r)
        count += 1
        print(f"At {env.now:3.0f} seconds, car #{count} arrives at {name}: {r}")
 
env = simpy.Environment()
env.process(booth("Booth 1",env))
env.process(booth("Booth 2",env))
env.process(booth("Booth 3",env))
env.run(until=300)
