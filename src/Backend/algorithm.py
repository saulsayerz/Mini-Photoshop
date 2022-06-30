from PIL import Image, ImageChops
import numpy
import io
import base64
from io import BytesIO

'''HELPER'''

def filetomatriks(file):
    # Fungsi ini menconvert gambar ke matriks numpy
    # Parameter : gambar
    # Return : matriks
    img = Image.open(file)
    matriks = numpy.array(img)  # convert gambarnya jadi matriks
    return matriks

def matrikstostring(matrikshasil,file):  
    # Fungsi ini mengubah matriks ke string, diubah ke unsigned int 0 - 255 dahulu sesuai elemen RGB
    # Parameter : matriks
    # Return : string
     
    numpy.clip(matrikshasil,0,255,matrikshasil)
    matriksunsigned = matrikshasil.astype('uint8') 
    hasilgambar = Image.fromarray(matriksunsigned)
    buffered = BytesIO()
    hasilgambar.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

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
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0]))  #Inisialisasi matriks kosong sebagai hasilnya
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
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0]))  #Inisialisasi matriks kosong sebagai hasilnya
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
            for i in range (matriksawal.shape[0]):
                for j in range (matriksawal.shape[1]):
                    matrikshasil[i,j,color] = 255 - matriksawal[i,j,color]
    else:
        matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0]))  #Inisialisasi matriks kosong sebagai hasilnya
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j] = 255 - matriksawal[i,j]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar