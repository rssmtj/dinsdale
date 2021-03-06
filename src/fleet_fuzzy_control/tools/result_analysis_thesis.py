#!/usr/bin/env python


from __future__ import division
import sys
sys.dont_write_bytecode = True
import numpy as np
from thesis import *
import matplotlib.pyplot as plt


class ResultAnalysis:
    """ Analyse the logged data after execution """

    def __init__(self, number):
        """ Initialize data to be analyzed """

        self.data = {}
        self.data['y'] = [[] for i in xrange(number)]
        self.data['u'] = [[] for i in xrange(number)]
        self.data['v'] = [[] for i in xrange(number)]
        self.data['w'] = [[] for i in xrange(number)]
        self.data['g'] = [[] for i in xrange(number)]
        self.data['h'] = [[] for i in xrange(number)]

    def analyze(self):
        t = np.arange(0, 10, .1)
        p0 = np.array([x[0:2] for x in self.data['y'][0]])
        p1 = np.array([x[0:2] for x in self.data['y'][1]])
        p2 = np.array([x[0:2] for x in self.data['y'][2]])
        
        fig, ax = newfig(.7)
        ax.plot(p0[:, 0], p0[:, 1], label = 'boat 0')
        ax.plot(p1[:, 0], p1[:, 1], label = 'boat 1')
        ax.plot(p2[:, 0], p2[:, 1], label = 'boat 2')
        
        o = [[90, 0, 40],
             [35, 5, 50],
             [25, -30, 25],
            ]
        xx = np.zeros((200, 4))
        yy = np.zeros((200, 4))
        for i in xrange(3):
            for j in range(200):
                temp = 2*np.pi*j/200
                xx[j,i] = o[i][0] + o[i][2]/3 * np.cos(temp)
                yy[j,i] = o[i][1] + o[i][2]/3 * np.sin(temp)
            ax.plot(xx[:, i], yy[:, i], color='k', linestyle='-.')
        
        for j in range(200):
            temp = 2*np.pi*j/200
            xx[j,3] = 150 + 1 * np.cos(temp)
            yy[j,3] = 0 + 1 * np.sin(temp)
        ax.plot(xx[:, 3], yy[:, 3], color='m')
        
        ax.set_aspect('equal')
        ax.legend()
        ax.set_xlabel(r'$x\, [\mathrm{m}]$')
        ax.set_ylabel(r'$y\, [\mathrm{m}]$')
        #plt.show()
        savefig('boats')
