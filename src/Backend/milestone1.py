
from helper import *
from math import floor
import numpy

'''MILESTONE 1'''

def turnright(file) :
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[j,i,color] = matriksawal[matriksawal.shape[0]-i-1,j,color]
    else: 
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[j,i] = matriksawal[matriksawal.shape[0]-i-1,j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def turnleft(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[j,i,color] = matriksawal[i,matriksawal.shape[1]-j-1,color]
    else: 
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[j,i] = matriksawal[i,matriksawal.shape[1]-j-1]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def fliph(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[i,j,color] = matriksawal[i,matriksawal.shape[1]-1-j,color]
    else: 
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = matriksawal[i,matriksawal.shape[1]-1-j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def flipv(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[i,j,color] = matriksawal[matriksawal.shape[0] -i -1,j,color]
    else: 
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = matriksawal[matriksawal.shape[0] -i -1,j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def greyscale(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = 0.299 * matriksawal[i,j,0] + 0.587 * matriksawal[i,j,1] + 0.144 * matriksawal[i,j,2]
        stringgambar = matrikstostring(matrikshasil,file)
    else:
        stringgambar = matrikstostring(matriksawal,file)
    return stringgambar

def negative(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            if color < 3:
                for i in range (matriksawal.shape[0]):
                    for j in range (matriksawal.shape[1]):
                        matrikshasil[i,j,color] = 255 - matriksawal[i,j,color]
            else :
                matrikshasil[:,:,color] = matriksawal[:,:,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = 255 - matriksawal[i,j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def complement(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    if color < 3:
                        for i in range (matriksawal.shape[0]):
                            for j in range (matriksawal.shape[1]):
                                matrikshasil[i,j,color] = ~(matriksawal[i,j,color])
                    else :
                        matrikshasil[:,:,color] = matriksawal[:,:,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = ~(matriksawal[i,j])
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def zoomin(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0]*2, matriksawal.shape[1]*2, matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[i*2,j*2,color] = matriksawal[i,j,color]
                    matrikshasil[i*2+1,j*2+1,color] = matriksawal[i,j,color]
                    matrikshasil[i*2+1,j*2,color] = matriksawal[i,j,color]
                    matrikshasil[i*2,j*2+1,color] = matriksawal[i,j,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0]*2, matriksawal.shape[1]*2))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                    matrikshasil[i*2,j*2] = matriksawal[i,j]
                    matrikshasil[i*2+1,j*2+1] = matriksawal[i,j]
                    matrikshasil[i*2+1,j*2] = matriksawal[i,j]
                    matrikshasil[i*2,j*2+1] = matriksawal[i,j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def zoomout(file):
    matriksawal = filetomatriks(file)
    baris = floor(matriksawal.shape[0]/2)
    kolom = floor(matriksawal.shape[1]/2)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((baris,kolom, matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            for i in range (baris):
                for j in range (kolom):
                    temp = int(matriksawal[i*2,j*2,color]) + int(matriksawal[i*2+1,j*2+1,color]) + int(matriksawal[i*2+1,j*2,color]) + int(matriksawal[i*2,j*2+1,color])
                    matrikshasil[i,j,color] = round(temp/4)
    else:
        matrikshasil = numpy.zeros((baris,kolom))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (baris):
            for j in range (kolom):
                temp = int(matriksawal[i*2,j*2]) + int(matriksawal[i*2+1,j*2+1]) + int(matriksawal[i*2+1,j*2]) + int(matriksawal[i*2,j*2+1])
                matrikshasil[i,j] = round(temp/4)
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar
