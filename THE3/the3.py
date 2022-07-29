import math	

def linear(X,Weights): 
	outputSize = len(Weights)
	inputSize = len(Weights[0])
	result = []
	sum = 0
	for i in range(outputSize):
		for j in range(inputSize):
			sum += X[j]*Weights[i][j]
		result.append(sum)
		sum = 0
	return result		

def relu(X): 
	result = []
	for i in X:
		result.append(max(0,i))
	return result	
		
def sigmoid(X):
	result = []
	for i in X:
		if i >= 700:
			result.append(1)
		elif -700 < i < 700:
			result.append(1/(1+math.e**(-i)))
		elif i <= -700:
			result.append(0)
	return result

def forward_pass(Network,X):	
	copyX = X[:]
	for i in Network: 
		if type(i) == list: 
			copyX = linear(copyX,i[1])

		elif i[:4] == "relu": 
			copyX = relu(copyX)

		elif i[:7] == "sigmoid": 
			copyX = sigmoid(copyX)
	return copyX





