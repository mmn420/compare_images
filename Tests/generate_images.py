import os
import random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

def create_test_image(path, background_color, shape_color, size=(400, 400)):
    image = Image.new("RGB", size, background_color)
    draw = ImageDraw.Draw(image)
    
    # Generate random positions for shapes
    rect_pos = [random.randint(0, size[0] - 40), random.randint(0, size[1] - 40)]
    ellipse_pos = [random.randint(0, size[0] - 40), random.randint(0, size[1] - 40)]
    line_pos = [random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1])]
    polygon_pos = [random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1])]
    
    # Add shapes with the same color
    draw.rectangle([rect_pos[0], rect_pos[1], rect_pos[0] + 40, rect_pos[1] + 40], outline=shape_color, fill=shape_color, width=3)
    draw.ellipse([ellipse_pos[0], ellipse_pos[1], ellipse_pos[0] + 40, ellipse_pos[1] + 40], outline=shape_color, fill=shape_color, width=3)
    draw.line(line_pos, fill=shape_color, width=2)
    draw.polygon(polygon_pos, outline=shape_color, fill=shape_color, width=3)

    image.save(path)

def add_noise(image, noise_level=0.1):
    np_image = np.array(image)
    noise = np.random.normal(0, noise_level, np_image.shape)
    noisy_image = np.clip(np_image + noise * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)

def create_variant_image(golden_image_path, variant_path):
    image = Image.open(golden_image_path)
    
    image = add_noise(image, noise_level=random.uniform(0.01, 0.05))
    
    draw = ImageDraw.Draw(image)
    size = image.size
    shape_color = "#FFFFFF"
    rect_pos = [random.randint(0, size[0] - 40), random.randint(0, size[1] - 40)]
    ellipse_pos = [random.randint(0, size[0] - 40), random.randint(0, size[1] - 40)]
    line_pos = [random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1])]
    polygon_pos = [random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1]), random.randint(0, size[0]), random.randint(0, size[1])]
    
    draw.rectangle([rect_pos[0], rect_pos[1], rect_pos[0] + 40, rect_pos[1] + 40], outline=shape_color, fill=shape_color, width=3)
    draw.ellipse([ellipse_pos[0], ellipse_pos[1], ellipse_pos[0] + 40, ellipse_pos[1] + 40], outline=shape_color, fill=shape_color, width=3)
    draw.line(line_pos, fill=shape_color, width=2)
    draw.polygon(polygon_pos, outline=shape_color, fill=shape_color, width=3)
    
    image.save(variant_path)

def generate_golden_and_variants(base_folder, num_variants=30):
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
    
    background_color = "#FF00FF"
    shape_color = "#FFFFFF"
    
    # Generate the golden image
    golden_image_path = os.path.join(base_folder, "golden_image.png")
    create_test_image(golden_image_path, background_color, shape_color)
    
    # Create variant_0 identical to the golden image
    variant_0_folder = os.path.join(base_folder, "variant_0")
    if not os.path.exists(variant_0_folder):
        os.makedirs(variant_0_folder)
    variant_0_path = os.path.join(variant_0_folder, "variant_image.png")
    Image.open(golden_image_path).save(variant_0_path)
    
    # Generate other variants
    for i in range(1, num_variants):
        variant_folder = os.path.join(base_folder, f"variant_{i}")
        if not os.path.exists(variant_folder):
            os.makedirs(variant_folder)
        variant_path = os.path.join(variant_folder, f"variant_image.png")
        create_variant_image(golden_image_path, variant_path)

generate_golden_and_variants("golden_comparison_images")
print("Golden image and its variants created in the 'golden_comparison_images' folder")