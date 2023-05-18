#OpenCV Python Program Deteksi cabe

## Program Deteksi Cabe

Program ini menggunakan OpenCV dan Tkinter untuk mendeteksi cabe pada gambar. Program dapat membuka file gambar, melakukan konversi warna RGB ke HSV, segmentasi warna untuk deteksi cabe, morfologi untuk menghilangkan noise, mendeteksi kontur untuk mengambil area cabe, dan menampilkan jumlah cabe yang terdeteksi pada gambar.

### Dependencies
- `tkinter`
- `cv2`
- `numpy`
- `os`

Pastikan semua dependencies terinstal sebelum menjalankan program.

### Fungsi-fungsi Utama

#### `save_result(file_path, img, contours)`

Fungsi ini digunakan untuk menyimpan gambar dengan kotak posisi cabe yang ditandai.

**Argumen:**
- `file_path`: Path file gambar yang akan disimpan.
- `img`: Gambar asli.
- `contours`: Kontur dari cabe yang terdeteksi.

**Output:**
- `count`: Jumlah cabe yang terdeteksi pada gambar.

#### `save_info(file_name, count)`

Fungsi ini digunakan untuk menyimpan informasi deteksi cabe ke file teks.

**Argumen:**
- `file_name`: Nama file gambar yang terdeteksi.
- `count`: Jumlah cabe yang terdeteksi pada gambar.

#### `open_image()`

Fungsi ini digunakan untuk membuka file gambar, melakukan konversi warna RGB ke HSV, segmentasi warna untuk deteksi cabe, morfologi untuk menghilangkan noise, dan mendeteksi kontur untuk mengambil area cabe.

#### `process_images()`

Fungsi ini digunakan untuk menjalankan proses deteksi cabe saat tombol "Start" ditekan. Tombol akan dinonaktifkan setelah proses selesai.

### Cara Menjalankan Program

1. Pastikan semua dependencies terinstal.
2. Jalankan program dengan menjalankan script utama.

```bash
python main.py
```


### Struktur Folder

Pastikan struktur folder berikut ada sebelum menjalankan program:

```
├── gambar
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── hasil
│   ├── info.txt
│   └── ...
└── main.py
```

- Folder `gambar` berisi file-file gambar yang akan diproses.
- Folder `hasil` akan berisi hasil deteksi cabe dan file `info.txt` yang menyimpan informasi deteksi cabe.

### Lisensi

Program ini dilisensikan di bawah lisensi [MIT](LICENSE).

---

*Hak Cipta (c) 2023 Chaerul Candra Pranugrah*
