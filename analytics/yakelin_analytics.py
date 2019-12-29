import pandas as pd
import matplotlib.pyplot as plt

random=pd.read_csv("../data/results_random.csv")
suits=pd.read_csv("../data/results_suits_strat.csv")
vals=pd.read_csv("../data/results_val_strat.csv")

suits.columns = ["Cards_on_table","Number_of_wins_suits","Success_rate_suits"]
vals.columns = ["Cards_on_table","Number_of_wins_vals","Success_rate_vals"]

joined = random.merge(suits,on="Cards_on_table").merge(vals,on="Cards_on_table")

plt.plot('Cards_on_table','Success_rate',data=joined, color = 'red', label = "Choose random card")
plt.plot('Cards_on_table','Success_rate_suits',data=joined, color = 'blue', label = "Choose least seen suit")
plt.plot('Cards_on_table','Success_rate_vals',data=joined, color = 'green', label = "Choose least seen value")

plt.title("Probabilities of winning Yakelin for three different strategies")
plt.xlabel("Number of cards on the table")
plt.ylabel("Win probability")
plt.legend()

plt.savefig("../data/win_probabilities.png")