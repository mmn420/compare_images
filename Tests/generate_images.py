from PIL import Image, ImageDraw

def create_complex_test_image(path, base_color, size=(200, 200), diff=False):
    image = Image.new("RGB", size, base_color)
    draw = ImageDraw.Draw(image)
    
    # Add base details to both images
    draw.rectangle([20, 20, 60, 60], outline="white", width=3)
    draw.ellipse([80, 80, 120, 120], outline="white", width=3)
    draw.line([0, 0, size[0], size[1]], fill="white", width=2)
    draw.polygon([100, 150, 130, 180, 70, 180], outline="white", width=3)
    
    if diff:
        # Add multiple differences
        draw.rectangle([50, 50, 100, 100], fill="blue")
        draw.ellipse([120, 30, 170, 80], fill="green")
        draw.line([10, 190, 190, 10], fill="yellow", width=5)
        draw.polygon([150, 150, 180, 180, 120, 180], fill="purple")
        draw.text((10, 10), "Different", fill="red")
    
    image.save(path)

# Create two images
create_complex_test_image("complex_image1.png", "blue")
create_complex_test_image("complex_image2.png", "red", diff=True)

print("Complex test images created: complex_image1.png and complex_image2.png")