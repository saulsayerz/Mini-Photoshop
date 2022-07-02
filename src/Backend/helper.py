from PIL import Image
import numpy
import sys
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
    hasilgambar.save(buffered, format=Image.open(file).format)
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

def complement_val(val):
    b = (~val).to_bytes(1, byteorder=sys.byteorder, signed=True)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=False)

def gaussianfunc(x,y):
    # Fungsi ini menghitung nilai gaussian
    # Parameter : x, y
    # Return : nilai gaussian

    return (1/(2*numpy.pi*1.5**2))*numpy.exp(-((x**2)+(y**2))/(2*1.5**2))

def gausshighpassfunc(x,y):
    # Fungsi ini menghitung nilai gaussian highpass
    # Parameter : x, y
    # Return : nilai gaussian highpass

    return 1 - numpy.exp(-((x**2)+(y**2))/(1.5**2))

def gausslowpassfunc(x,y):
    # Fungsi ini menghitung nilai gaussian lowpass
    # Parameter : x, y
    # Return : nilai gaussian lowpass

    return numpy.exp(-((x**2)+(y**2))/(1.5**2))
