# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:49:16 2026

@author: Kenza01
"""

from sklearn import svm

X = [[0, 0], [2, 2]]
y = [0.5, 2.5]

regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])