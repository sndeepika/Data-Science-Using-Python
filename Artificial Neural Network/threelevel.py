#!/usr/bin/env python3
import numpy as np
from random import randrange
from scipy.special import expit

if __name__ == "__main__":

    a = np.load('../digits.npy')                   
    b = a.reshape(10,500,400)                      # reshape to [digit, picture number, pixels]
    c  = b[0:10,np.random.permutation(500),0:400]  

    train = c[0:10,0:400,0:400]                    # 80% for training
    test  = c[0:10,400:500,0:400]                  # 20% for testing

    hidden = 50
    alpha = 0.1
    w1 = np.random.randn(400*hidden).reshape(hidden,400)
    w2 = np.random.randn(10*hidden).reshape(10,hidden)

    totalerr = 0
    for i in range(1,11):
        dig = randrange(10)              
        pix = randrange(400)             
        x = train[dig,pix]              
        y = np.zeros(10)                 
        y[dig] = 1.0
        z2 = np.matmul(w1,x)               # input to next layer
        a2 = expit(z2)
        z3 = np.matmul(w2,a2)
        a3 = expit(z3)

        predict = np.argmax(a3)          # prediction
        print(a3)
        print(predict)

        delta3 = (a3 - y)*a3*(1.0 - a3)
        delta2 = np.matmul(w2.T, delta3)*a2*(1.0 - a2)

        print(delta2)
        print(delta3)
        break
