#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import argparse
import encodings

parser = argparse.ArgumentParser(description='Creation of a Julia image')
parser.add_argument('-c', type=int, default=800,
                help='number of column, default')
parser.add_argument('-r', type=int, default=600,
                help='number of row, default 600')
parser.add_argument('-ce', type=int, default=2.0,
                help='centrature')
parser.add_argument('-d', default=0.27015,
                help='diagonal parameter')
parser.add_argument('-e', default=4,
                help='expasion parameter')
                
args = parser.parse_args()


def intensity(row, col, x, y):
    '''
    The output is the intensity colour of the pixel based in the dimension
    of the image and the position of the pixel in the image
    '''
    zx = 1.5*(x-col/2)/(0.5*1*col)
    zy = 1.0*(y-row/2)/(0.5*1*row)
    colour = 255
    t=True
    while t==True:

        condition_1 = zx*zx+zy*zy>=args.e
        condition_2 = colour <= 1
        if (condition_1 or condition_2):
            t=False
      
        a = zx*zx-zy*zy-0.7
        zy = args.ce*zx*zy+args.d
        zx = a
        colour -= 1
    return colour
   
def image_creation(row, col):
    '''
    This function takes as input the number of row and the number of columns
    and row which will form the Julia image.    
    '''
    A = np.zeros([row,col])

    for x in range(col):
        for y in range(row):
            A[y][x] = intensity(row, col, x, y)
    
    plt.imshow(A)
    plt.savefig('julia_image')


if __name__ == "__main__":
   image_creation( args.r,args.c)
