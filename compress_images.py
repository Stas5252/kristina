import os
from PIL import Image

def compress_images(directory, max_size=(1600, 1600)):
    if not os.path.exists(directory):
        print(f"Directory {directory} not found")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    temp_path = filepath + ".tmp.jpg"
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(temp_path, "JPEG", quality=85, optimize=True)
                os.replace(temp_path, filepath)
                print(f"Compressed {directory}/{filename}: {width}x{height} -> {img.size[0]}x{img.size[1]}")
            except Exception as e:
                print(f"Error compressing {filename}: {e}")

if __name__ == "__main__":
    folders = [
        "беременность",
        "групповая",
        "женственность",
        "классика",
        "мужская",
        "семейные",
        "стрит",
        "творчество",
        "спортшик"
    ]
    for folder in folders:
        compress_images(folder)
