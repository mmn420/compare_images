import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Compare two images")
    parser.add_argument('image1_path', type=str, help='Path to the first image')
    parser.add_argument('image2_path', type=str, help='Path to the second image')
    parser.add_argument('tolerance', type=int, help='Tolerance for the comparison')
    args = parser.parse_args()

    if not os.path.exists(args.image1_path):
        raise FileNotFoundError(f"Image1 path does not exist: {args.image1_path}")
    if not os.path.exists(args.image2_path):
        raise FileNotFoundError(f"Image2 path does not exist: {args.image2_path}")
    if args.tolerance < 0:
        raise ValueError("Tolerance must be a positive integer")

    return args
