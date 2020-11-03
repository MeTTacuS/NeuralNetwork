import numpy as np


class Neuronas:
    def __init__(self, data, weights, data_outputs):
        self.data = data
        self.data_outputs = data_outputs
        self.weights = weights

# slenksine funkcija
    def slenkstine(self, a):
        return 1 if a > 0 else 0

# sigmoidinė funkcija
    def sigmoidine(self, a):
        return 1 / (1 + np.exp(-a))

# įėjimo reikšmių ir svorių sandaugų suma
    def suma(self, data):
        a = np.dot(data, self.weights)
        return a

# mokymo paklaida ir naujų svorių gavimas
    def paklaida(self, y, i, l_rate=1):
        error = self.data_outputs[i] - y
        if y != self.data_outputs[i]:
            for j in range(len(self.weights)):
                self.weights[j] = self.weights[j] + \
                    (l_rate * error * self.data[i][j])

# neurono apmokymo funkcija
# funkcija = 0, jei pasirinkta slenkstinė aktyvacijos funkcija
# funkcija = 1, jei sigmoidinė
    def train(self, funkcija, iterations=1000, l_rate=1):
        for _ in range(iterations):
            for i in range(len(self.data)):
                a = self.suma(self.data[i])
                if funkcija == 1:
                    y = self.sigmoidine(a)
                else:
                    y = self.slenkstine(a)

                # apskaičiuojama paklaida
                self.paklaida(y, i)


# skaičiuojama išėjimo reikšmė

    def calculateOutput(self, data, funkcija):
        a = self.suma(data)
        if funkcija == 0:
            return self.slenkstine(a)
        else:
            # Kadangi sigmoidinės funkcijos reikšmės yra intervale (0, 1),
            # nustatoma, kad jei reikšmė mažesnė nei 0,09 - grąžinamas 0,
            # kitu atveju grąžinamas 1
            if self.sigmoidine(a) < 0.09:
                return 0
            else:
                return 1


if __name__ == '__main__':
    # nulinis įėjimas, x1, x2
    data = [[1.0, -0.2, 0.5],
            [1.0, 0.2, -0.5],
            [1.0, 0.8, -0.8],
            [1.0, 0.8, 0.8]]

    data_outputs = np.array([[0, 0, 1, 1]]).T

    weights = [0, 0, 0]

    neuronas = Neuronas(data, weights, data_outputs)
    neuronas.train(1)
    print(weights)

    print("Slenkstine[0] ar sigmoidine[1] aktyvacijos funkcija?")
    user_input = int(input("Aktyvacijos funkcija: "))

    print(neuronas.calculateOutput(data[3], user_input))
