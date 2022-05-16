##practica 5
import numpy as np
from matplotlib import pyplot as plt
import math as ma
import cv2 #opencv

def binary(m1):
    img = m1
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
    cv2.imshow('binary',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def binaryinv(m1):
    img = m1
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('binaryinv',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Trunc(m1):
    img = m1
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_TRUNC)
    cv2.imshow('Trunc',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    
def To_Zero(m1):
    img = m1
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_TOZERO)
    cv2.imshow('To_Zero',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
def Tz_inv(m1):
    img = m1
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('Tz_inv',threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Mean(m1):
    img = m1
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imshow('mean',th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
def Gaus(m1):
    img = m1
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('gaus',th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
def Otsu(m1):
    img = m1
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Otsu',threshold2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     
    
    
ima1 = cv2.imread('bookpage.png')
cv2.imshow('Imagen1', ima1)
x=cv2.waitKey(0)

while True:

    if x == ord("d"):
        binary(ima1)

        
    if x == ord("d"):
        binaryinv(ima1)

        
    if x == ord("d"):
        Trunc(ima1)

        
    if x == ord("d"):
        To_Zero(ima1)

    if x == ord("d"):
        Tz_inv(ima1)
        
    if x == ord("d"):
        Mean(ima1)

        
    if x == ord("d"):
        Gaus(ima1)

        
    if x == ord("d"):
        Otsu(ima1)
      
        

    cv2.destroyAllWindows()        
    break
