import numpy as np
import os

class Neuronas:
    def __init__(self, data, weights, data_outputs):
        self.data = data
        self.data_outputs = data_outputs
        self.weights = weights

# slenkstine funkcija
    def slenkstine(self, a):
        return 1 if a > 0 else 0

# sigmoidine funkcija
    def sigmoidine(self, a):
        return 1 / (1 + np.exp(-a))

# iejimo reiksmiu ir svoriu sandaugu suma
    def suma(self, data):
        a = np.dot(data, self.weights)
        return a

# nauju svoriu gavimas
    def paklaida(self, y, i, l_rate):
        error = self.data_outputs[i] - y
        if y != self.data_outputs[i]:
            for j in range(len(self.weights)):
                self.weights[j] = self.weights[j] + \
                    (l_rate * error * self.data[i][j])

#perceptrono veikimo paklaida E(W) - skirtumu tarp neurono isejime 
#gautu reiksmiu ir norimu reiksmiu sumos funkcija
    def paklaidaEW(self, data, funkcija, data_outputs):
        paklaidaE = 0
        for i in range(len(data)):
            paklaidaE += self.calculateOutput(data[i], funkcija) - data_outputs[i][0] 
        return paklaidaE
            

# neurono apmokymo funkcija
# funkcija = 0, jei pasirinkta slenkstine aktyvacijos funkcija
# funkcija = 1, jei sigmoidine
    def train(self, funkcija, iterations, l_rate):
        for _ in range(iterations):
            for i in range(len(self.data)):
                a = self.suma(self.data[i])
                if funkcija == 1:
                    y = self.sigmoidine(a)
                else:
                    y = self.slenkstine(a)

                # apskaičiuojama paklaida
                self.paklaida(y, i, l_rate)

#santykis tarp teisingai klasifikuotu ir visu duomenu
    def tikslumas(self, data, funkcija, data_outputs):
        teisingiOutputs = 0
        for i in range(len(data)):
            if int(round(self.calculateOutput(data[i], funkcija))) == data_outputs[i][0]:
                teisingiOutputs += 1
        return teisingiOutputs / len(data)
            

# skaiciuojama isejimo reiksme
    def calculateOutput(self, data, funkcija):
        a = self.suma(data)
        if funkcija == 0:
            return self.slenkstine(a)
        else:
#Naudojant sigmoidine funkcija, neurono isejimo reiksmes yra intervale (0,1), todel
#vertinant rezultata, sios reiksmes yra suapvalinamos
            return self.sigmoidine(a)[0] #int(round(self.sigmoidine(a)[0]))

if __name__ == '__main__':
    
    def klasifikuoti(klase1, klase2, learningRate, iterations, funkcija):
        data = []
        dataMokymui = []
        dataTestavimui = []
        count = 0
        count2 = 0

        for item in klase1:
            a = [float(i) for i in item.split(',')]
            a.insert(0, 1.0) 
            data.append(a)
            if count < 40:
                dataMokymui.append(a)
            if count >= 40:
                dataTestavimui.append(a)
            count += 1

        for item2 in klase2:
            b = [float(j) for j in item2.split(',')]
            b.insert(0, 1.0) 
            data.append(b)
            if (inputDuomenys == 0 and count2 < 80) or (inputDuomenys == 1 and count2 < 40):
                dataMokymui.append(b)
            if (inputDuomenys == 0 and count2 >= 80) or (inputDuomenys == 1 and count2 >= 40):
                dataTestavimui.append(b)
            count2 += 1
        
        if inputDuomenys == 0:
            output1 = np.array([[0] * 40]).T
            output2 = np.array([[1] * 80]).T
            data_outputsMokymui = np.concatenate((output1, output2))
            output3 = np.array([[0] * 10]).T
            output4 = np.array([[1] * 20]).T
            data_outputsTestavimui = np.concatenate((output3, output4))
        if inputDuomenys == 1:
            output1 = np.array([[0] * 40]).T
            output2 = np.array([[1] * 40]).T
            data_outputsMokymui = np.concatenate((output1, output2))
            output3 = np.array([[0] * 10]).T
            output4 = np.array([[1] * 10]).T
            data_outputsTestavimui = np.concatenate((output3, output4))

        weights = [0, 0, 0, 0, 0] 

        neuronas = Neuronas(dataMokymui, weights, data_outputsMokymui)
        neuronas.train(funkcija, iterations, learningRate)
        print("svoriai", neuronas.weights)
        print("paklaida:  ", neuronas.paklaidaEW(dataTestavimui, funkcija, data_outputsTestavimui))
        print("tikslumas:  ", neuronas.tikslumas(dataTestavimui, funkcija, data_outputsTestavimui))

#nuskaitomi duomenys is failo
    setosa = []
    versicolor = []
    virginica = []
    versicolorVirginica = []

    with open("PATH TO IRIS.DATA", 'r') as read_obj:
        for line in read_obj:
            if "setosa" in line:
                setosa.append(line.replace(',Iris-setosa\n', ''))
            if "versicolor" in line:
                versicolor.append(line.replace(',Iris-versicolor\n', ''))
            if "virginica" in line:
                virginica.append(line.replace(',Iris-virginica\n', ''))

#sudaroma versicolor-virginica klase
    versicolorVirginica.append(versicolor)
    versicolorVirginica.append(virginica)
    versicolorVirginica = [j for i in versicolorVirginica for j in i]

#gaunami duomenys is vartotojo
    inputDuomenys = int(input("Pasirinkite duomenu rinkini [0] [1]: "))
    inputGreitis = float(input("Mokymo greitis: "))
    inputIteracijos = int(input("Iteracijos: "))
    inputFunkcija = int(input("Slenkstine[0] ar sigmoidine[1] aktyvacijos funkcija?: "))

    if inputDuomenys == 0:
        klasifikuoti(setosa, versicolorVirginica, inputGreitis, inputIteracijos, inputFunkcija)
    elif inputDuomenys == 1:
        klasifikuoti(versicolor, virginica, inputGreitis, inputIteracijos, inputFunkcija)
    else: print("neteisingi duomenys")

