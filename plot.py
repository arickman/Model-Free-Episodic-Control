import numpy as np
import csv
import matplotlib.pyplot as plt 
#f = open('agents/Qbert-v0_1558722343/results.csv')
#f = open('agents_avg/Qbert-v0_1558722364/results.csv')
f = open('agents_wavg/Qbert-v0_1558722383/results.csv')
csv_f = csv.reader(f)

epochs = []
episodes = []
frames = []
reward_sum = []
reward_avg = []
reward_max = []
for counter,row in enumerate(csv_f):
	if counter == 0: continue
	epochs.append(int(row[0]))
	episodes.append(int(row[1]))
	frames.append(int(row[2]))
	reward_sum.append(int(row[3]))
	reward_avg.append(int(row[4]))
	reward_max.append(int(row[5]))

fig, ax = plt.subplots()
ax.plot(epochs, reward_avg, scaley=False)
ax.set_xlabel("Epoch")
ax.set_ylabel("Average Reward")
ax.set_title("Weighted Average Update Rule")
ax.set_xlim(0,12)
ax.set_ylim(500,8500)
fig.savefig("plots/waverage.pdf")


