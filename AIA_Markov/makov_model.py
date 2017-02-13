import random
class mom:
    """
        @param a: Matriz de probabilidad de transicción
        @param b: Probabilidad de observación
        @param pi: Vector de posibles estados de transicción
        @markov Instancia un modelo oculto de markov
    """
    def __init__(self,pi, a, b):
        self.a = a
        self.b = b
        self.pi = pi

    def fordward(self, observations, pi, a, b, t):
        self.__init__(pi,a,b)
        alfa = []
        for i in range(len(self.b)):
            for j in self.b[i]:
                alfa[i][j] = j*(self.pi[i])
            if i == 0:
                return self.pi * b[0][0]
            else:
                for k in t:
                    for j in n:
                        a[j]
    def viterbi(self):
        pass

    """
        @param n: b
    """
    def samples(self, n):
        pass

class grid(mom):
    """
            @grid Instancia de una cuadricula
    """
    def __init__(self, grid):
        pass