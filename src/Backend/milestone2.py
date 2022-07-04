from helper import *
import math
import numpy

'''MILESTONE 2'''
def brighten(val,file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            if color < 3:
                for i in range (matriksawal.shape[0]):
                    for j in range (matriksawal.shape[1]):
                        matrikshasil[i,j,color] = matriksawal[i,j,color] + val
            else :
                matrikshasil[:,:,color] = matriksawal[:,:,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = matriksawal[i,j,color] + val
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def contrast(file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            Imax = matriksawal[:,:,color].max()
            Imin = matriksawal[:,:,color].min()
            if color < 3:
                for i in range (matriksawal.shape[0]):
                    for j in range (matriksawal.shape[1]):
                        matrikshasil[i,j,color] = round(int(matriksawal[i,j,color]) - int(Imin)) * (255/(int(Imax)-int(Imin)))
            else :
                matrikshasil[:,:,color] = matriksawal[:,:,color]
                    
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        Imax = matriksawal[:,:].max()
        Imin = matriksawal[:,:].min()
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = round(int(matriksawal[i,j]) - int(Imin)) * (255/(int(Imax)-int(Imin)))
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def transformasi(type,file):
    matriksawal = filetomatriks(file)
    if matriksawal.ndim == 3:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], matriksawal.shape[2]))  #Inisialisasi matriks kosong sebagai hasilnya
        for color in range (matriksawal.shape[2]):
            if color < 3:
                for i in range (matriksawal.shape[0]):
                    for j in range (matriksawal.shape[1]):
                        if type == "pangkat":
                            matrikshasil[i,j,color] = round(math.pow(matriksawal[i,j,color],0.85))
                        else: #logaritma
                            matrikshasil[i,j,color] = round(50*math.log(int(matriksawal[i,j,color]) + 1))
            else :
                matrikshasil[:,:,color] = matriksawal[:,:,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                if type == "pangkat":
                    matrikshasil[i,j,color] = round(math.pow(matriksawal[i,j],0.85))
                else: #logaritma
                    matrikshasil[i,j,color] = round(50*math.log(int(matriksawal[i,j]) + 1))
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

# base64String = transformasi("pangksat",'pasfoto.jpg')     