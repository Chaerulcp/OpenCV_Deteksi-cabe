import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
import os
import time

# Fungsi untuk menyimpan gambar dengan kotak posisi cabe yang ditandai
def save_result(file_path, img, contours):
    count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1750:
            count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 8)


    # menampilkan hasil deteksi pada UI
    cv2.namedWindow('Deteksi Cabe', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Deteksi Cabe', 500, 400)
    cv2.imshow('Deteksi Cabe', img)
    cv2.waitKey(1000)  # Menunggu 1 detik sebelum melanjutkan
    cv2.destroyAllWindows()

    # Simpan gambar hasil deteksi cabe
    result_path = f"hasil/{os.path.basename(file_path)}"
    cv2.imwrite(result_path, img)
    return count

# Fungsi untuk menyimpan informasi deteksi cabe ke file txt
def save_info(file_name, count):
    info = f"Nama Gambar: {file_name}\n"
    info += f"Jumlah Cabe: {count}\n\n"

    with open("hasil/info.txt", "a") as file:
        file.write(info)

# Fungsi untuk membuka file gambar
def open_image():
    # Mendapatkan daftar file gambar dalam folder "gambar"
    folder_path = "gambar"
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Memproses setiap file gambar
    for image_file in image_files:
        # membaca file gambar
        file_path = os.path.join(folder_path, image_file)
        img = cv2.imread(file_path)

        # konversi warna RGB ke HSV
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # menampilkan gambar hasil konversi warna RGB ke HSV
        cv2.namedWindow('Konversi HSV', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Konversi HSV', 500, 400)
        cv2.imshow('Konversi HSV', hsv_img)
        cv2.waitKey(1000)  # Menunggu 1 detik sebelum melanjutkan
        cv2.destroyAllWindows()

        # definisi range warna untuk deteksi cabe
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])

        # segmentasi warna untuk deteksi cabe
        mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)

        # menampilkan gambar hasil segmentasi
        cv2.namedWindow('Segmentasi Warna', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Segmentasi Warna', 500, 400)
        cv2.imshow('Segmentasi Warna', mask_red)
        cv2.waitKey(1000)  # Menunggu 1 detik sebelum melanjutkan
        cv2.destroyAllWindows()

        # morfologi untuk menghilangkan noise
        kernel = np.ones((5, 5), np.uint8)
        mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)

        # deteksi kontur untuk mengambil area cabe
        contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # menghitung jumlah cabe dan menampilkan kotak posisi cabe pada gambar
        count = save_result(file_path, img.copy(), contours)

        # menyimpan informasi deteksi cabe ke file txt
        save_info(image_file, count)

   

        # menampilkan jumlah cabe pada console
        print('Jumlah cabe: ' + str(count))

# membuat UI dengan label "Upload Image"
root = tk.Tk()
root.title("Program Deteksi Cabe")
canvas = tk.Canvas(root, width=300, height=10)
canvas.pack()

# Fungsi untuk menjalankan proses saat tombol "Upload Image" ditekan
def process_images():
    open_image()
    button.configure(state='disabled')  # Menonaktifkan tombol setelah proses selesai

# membuat tombol "Upload Image" untuk memilih file gambar
button = tk.Button(root, text="Start", command=process_images)
button.pack()

# style butttn
button.configure(width=20, activebackground="#33B5E5", relief=tk.FLAT, fg='white', bg='#33B5E5', font=('helvetica', 12, 'bold'))



# menjalankan UI
root.mainloop()
