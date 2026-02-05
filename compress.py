from PIL import Image
import os

def compress_image(input_path, output_path, target_kb=200, step=5, min_quality=10):
    img = Image.open(input_path)
    quality = 95
    while quality >= min_quality:
        img.save(output_path, optimize=True, quality=quality)
        size_kb = os.path.getsize(output_path) // 1024
        if size_kb <= target_kb:
            print(f"Compressed to {size_kb} KB with quality={quality}")
            return
        quality -= step
    print("Could not reach target size, final size:", size_kb, "KB")

compress_image("C:\\Users\\chakr\\Downloads\\DSC_0845-PL.jpg", "output.jpg", target_kb=200)
