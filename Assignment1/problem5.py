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
from cv import coefficientOfVariation


def runtime():
	#create bins of 0.1ms
	bins, time_length = [], 5
	for i in range(0, int(time_length*1000)):
		bins.append(i/1000)
	return bins


def plotV(values, xaxis):
	plt.plot(xaxis, values)
	title = "CV with varying sigmas"
	plt.title(title)
	plt.xlabel("Sigma")
	plt.ylabel("CV")
	plt.style.use('seaborn-whitegrid')
	plt.show()

#FORMULA
#t1 and t2 markov chain
def problem1(vt1, t1, t2, I):
	vrest = -65
	spike_threshold = -50
	reset_potential = 30
	tau = 20

	#I = float(np.random.normal(mu, sigma, size))
	mu, sigma, size = 0, 1, 1
	spike = False
	V = I + float(np.random.normal(mu, sigma, size))

	if (vt1 >= reset_potential):
		vt2 = vrest
		spike = True
	else:
		vt2 = vrest + V + (vt1 - vrest - V) * math.exp((-t2 -t1)/tau)
	
	return vt2, spike

#USES FORMULA TO PARSE THROUGH TIME INTERVAL T
def problem2(I):
	bins = runtime()
	#find V
	spike_times, voltages = [],[]
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
				spike_times.append(i)
				spike_counter += 1

	return spike_counter, spike_times

"""
3 Plots
3 histogram of ISI with CV
"""
def problem5():
	sigmas = []
	for i in range(0, 100):
		sigmas.append(i)

	spike_counter, spike_times, ISI, cv = [],[],[],[]

	#runs the formula 100times to find ISI of 100 sigmas
	for sig in sigmas:
		#input where spike rate is about 50 plus rand
		I = 114 + float(np.random.normal(0, sig, 1))
		counter, times = problem2(I)
		# print(times)
		# print("\n\n\n")
		spike_counter.append(counter)
		spike_times.append(times)

	#runs 3 times for each sigma
	for times in spike_times:
		temp=[]
		ISI.append(temp)
		#runs through each spike time array
		for t in range(0, len(times)):
			if(t == 0):
				pass
			else:
				diff = times[t] - times[t-1] 
				#fill temp array w/ diff
				temp.append(diff)
	count = 0
	for x in ISI:
		n = len(x) 
		if(n==0):
			pass
		else:
			count+=1
			cv.append(round(coefficientOfVariation(x, n), 5)) 
	values=[]
	for i in range(0, count):
		values.append(i)
	plotV(cv, values)


if __name__ == "__main__":
	#plot()
	#test()
	problem5()

	
