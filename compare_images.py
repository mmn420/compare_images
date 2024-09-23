from parser import parse_args
from diff_images import compare_images

if __name__ == '__main__':
    args = parse_args()
    
    diff_image1, diff_image2, combined_diff_image, report = compare_images(args.image1_path, args.image2_path, args.tolerance)


diff_image1.save("diff_image1.png")
diff_image2.save("diff_image2.png")
combined_diff_image.save("combined_diff_image.png")
print(report)