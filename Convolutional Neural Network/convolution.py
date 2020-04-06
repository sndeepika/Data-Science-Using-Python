#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def readpgmfile(filename='D:/DataScience/convolutional_neural_network/cow.pgm'):
    with open(filename,'r') as fd:
       magic = fd.readline()
       wid, hgt  = tuple(map(int, fd.readline().strip().split()))
       pmax  = int(fd.readline())
       print(wid,hgt,pmax)
       a = []
       for line in fd.readlines():
          a += list(map(int, line.strip().split()))
    return a, wid, hgt

if __name__ == "__main__":
 
    
    test, w, h = readpgmfile('D:/DataScience/convolutional_neural_network/cow.pgm')
    im1 = np.array(test).reshape(h,w)
    im1 = 255 - im1

    fig, ax = plt.subplots(1,4)
    ax[0].imshow(im1, cmap='Greys')

    im2 =np.abs(im1[ : , 1: ] - im1[ : , 0:-1])
    ax[1].imshow(im2, cmap='Greys')

    im3 = np.abs(im1[1: ,  : ] - im1[0:-1, : ])
    ax[2].imshow(im3, cmap='Greys')

    im4 = im2[1: , :] + im3[ :, 1: ]

    im4max = np.max(im4)
    im4min = np.min(im4)
    im4 = np.round(2.0 * (im4 - im4min)/(im4max - im4min))
    ax[3].imshow(im4, cmap='Greys')

    plt.show()
