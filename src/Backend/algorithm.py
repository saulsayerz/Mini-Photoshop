from PIL import Image, ImageChops
import numpy
import io
import base64
from io import BytesIO

'''HELPER'''

def filetomatriks(file):
    # Fungsi ini menconvert gambar ke matriks dengan mengecek modeawal terlebih dahulu.
    # Parameter : gambar
    # Return : matriks
    img = Image.open(file)
    matriks = numpy.array(img)  # convert gambarnya jadi matriks
    return matriks

def matrikstostring(matrikshasil,file):  
    # Fungsi ini mengubah matriks ke string, diubah ke unsigned int 0 - 255 dahulu sesuai elemen RGB / L
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
    matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0], 3))  #Inisialisasi matriks kosong sebagai hasilnya
    for color in range (3):
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[j,i,color] = matriksawal[matriksawal.shape[0]-i-1,j,color]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def turnleft(file):
    matriksawal = filetomatriks(file)
    matrikshasil = numpy.zeros((matriksawal.shape[1], matriksawal.shape[0], 3))  #Inisialisasi matriks kosong sebagai hasilnya
    for color in range (3):
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[j,i,color] = matriksawal[i,matriksawal.shape[1]-j-1,color]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def fliph(file):
    matriksawal = filetomatriks(file)
    matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], 3))  #Inisialisasi matriks kosong sebagai hasilnya
    for color in range (3):
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j,color] = matriksawal[i,matriksawal.shape[1]-1-j,color]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

def flipv(file):
    matriksawal = filetomatriks(file)
    matrikshasil = numpy.zeros((matriksawal.shape[0], matriksawal.shape[1], 3))  #Inisialisasi matriks kosong sebagai hasilnya
    for color in range (3):
        for i in range (matriksawal.shape[0]):
            for j in range (matriksawal.shape[1]):
                matrikshasil[i,j,color] = matriksawal[matriksawal.shape[0] -i -1,j,color]
    stringgambar = matrikstostring(matrikshasil,file)
    return stringgambar

'''MILESTONE 2'''
