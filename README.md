# Mini-Photoshop
> A website-based-app to edit photos using Python Flask as Backend

## Table of Contents

- [Mini-Photoshop](#mini-photoshop)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks / Libraries](#frameworks--libraries)
  - [Screenshots](#screenshots)
  - [Features](#features)
  - [Requirements and Setup](#requirements-and-setup)
  - [How to Run](#how-to-run)
  - [References](#references)
  - [Contact](#contact)

## General Information
Saat ini, terdapat berbagai macam aplikasi yang dapat digunakan untuk melakukan photo editing. Beberapa contoh aplikasi yang mungkin kamu ketahui adalah Adobe Photoshop, Adobe Lightroom, Picsart, Snapseed, VSCO, dan lain lain. Beberapa fitur editing yang ada pada aplikasi tersebut dapat dilakukan dengan pendekatan pemrosesan matriks seperti yang sudah dipelajari pada mata kuliah Aljabar Linier dan Geometri dan Interpretasi dan Pengolahan Citra. *Sayerz Mini-Photoshop* merupakan aplikasi berbasis web yang menerapkan photo editing tersebut dengan pendekatan pengolahan matriks. Aplikasi ini menggunakan Front-end dan Back-end secara terpisah, kemudian menggunakan Python dengan library Flask untuk menjadikannya sebagai REST-api sehingga dapat dipanggil oleh Frontend. Baik spesifikasi atau fitur lain pada aplikasi ini akan diperjelas lagi di bawah.

## Technologies Used

### Languages
- Python : Backend
- Javascript : Frontend

### Frameworks / Libraries
- Bootstrap : Untuk mempermudah desain web dengan memperoleh template komponen dengan cepat
- base64 : Untuk mempermudah melakukan encoding dan decoding dari sebuah url gambar menjadi string untuk dapat dikirim dari backend ke frontend
- PIL (Image) : Untuk membuka dan memproses gambar
- numpy : Untuk mengkonversi gambar menjadi sebuah matriks serta melakukan operasi matematika
- Flask : Untuk menjadikan python menjadi REST-api sehingga menjadi backend yang terpisah dengan frontend

## Screenshots
![main_page.png](./src/Frontend/assets/MainPage.png)
![photoshop.png](./src/Frontend/assets/photoshop.png)

## Features
Fitur - fitur yang tersedia dalam aplikasi ini untuk mengolah citra dapat diakses melalui sidebar yang tersedia. Setiap fitur ditandai dengan sebuah icon untuk membedakannya. Dari paling atas, fungsi icon tersebut adalah:
- Rotate Left : Operasi geometri untuk memutar gambar 90 derajat berlawanan arah jarum jam. Cara kerjanya adalah dengan membuat matriks baru yang dimensi panjang x lebarnya ditukar, kemudian meletakkan tiap titik (x,y) pada matriks awal menjadi (-y,x)
- Rotate Right : Operasi geometri untuk memutar gambar 90 derajat searah jarum jam. Cara kerjanya adalah dengan membuat matriks baru yang dimensi panjang x lebarnya ditukar, kemudian meletakkan tiap titik (x,y) pada matriks awal menjadi (y,-x)
- Flip Horizontal : Operasi geometri untuk mencerminkan citra secara sumbu x. Cara kerjanya adalah dengan mengubah tiap titik (x,y) pada matriks awal menjadi (-x,y)
- Flip Vertical : Operasi geometri untuk mencerminkan citra secara sumbu y. Cara kerjanya adalah dengan mengubah tiap titik (x,y) pada matriks awal menjadi (x,-y)
- Negative : Operasi untuk memberikan warna yang negatif (kebalikan) dari gambar awal. Cara kerjanya adalah menukar tiap elemen warna p pada matriks menjadi 255 - p
- Complement : Operasi untuk menukar warna secara komplemen dari gambar awal. Karena elemen warna matriks sudah berupa unsigned, cara kerjanya cukup dengan memberikan komplemen untuk tiap elemennya (misal 00001111 menjadi 11110000)
- Zoom In : Operasi geometri untuk melakukan perbesaran gambar. Cara kerjanya dengan membuat matriks baru yang ukurannya panjang dan lebarnya masing masing dua kali lebih besar, lalu untuk tiap pixel (x,y) pada matriks awal akan dicopy ke 4 elemen matriks baru yang bersebelahan.
- Zoom Out : Operasi geometri untuk melakukan perkecilan gambar. Cara kerjanya dengan membuat matriks baru yang ukuran panjang dan lebarnya masing masing setengah dari matriks awal, lalu untuk tiap 4 pixel berdekatan pada matriks awal akan dirata - rata menjadi posisi yang bersesuaian di matriks baru.
- Brighten : Operasi untuk memberikan mempercerah warna pada gambar. Cara kerjanya adalah dengan menambah 50 untuk tiap elemen pixel pada gambar
- Darken : Operasi untuk memberikan mempergelap warna pada gambar. Cara kerjanya adalah dengan mengurangi 50 untuk tiap elemen pixel pada gambar
- GrayScale : Operasi untuk mengubah gambar berwarna menjadi gambar hitam putih. Caranya adalah dengan membuat matriks baru yang dimensinya hanya 2 (panjang x lebar), kemudian untuk tiap pixel RGB akan dirata-rata dengan formula 0.299R + 0.587G + 0.144B
- Contrast Stretching : Operasi untuk memperjelas kontras pada gambar. Cara kerjanya cukup ringkas menggunakan formula sebagaimana tersedia pada referensi (referensi kedua)
- Transformasi Pangkat : Melakukan transformasi pixel pada gambar dengan fungsi pangkat s = cr^y. Konstanta yang diambil adalah c = 1 dan y = 0.85
- Transformasi Log : Melakukan transformasi pixel pada gambar dengan fungsi logaritma s = clog(r+1). Konstanta yang diambil adalah c = 50
- Gaussian Blur : Memberikan efek blur pada gambar sesuai fungsi gauss. Cara kerjanya adalah dengan membuat kernel berukuran 5x5 yang nilainya terbesar sesuai fungsi gauss, kemudian untuk tiap pixel pada matriks baru kita terapkan konvolusi yakni dengan menjumlahkan pixel lama yang disekitarnya dikalikan dengan posisi kernel yang bersesuaian.
- Sharpen : Untuk mempertajam citra. Cara kerjanya serupa dengan fitur Gaussian Blur, namun menggunakan formula Gaussian Highpass. Kemudian, kita menjumlahkan matriks awal dengan c(matriks awal - matriks blur). Diambil c sebesar 5 sebagaimana tertulis di referensi
- Gaussian Noise : Untuk memberikan efek noise / grainy pada citra. Cara kerjanya dengan membentuk sebuah matriks baru yang ukuran serta dimensinya sama dengan matriks awal, kemudian kita mengisi elemen tersebut hingga tersusun menjadi distribusi normal sesuai fungsi gauss (karena distribusi normal sudah pasti menggunakan fungsi gauss). Kemudian, kita cukup menjumlahkan matriks awal dengan matriks baru tersebut.
- Undo : Untuk mengembalikan operasi edit menjadi satu langkah sebelumnya. Gambar setiap operasi akan disimpan dalam bentuk encoded string dalam array, sehingga kita hanya perlu memundurkan indeks gambarnya sebanyak 1. Apabila undo sudah mentok, maka tidak akan melakukan apa apa
- Redo : Serupa seperti undo, namun memajukan indeks sebanyak 1
- Reset : Untuk mengembalikan gambar menjadi semula sebelum diedit
- Save : Untuk mengunduh gambar setelah diedit dengan format nama {namafile awal}-edited.{formatfile awal}

**NOTE: Untuk mengatasi adanya distortion pada gambar setelah diolah, maka untuk tiap fitur akan divalidasi dengan melakukan rounding ke angka terdekat kemudian diclip agar nilai pixelnya hanya berada dalam range 0 - 255**

## Requirements and Setup
- Python 3 diperlukan dalam program ini. Anda bisa mendownloadnya pada link <a href="http://www.python.org/downloads/">berikut</a>, atau agar mempermudah anda dapat menonton proses instalasinya dari link <a href="https://www.youtube.com/watch?v=Kn1HF3oD19c">berikut</a>.

- pip harus terinstall. Anda bisa melakukan instalasi pada link <a href="https://pip.pypa.io/en/stable/installation/">berikut</a>. Pastikan juga pip harus ada pada PATH dengan cara <a href="https://www.youtube.com/watch?v=UTUlp6L2zkw">berikut</a>.

- Terdapat beberapa library yang harus terinstall untuk menjalankan program ini, yakni numpy, PIL Image, dan Flask. Anda bisa menggunakan pip yang sudah diinstall sebelumnya. Buka powershell atau terminal pada komputer anda, kemudian masukkan sintaks berikut: 
```
pip install numpy
pip install Flask
pip install PIL
```

- Clone repository ini ke dalam komputer anda dengan cara memasukkan sintaks berikut pada powershell atau terminal:
```
git clone https://github.com/saulsayerz/Mini-Photoshop
```

## How to Run
- Menjalankan backend dengan cara membuka terminal pada root repository yang sudah anda clone, kemudian cd ke src/backend. kemudian, masukkan sintaks berikut:
```
Flask run
```

- Menjalankan frontend dengan membuka terminal lain pada root repository, kemudian cd ke src/frontend. Kemudian, anda dapat membuat sebuah server http. Sebagai contoh, anda dapat memasukkan sintaks berikut:
```
python -m http.server 8000
```
- Website sudah bisa diakses melalui browser anda dengan link localhost:8000
- Silahkan upload gambar yang anda ingin edit pada box upload, kemudian klik tombol submit
- Box photoshop untuk mengedit foto akan terbuka, dan anda bisa melakukan fitur atau operasi edit yang tersedia pada sidebar (termasuk save)

## References :
- <a href="https://informatika.stei.itb.ac.id/~rinaldi.munir/Citra/2020-2021/05-Operasi-dasar-pengolahan-citra-2021.pdf">Milestone 1 dan Image Brightening</a>
- <a href="https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33">Contrast Stretching</a>
- <a href="https://informatika.stei.itb.ac.id/~rinaldi.munir/Citra/2019-2020/09-Image-Enhancement-Bagian1.pdf">Transformasi log dan pangkat</a>
- <a href="https://informatika.stei.itb.ac.id/~rinaldi.munir/Citra/2020-2021/10-Image-Enhancement-Bagian3-2021.pdf">Image Enchancement Bagian 3</a>
- <a href="https://www.pixelstech.net/article/1353768112-Gaussian-Blur-Algorithm#:~:text=Usually%2C%20image%20processing%20software%20will,Gaussian%20distribution%20to%20process%20images">Gaussian Blur Algorithm</a>
- <a href="https://stackoverflow.com/questions/4993082/how-can-i-sharpen-an-image-in-opencv">How to Sharpen Image in Python</a> 
- <a href="https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv">How to add Gaussian Noise in Python</a> 

## Contact :
> Saul Sayers (13520094), Informatika ITB 2020. 

More detailed contact: 
- Line : saulsayerz
- Instagram : <a href="https://www.instagram.com/saulsayers/?hl=en">saulsayers</a> 
- Linkedin : <a href="https://www.linkedin.com/in/saulsayers/?originalSubdomain=id">saulsayers</a>
- github : <a href="https://github.com/saulsayerz">saulsayerz</a>
- email : saulsayers@gmail.com
