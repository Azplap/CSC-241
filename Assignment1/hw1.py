
import math, sys
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#PROBLEM WITH RESETS
#t1 and t2 markov chain
def problem1(vt1):
	vrest = -65
	spike_threshold = -50
	reset_potential = 30
	tau = 20

	mu, sigma, size = 0, 1, 1
	I = 5#float(np.random.normal(mu, sigma, size))
	reset = False

	if (vt1 >= reset_potential):
		vt2 = vrest
		reset = True
	else:
		rate = -(1/tau) * (vt1 - vrest) + I
		vt2 = vt1 + rate
	
	return vt2

def problem2():
	#create bins of 0.1ms
	bins = []
	for i in range(0, 5000):
		bins.append(i/1000)

	#find V
	voltages = []
	
	for i in bins:
		#base case
		if(i == 0):
			voltages.append(-65)
		else:
			#runs problem1 w/ previous voltage, t1 and t2
			vt1 = float(voltages[ int(i*1000-1) ])
			result=problem1( vt1 ) 
			voltages.append(result) 


	plt.style.use('seaborn-whitegrid')
	fig = plt.figure()
	ax = plt.axes()
	ax.plot(bins, voltages)
	plt.show()



if __name__ == "__main__":
	problem2()