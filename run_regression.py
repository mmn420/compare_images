import datetime
import os
import subprocess
from PIL import Image
import numpy as np
from tabulate import tabulate

def golden_compare(output_dir, golden_output_dir):
    output_images = os.listdir(output_dir)
    for image_name in output_images:
        output_image_path = os.path.join(output_dir, image_name)
        golden_image_path = os.path.join(golden_output_dir, image_name)
        
        if not os.path.exists(output_image_path):
            print(f"Output image not found: {output_image_path}")
            return f"Output image not found: {output_image_path}"
        if not os.path.exists(golden_image_path):
            print(f"Golden image not found: {golden_image_path}")
            return f"Golden image not found: {golden_image_path}"
        
        image1 = Image.open(output_image_path)
        image2 = Image.open(golden_image_path)
        arr1 = np.array(image1)
        arr2 = np.array(image2)
        if image1.size != image2.size or image1.mode != image2.mode or not np.array_equal(arr1, arr2):
            return f"Images do not match: {output_image_path}, {golden_image_path}"
    return "All images match. PASSED"

def get_image_pairs(base_folder):
    # List all directories in the base folder
    directories = [d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))]
    golden_image = os.path.join(base_folder, "golden_image.png")
    
    images = []
    for directory in directories:
        # Get the variant images
        variants = [f for f in os.listdir(os.path.join(base_folder, directory)) if f.startswith("variant_")]
        for variant in variants:
            variant_image = os.path.join(base_folder, directory, "variant_image.png")
            images.append((golden_image, variant_image, directory))
    
    return images

def test_script(generate_golden=False):
    base_folder = ".\\Tests\\golden_comparison_images"
    image_pairs = get_image_pairs(base_folder)
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    
    results = []
    for image1_path, image2_path, variant_folder in image_pairs:
        process = subprocess.Popen([
            "C:/Users/z004zy1n/Desktop/RVE_QA_Tasks/Compare_Images/.venv/Scripts/python.exe",
            "run_compare.py",
            "-golden_image", image1_path,
            "-compare_image", image2_path,
            "-tolerance", "10"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        process.wait()
        process.kill()
        if generate_golden:
            continue
        else:
            print(f"Comparing images in folder: {variant_folder}")
            output_dir = os.path.join(base_folder, variant_folder, "output")
            golden_output_dir = os.path.join(base_folder, variant_folder, "golden_output")
            results.append((golden_compare(output_dir, golden_output_dir), variant_folder))
    if generate_golden:
        print("Golden images generated. Exiting.")
    else:
        headers = ["Regression Result","Variant Folder"]
        table = tabulate(results, headers, tablefmt="grid")
        with open(f"comparison_results_{current_date}.txt", "w") as f:
            f.write(table)
        print(f"Comparison results saved to 'comparison_results_{current_date}.txt'")
        print(table)

test_script(generate_golden=False)