# -*- coding: utf-8 -*-
import numpy as np

a = [((1,2,3,4),(2,3,4,1)),(2,3,4,5)]
b = [1,1,1,1]


a1 = np.array(a)
a2 = np.mat(a)

print(a1.shape)
print(a1)
print(a2.shape)

