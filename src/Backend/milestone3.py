import sys
sys.path.insert(0, 'Backend/')
from helper import *
import numpy

'''MILESTONE 3'''
def gauss(type,file):
    gaussarr = []
    for i in range(-2,3):
        for j in range(-2,3):
            if type == "blur":
                gaussarr.append(gaussianfunc(i,j))
            elif type == "sharpen":
                gaussarr.append(gausshighpassfunc(i,j))
            else: #smooth
                gaussarr.append(gausslowpassfunc(i,j))
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
                        for k in range(-2,3):
                            for l in range (-2,3):
                                if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                    total += int(matriksawal[i+k,j+l,color])*gaussarr[5*k + l + 6]
                        matrikshasil[i,j,color] = total
                    else :
                        matrikshasil[:,:,color] = matriksawal[:,:,color]

    else:
        matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                    total = 0
                    for k in range(-2,3):
                        for l in range (-2,3):
                            if i+k >= 0 and i+k < matriksawal.shape[0] and j+l >= 0 and j+l < matriksawal.shape[1]:
                                total += int(matriksawal[i+k,j+l])*gaussarr[5*k + l + 6]

                    matrikshasil[i,j,color] = total
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar