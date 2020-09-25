import numpy as np

class Neuron():
    
    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)
        
        #converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        # self.synaptic_weights = 2 * np.random.random((2, 1)) - 1
        self.synaptic_weights = [[0],[1],[1]]

        self.bias = 0

        self.inputs1 = np.array([1, -0.2, 0.5])
        self.inputs2 = np.array([1, 0.2, -0.5])
        self.inputs3 = np.array([1, 0.8, -0.8])
        self.inputs4 = np.array([1, 0.8, 0.8])

    def sigmoid(self, x):
        #applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def slenkstine(self, x):
        if (x >= 0).all():
            return 1
        else:
            return 0

    def sigmoid_derivative(self, x):
        #computing derivative to the Sigmoid function
        return x * (1 - x)

    def thinkSigmoid(self, inputs):
            #passing the inputs via the neuron to get output   
            #converting values to floats
            
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

    def thinkSlenkstine(self, inputs):
        inputs = inputs.astype(float)
        output = self.slenkstine(np.dot(inputs, self.synaptic_weights))
        return output

    def train(self, training_inputs, training_outputs, training_iterations):
        
        #training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            #siphon the training data via  the neuron
            output = self.thinkSigmoid(training_inputs)

            #computing error rate for back-propagation
            error = training_outputs - output
            
            #performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

if __name__ == "__main__":

    #initializing the neuron class
    neuron = Neuron()

    print("Beginning Randomly Generated Weights: ")
    print(neuron.synaptic_weights)

    #training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[1,-0.2, 0.5],
                                [1, 0.2, -0.5],
                                [1, 0.8, -0.8],
                                [1, 0.8, 0.8]])

    training_outputs = np.array([[0,0,1,1]]).T

    #training taking place
    neuron.train(training_inputs, training_outputs, 15000)

    print("Ending Weights After Training: ")
    print(neuron.synaptic_weights)

    print("Slenkstine[0] ar sigmoidine[1] aktyvacijos funkcija?")
    user_input_zero = int(input("Aktyvacijos funkcija: "))

    print("New Output data: ")

    if user_input_zero == 1 :
        print(neuron.thinkSigmoid(neuron.inputs4))
    elif user_input_zero == 0 :
        print(neuron.thinkSlenkstine(neuron.inputs4))
    
    
    