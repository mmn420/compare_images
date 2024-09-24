import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Compare two images")
    parser.add_argument('-golden_image', required=True, help='Path to the first image')
    parser.add_argument('-compare_image', required=True, help='Path to the second image')
    parser.add_argument('-tolerance', required=True, type=int, help='Tolerance for the comparison')
    args = parser.parse_args()

    if not os.path.exists(args.golden_image):
        raise FileNotFoundError(f"Image1 path does not exist: {args.golden_image}")
    if not os.path.exists(args.compare_image):
        raise FileNotFoundError(f"Image2 path does not exist: {args.compare_image}")
    if args.tolerance < 0:
        raise ValueError("Tolerance must be a positive integer")

    return args