"""
Austin Peng
CSC 241
Assignment 1

Simulate a leaky integrate-and-fire model neuron with a resting potential of Vrest = -65mV and a spiking threshold
of -50mV. The input current is Iptq. The membrane has a decay constant of tau = 20ms:


dV(t) / t = -(1/tau) * [V(t) - V(rest)] + I(t) 

Add the assumption that the membrane potential cannot decrease below the reset potential, i.e. whenever an
input pushes V to below the reset potential, reset it to -70mV.

Simulate your model neuron with excitatory and inhibitory inputs of varying magnitude and variance. Plot
the interspike interval (ISI) distribution and compute the mean spike rate. Plot the coecient of variation (CV)
of the ISI distribution as a function of the standard deviation of the input current. What do you find and why?

At each step, summarize your observations in a couple of sentences, and include your predictions for each
before you ran the simulations.
"""
import numpy as np
import math, sys
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def test():
	a=1
	b=True
	return a, b

#FORMULA
#t1 and t2 markov chain
def problem1(vt1, t1, t2, I):
	#I = float(np.random.normal(mu, sigma, size))
	vrest = -65
	spike_threshold = -50
	reset_potential = 30
	tau = 20

	mu, sigma, size = 0, 1, 1
	spike = False

	if (vt1 >= reset_potential):
		vt2 = vrest
		spike = True

	else:
		vt2 = vrest + I + (vt1 - vrest - I) * math.exp((-t2 -t1)/tau)
	
	return vt2, spike

#PLOTS V(t) OVER TIME
def problem2(I):
	#create bins of 0.1ms
	bins = []
	time_length = 2
	for i in range(0, time_length*1000):
		bins.append(i/1000)

	#find V
	voltages = []
	spike_counter = 0
	
	for i in bins:
		#base case
		if(i == 0):
			result, spike = problem1(-65, i, i, I)
			voltages.append(result)
		else:
			#runs problem1 w/ previous voltage, t1 and t2
			vt1 = float(voltages[ int(i*1000-1) ])
			result, spike = problem1( vt1 , i-1/1000, i, I)
			voltages.append(result) 
			if(spike == True):
				spike_counter += 1
	
	spikerate = spike_counter/time_length
	print("spikerate:" , spikerate)
	
	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	ax = plt.axes()
	ax.plot(bins, voltages)
	title = "Membrane Potentials for I = "+str(I) +"mV"
	plt.title(title)
	plt.xlabel("Time (t)")
	plt.ylabel("Output (V)")
	plt.show()
	return spikerate

#PLOTS SPIKERATE OVER INPUT V
def problem3():
	input_range = []
	for i in range(960, 1150):
		input_range.append(i/10)

	spikerate_list = []

	for I in input_range:
		spikerate_list.append(problem2(I))
	
	print(spikerate_list)

	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	ax = plt.axes()
	ax.plot(input_range, spikerate_list)
	plt.title("Function of Spike Rate with respect to I")
	plt.xlabel("Input I (V)")
	plt.ylabel("Spike Rate")
	plt.show()



if __name__ == "__main__":
	#test()
	problem2(114)
