from PIL import Image
import numpy as np

def generate_report(arr1, diff, tolerance_value):
    diff_pixels = np.sum(diff > tolerance_value)
    severity = (diff_pixels / diff.size) * 100
    average_difference = np.mean(diff[diff > tolerance_value])
    report = (
        f"Total differing pixels: {diff_pixels}\n"
        f"Severity of differences: {severity:.2f}%\n"
        f"Average difference value: {average_difference:.2f}"
    )
    return report

def compare_images(image1_path, image2_path, tolerance):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image1.size != image2.size or image1.mode != image2.mode:
        raise ValueError("Images must be of the same size and format")

    arr1 = np.array(image1)
    arr2 = np.array(image2)

    if np.array_equal(arr1, arr2):
            empty_diff1 = Image.new(image1.mode, image1.size)
            empty_diff2 = Image.new(image1.mode, image1.size)
            overlay_image = Image.blend(image1, image2, alpha=0.5)
            report = "The images are identical."
            return empty_diff1, empty_diff2, overlay_image, report

    max_pixel_value = 255
    tolerance_value = (tolerance / 100) * max_pixel_value
    diff = np.abs(arr1 - arr2)

    mask1 = np.where(arr1 > arr2 + tolerance_value, arr1, 0)
    mask1 = np.where(arr1 <= arr2 + tolerance_value, 0, mask1)
    mask2 = np.where(arr2 > arr1 + tolerance_value, arr2, 0)
    mask2 = np.where(arr2 <= arr1 + tolerance_value, 0, mask2)
    diff_image1 = Image.fromarray(mask1)
    diff_image2 = Image.fromarray(mask2)

    overlay_image = Image.blend(image1, image2, alpha=0.5)

    report = generate_report(arr1, diff, tolerance_value)
    return diff_image1, diff_image2, overlay_image, report