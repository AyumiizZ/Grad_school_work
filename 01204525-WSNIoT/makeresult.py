import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("results.csv")
success = data.groupby("prob").success.mean()
 
success.plot(style="b--")
success.plot(style="go")
plt.grid(True)
plt.xlabel("Gossip Probability")
plt.ylabel("Success Rate (%)")
plt.show()
