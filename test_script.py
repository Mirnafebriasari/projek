from motipy.image import process_image  # Pastikan ini sesuai dengan fungsi yang ada di image.py

image_path = input("Masukkan path gambar: ")
output_path = input("Masukkan path untuk menyimpan gambar output: ")
level = input("Masukkan tingkat kecerahan ('sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah'): ")

process_image(image_path, output_path, level)  # Memanggil fungsi yang benar
