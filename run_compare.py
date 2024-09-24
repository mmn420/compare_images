import sys
from parser import parse_args
from compare_images import compare_images
import os

if __name__ == '__main__':
    args = parse_args()
    
    diff_image1, diff_image2, overlay_image, report = compare_images(args.golden_image, args.compare_image, args.tolerance)
    if diff_image1 is None and diff_image2 is None and overlay_image is None:
        print(report)
        sys.stdout.flush()
        exit()
    
    golden_output_dir = os.path.join(os.path.dirname(args.compare_image), "golden_output")
    output_dir = os.path.join(os.path.dirname(args.compare_image), "output")

    if os.path.exists(golden_output_dir):
        output_dir = os.path.join(os.path.dirname(args.compare_image), "output")
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = golden_output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    base_name1 = os.path.basename(args.golden_image)
    base_name2 = os.path.basename(args.compare_image)
    
    # Save the result images with the base names included
    diff_image1.save(os.path.join(output_dir, f"diff_{base_name1}"))
    diff_image2.save(os.path.join(output_dir, f"diff_{base_name2}"))
    overlay_image.save(os.path.join(output_dir, f"overlay_{base_name1.replace('.png', '')}_{base_name2.replace('.png', '')}.png"))
    
    print(report)