from helper import *
import random
import numpy

KERNEL_LEFT  =-2
KERNEL_RIGHT = 3

'''MILESTONE 3'''
def gaussblur(file):
    gaussarr = []
    for i in range(KERNEL_LEFT,KERNEL_RIGHT):
        for j in range(KERNEL_LEFT,KERNEL_RIGHT):
            gaussarr.append(gaussianfunc(i,j))
    total = 0
    for item in gaussarr:
        total += item
    for i in range (len(gaussarr)):
        gaussarr[i] = gaussarr[i]/total

    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    if color < 3:
                        total = 0
                        for k in range(KERNEL_LEFT,KERNEL_RIGHT):
                            for l in range (KERNEL_LEFT,KERNEL_RIGHT):
                                if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                    total += int(matriksawal[i+k,j+l,color])*gaussarr[5*k + l + 6]
                        matrikshasil[i,j,color] = total
                    else :
                        matrikshasil[i,j,color] = matriksawal[i,j,color]

    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                    total = 0
                    for k in range(KERNEL_LEFT,KERNEL_RIGHT):
                        for l in range (KERNEL_LEFT,KERNEL_RIGHT):
                            if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                total += int(matriksawal[i+k,j+l])*gaussarr[5*k + l + 6]
                    matrikshasil[i,j,color] = total
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def sharpen(file):
    gaussarr = []
    for i in range(KERNEL_LEFT,KERNEL_RIGHT):
        for j in range(KERNEL_LEFT,KERNEL_RIGHT):
            gaussarr.append(gausshighpassfunc(i,j))
    total = 0
    for item in gaussarr:
        total += item
    for i in range (len(gaussarr)):
        gaussarr[i] = gaussarr[i]/total

    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    if color < 3:
                        total = 0
                        for k in range(KERNEL_LEFT,KERNEL_RIGHT):
                            for l in range (KERNEL_LEFT,KERNEL_RIGHT):
                                if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                    total += int(matriksawal[i+k,j+l,color])*gaussarr[5*k + l + 6]
                        matrikshasil[i,j,color] = total
                    else :
                        matrikshasil[i,j,color] = matriksawal[i,j,color]

    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                    total = 0
                    for k in range(KERNEL_LEFT,KERNEL_RIGHT):
                        for l in range (KERNEL_LEFT,KERNEL_RIGHT):
                            if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                total += int(matriksawal[i+k,j+l])*gaussarr[5*k + l + 6]
                    matrikshasil[i,j,color] = total

    matrikshasil = matriksawal + 5*(matriksawal-matrikshasil)
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def noise(file):
    matriksawal = filetomatriks(file)
    mean = 0
    var = 500
    sigma = var**0.5
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        row,col,ch= matrikshasil.shape
        gauss = numpy.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        matrikshasil = matriksawal + gauss
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        row,col= matrikshasil.shape
        gauss = numpy.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        matrikshasil = matriksawal + gauss
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

# DRIVER
