import math
import random
import matplotlib.pyplot as plt
import numpy as np

def next_element(x):
	i, d = divmod(x, 1)
	next_x = i*d+1
	return next_x

# print(next_element(2.5))

def a_Sequence(x):
	prev_term = 0
	cur_term = x
	sequence = [x]
	while prev_term != cur_term:
		prev_term =  cur_term
		cur_term = next_element(cur_term)
		sequence.append(cur_term)
	return sequence

print(a_Sequence(3.14))

def stablization_time(x):
	sequence = a_Sequence(x)
	return len(sequence)-1

print(stablization_time(3.14))

def stablization_time_test(n,lower_lim,upper_lim):
	i = 0
	xData = []
	yData = []
	while i < n:
		x = random.uniform(lower_lim, upper_lim)
		xData.append(x)
		yData.append(stablization_time(x))
		i += 1
	return [xData,yData]

# print(stablization_time_test(10,1,10))

# n = 10000 
# lower_lim = 1
# upper_lim = 10000
# data = stablization_time_test(n,lower_lim,upper_lim)
# xData = data[0]
# yData = data[1]
# plt.plot(xData, yData,'o')
# plt.show()

def stabalization_value(x):
	sequence = a_Sequence(x)
	return sequence[-1]

def stablization_value_test(n,lower_lim,upper_lim):
	i = 0
	data = []
	while i < n:
		x = random.uniform(lower_lim, upper_lim)
		data.append(stabalization_value(x))
		i += 1
	return data

# print(stablization_value_test(10,1,10))

# n = 1000000 
# lower_lim = .1
# upper_lim = 10000
# data = stablization_value_test(n,lower_lim,upper_lim)
# plt.hist(data,bins=50)
# plt.show() 

def sequence_tests(n,lower_lim,upper_lim):
	i = 0
	data = []
	while i < n:
		x = random.uniform(lower_lim, upper_lim)
		data.append(a_Sequence(x))
		i += 1
	max_length = max([len(seq) for seq in data])
	padded_data = []
	for seq in data:
		padding = max_length - len(seq)
		last_elm = seq[-1]
		seq.extend([last_elm]*padding)
		padded_data.append(seq)
	return padded_data

# print(sequence_tests(10,1,10))

n = 10
lower_lim = 40
upper_lim = 50
sample_list = sequence_tests(n,lower_lim,upper_lim)
print(sample_list)
sample_list = np.array(sample_list)
print(np.shape(sample_list))
print(sample_list)
sample_list = np.transpose(sample_list)
print(np.shape(sample_list))
print(sample_list)
plt.plot(sample_list)
plt.show()