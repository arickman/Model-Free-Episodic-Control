import numpy as np
import csv
import matplotlib.pyplot as plt 
f_d = open('agents/Qbert-v0_1558722343/results.csv')
f_a = open('agents_avg/Qbert-v0_1558722364/results.csv')
f_w = open('agents_wavg/Qbert-v0_1558722383/results.csv')
csv_dict = {}
csv_dict['d'] = csv.reader(f_d)
csv_dict['a'] = csv.reader(f_a)
csv_dict['w'] = csv.reader(f_w)

plt.figure(figsize=(20, 5))
for keynum, key in enumerate(csv_dict):
	epochs = []
	reward_sum = []
	reward_avg = []
	reward_max = []
	csv_f = csv_dict[key]
	for counter,row in enumerate(csv_f):
		if counter == 0: continue
		epochs.append(int(row[0]))
		reward_sum.append(int(row[3]))
		reward_avg.append(int(row[4]))
		reward_max.append(int(row[5]))
	plt.subplot(1, 3, keynum + 1)
	plt.plot(epochs, np.array(reward_sum)/10)
	plt.plot(epochs, reward_avg)
	plt.plot(epochs, reward_max)
	plt.xlabel('Epochs')
	plt.ylabel('Reward Value')
	plt.ylim(0, 14000)
	plt.legend(['Summed Reward/10', 'Average Reward', 'Maximum Reward'], loc='upper left')
	if key == 'd' : plt.title('Default Update Rule')
	elif  key == 'a' : plt.title('Average Update Rule')
	elif key == 'w' : plt.title('Weighted Average Update Rule')

# fig, ax = plt.subplots()
# ax.plot(epochs, reward_max)
# ax.set_xlabel("Epoch")
# ax.set_ylabel("Max Reward")
# ax.set_title("Weighted Average Update Rule")
# fig.savefig("plots/wavg_11epochs_reward_max.pdf")

#plt.show()
plt.savefig('plots/plot_11epochs_w5.png')

