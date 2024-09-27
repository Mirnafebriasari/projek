from PIL import Image, ImageEnhance

def process_image(image_path, output_path, level):
    # Membaca gambar
    image = Image.open(image_path)

    # Mengatur tingkat kecerahan
    if level == 'sangat gelap':
        factor = 0.2
    elif level == 'gelap':
        factor = 0.5
    elif level == 'normal':
        factor = 1.0
    elif level == 'cerah':
        factor = 1.5
    elif level == 'sangat cerah':
        factor = 2.0
    else:
        raise ValueError("Tingkat kecerahan tidak dikenali.")

    # Menerapkan kecerahan
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)

    # Menyimpan gambar yang sudah diproses
    brightened_image.save(output_path)
    print(f"Gambar telah disimpan di {output_path}")
