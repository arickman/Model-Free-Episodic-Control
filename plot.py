import numpy as np
import csv
import matplotlib.pyplot as plt 
f_d_Q = open('agents/Qbert-v0_1559088024/results.csv')
f_a_Q = open('agents_avg/Qbert-v0_1559081161/results.csv')
f_w_Q = open('agents_wavg/Qbert-v0_1559258801/results.csv')

f_d_S = open('agents/SpaceInvaders-v0_1559335998/results.csv')
f_a_S = open('agents_avg/SpaceInvaders-v0_1559338005/results.csv')
f_w_S = open('agents_wavg/SpaceInvaders-v0_1559338074/results.csv')

f_d_P = open('agents/MsPacman-v0_1559416007/results.csv')
f_a_P = open('agents_avg/MsPacman-v0_1559416052/results.csv')
f_w_P = open('agents_wavg/MsPacman-v0_1559507275/results.csv')

csv_dict = {}
csv_dict['d_Q'] = csv.reader(f_d_Q)
csv_dict['a_Q'] = csv.reader(f_a_Q)
csv_dict['w_Q'] = csv.reader(f_w_Q)
csv_dict['d_S'] = csv.reader(f_d_S)
csv_dict['a_S'] = csv.reader(f_a_S)
csv_dict['w_S'] = csv.reader(f_w_S)
csv_dict['d_P'] = csv.reader(f_d_P)
csv_dict['a_P'] = csv.reader(f_a_P)
csv_dict['w_P'] = csv.reader(f_w_P)

#Load a dictionary with appropriate lists of rewards
plot_dict = {}
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
	plot_dict[key] = (epochs, reward_sum, reward_avg, reward_max)

#Generate plot
plt.figure(figsize = (40, 50))
plt.tight_layout()

plt.subplot(3,3,1)
plt.plot(plot_dict['d_Q'][0], plot_dict['d_Q'][1])
plt.plot(plot_dict['a_Q'][0], plot_dict['a_Q'][1])
plt.plot(plot_dict['w_Q'][0], plot_dict['w_Q'][1])
plt.xlabel('Epochs')
plt.ylabel('Summed Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Summed Reward for various Update Rules on Qbert')

plt.subplot(3,3,2)
plt.plot(plot_dict['d_Q'][0], plot_dict['d_Q'][2])
plt.plot(plot_dict['a_Q'][0], plot_dict['a_Q'][2])
plt.plot(plot_dict['w_Q'][0], plot_dict['w_Q'][2])
plt.xlabel('Epochs')
plt.ylabel('Average Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Average Reward for various Update Rules on Qbert')

plt.subplot(3,3,3)
plt.plot(plot_dict['d_Q'][0], plot_dict['d_Q'][3])
plt.plot(plot_dict['a_Q'][0], plot_dict['a_Q'][3])
plt.plot(plot_dict['w_Q'][0], plot_dict['w_Q'][3])
plt.xlabel('Epochs')
plt.ylabel('Maximum Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Maximum Reward for various Update Rules on Qbert')

plt.subplot(3,3,4)
plt.plot(plot_dict['d_S'][0], plot_dict['d_S'][1])
plt.plot(plot_dict['a_S'][0], plot_dict['a_S'][1])
plt.plot(plot_dict['w_S'][0], plot_dict['w_S'][1])
plt.xlabel('Epochs')
plt.ylabel('Summed Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Summed Reward for various Update Rules on Space-invaders')

plt.subplot(3,3,5)
plt.plot(plot_dict['d_S'][0], plot_dict['d_S'][2])
plt.plot(plot_dict['a_S'][0], plot_dict['a_S'][2])
plt.plot(plot_dict['w_S'][0], plot_dict['w_S'][2])
plt.xlabel('Epochs')
plt.ylabel('Average Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Average Reward for various Update Rules on Space-invaders')

plt.subplot(3,3,6)
plt.plot(plot_dict['d_S'][0], plot_dict['d_S'][3])
plt.plot(plot_dict['a_S'][0], plot_dict['a_S'][3])
plt.plot(plot_dict['w_S'][0], plot_dict['w_S'][3])
plt.xlabel('Epochs')
plt.ylabel('Maximum Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Maximum Reward for various Update Rules on Space-invaders')

plt.subplot(3,3,7)
plt.plot(plot_dict['d_P'][0], plot_dict['d_P'][1])
plt.plot(plot_dict['a_P'][0], plot_dict['a_P'][1])
plt.plot(plot_dict['w_P'][0], plot_dict['w_P'][1])
plt.xlabel('Epochs')
plt.ylabel('Summed Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Summed Reward for various Update Rules on Ms Pacman')

plt.subplot(3,3,8)
plt.plot(plot_dict['d_P'][0], plot_dict['d_P'][2])
plt.plot(plot_dict['a_P'][0], plot_dict['a_P'][2])
plt.plot(plot_dict['w_P'][0], plot_dict['w_P'][2])
plt.xlabel('Epochs')
plt.ylabel('Average Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Average Reward for various Update Rules on Ms Pacman')

plt.subplot(3,3,9)
plt.plot(plot_dict['d_P'][0], plot_dict['d_P'][3])
plt.plot(plot_dict['a_P'][0], plot_dict['a_P'][3])
plt.plot(plot_dict['w_P'][0], plot_dict['w_P'][3])
plt.xlabel('Epochs')
plt.ylabel('Maximum Reward')
plt.legend(['Default', 'Average', 'Weighted Average'], loc='best')
plt.title('Maximum Reward for various Update Rules on Ms Pacman')

#plt.show()
plt.savefig('plots/plot_20epochs_w5_QSP.png')
