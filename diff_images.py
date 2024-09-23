from PIL import Image, ImageChops
import numpy as np

def compare_images(image1_path, image2_path, tolerance):
    # Load images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image1.size != image2.size or image1.mode != image2.mode:
        raise ValueError("Images must be of the same size and format")

    arr1 = np.array(image1)
    arr2 = np.array(image2)
    diff = np.abs(arr1 - arr2)

    mask1 = np.where(diff > tolerance, arr1, 0)
    mask2 = np.where(diff > tolerance, arr2, 0)
    combined_mask = np.where(diff > tolerance, (arr1 + arr2) // 2, 0)
    diff_image1 = Image.fromarray(mask1)
    diff_image2 = Image.fromarray(mask2)
    combined_diff_image = Image.fromarray(combined_mask)


    total_pixels = arr1.size
    diff_pixels = np.count_nonzero(diff > tolerance)
    severity = (diff_pixels / total_pixels) * 100
    average_difference = np.mean(diff[diff > tolerance])

    report = (
        f"Total differing pixels: {diff_pixels}\n"
        f"Severity of differences: {severity:.2f}%\n"
        f"Average difference value: {average_difference:.2f}"
    )

    return diff_image1, diff_image2, combined_diff_image, report
