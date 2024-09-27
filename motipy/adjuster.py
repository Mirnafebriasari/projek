from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    
    Args:
        image_path (str): Path ke file gambar input.
        output_path (str): Path untuk menyimpan gambar output.
        level (str): Tingkat kecerahan ('sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah').
    """
    # Faktor kecerahan berdasarkan level yang ditentukan
    brightness_factors = {
        'sangat gelap': 0.2,
        'gelap': 0.5,
        'normal': 1.0,
        'cerah': 1.5,
        'sangat cerah': 2.0
    }
    
    # Mendapatkan faktor kecerahan dari level yang diberikan
    factor = brightness_factors.get(level.lower(), 1.0)  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    # Membaca gambar
    image = Image.open(image_path)
    
    # Menerapkan kecerahan
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)

    # Menyimpan gambar yang sudah diproses
    brightened_image.save(output_path)
    print(f"Gambar telah disimpan di: {output_path}")

# Contoh penggunaan
if __name__ == "__main__":
    image_path = input("Masukkan path gambar (contoh: C:\\Users\\Asus\\Documents\\jj.jpg): ")
    output_path = input("Masukkan path untuk menyimpan gambar output (contoh: C:\\Users\\Asus\\Documents\\brightened_image.jpg): ")
    level = input("Masukkan tingkat kecerahan ('sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah'): ")
    
    adjust_brightness(image_path, output_path, level)
