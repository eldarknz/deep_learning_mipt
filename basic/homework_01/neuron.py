# https://stepik.org/lesson/316052/step/13?unit=301794

from functools import reduce

class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        sum_all = reduce(lambda z,y: z + y, list(map(lambda i, j: i*j, self.w, self.x))) 
        return self.f(sum_all)

    def backlog(self):
        return self.x
