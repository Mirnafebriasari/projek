from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    
    Args:
        image_path (str): Path ke file gambar input.
        output_path (str): Path untuk menyimpan gambar output.
        level (str): Tingkat kecerahan ('sangat gelap', 'gelap', 'normal', 'cerah', 'sangat cerah').
    """
    brightness_factors = {
        'sangat gelap': 0.2,
        'gelap': 0.5,
        'normal': 1.0,
        'cerah': 1.5,
        'sangat cerah': 2.0
    }
    
    factor = brightness_factors.get(level.lower(), 1.0)  # Default ke 'normal' jika level tidak valid

    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)
    brightened_image.save(output_path)
    print(f"Gambar berhasil disimpan di: {output_path}")
