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


def runtime():
	#create bins of 0.1ms
	bins, time_length = [], 0.5
	for i in range(0, int(time_length*1000)):
		bins.append(i/1000)
	return bins


def plotV(v1, v2, v3, sig1, sig2, sig3):
	bins = runtime()

	plt.subplot(1, 3, 1)
	plt.plot(bins, v1)
	title = "Membrane Potentials with sigma = "+str(sig1)
	plt.title(title)
	plt.xlabel("Time (t)")
	plt.ylabel("Output (V)")

	plt.subplot(1, 3, 2)
	plt.plot(bins, v2)
	title = "Membrane Potentials with sigma = "+str(sig2)
	plt.title(title)
	plt.xlabel("Time (t)")
	plt.ylabel("Output (V)")

	plt.subplot(1, 3, 3)
	plt.plot(bins, v3)
	title = "Membrane Potentials with sigma = "+str(sig3)
	plt.title(title)
	plt.xlabel("Time (t)")
	plt.ylabel("Output (V)")

	plt.style.use('seaborn-whitegrid')
	#plt.tight_layout()
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

#PLOTS V(t) OVER TIME
def problem2(I):
	bins = runtime()
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

	return voltages

"""
3 Plots
3 of V but with gaussian dist
"""
def problem4():

	sigmas = [1,10,15]
	voltages = []
	for sig in sigmas:
		#input where spike rate is about 50 plus rand
		I = 114 + float(np.random.normal(0, sig, 1))
		voltages.append(problem2(I))

	plotV(voltages[0], voltages[1], voltages[2], sigmas[0], sigmas[1], sigmas[2])


if __name__ == "__main__":
	#plot()
	problem4()
