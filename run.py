import csv
import numpy as np
import gossip
 
SEED = range(5)
PROB = np.arange(0.1,1.1,.2)
 
with open("results.csv","w") as out:
    writer = csv.writer(out)
    writer.writerow(['seed','prob','success','tx','rx'])
    for seed in SEED:
        print(f"Running seed: {seed}")
        for prob in PROB:
            success,tx,rx = gossip.runsim(seed,prob,50)
            writer.writerow([seed,prob,success,tx,rx])
