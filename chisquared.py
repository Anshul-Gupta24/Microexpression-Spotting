'''
calculate chi squared distance between two histograms
'''


def chisquared(a,b):

	chi = 0.0

	for x,y in zip(a,b):
		
		#print x,y
		if(x+y>0):
			chi += (float(x-y)**2 / float(x+y))
		
	return chi


if __name__=='__main__':
	print chisquared([1,2],[3,4])
