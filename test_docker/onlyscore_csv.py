import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv

# Parse command-line arguments
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--image_dir', type=str, help='input image directory')
parser.add_argument('--output_dir', type=str, help='output directory')
parser.add_argument('--mask_dir', type=str, default='', help='ground truth mask directory (optional)')
args = parser.parse_args()

image_dir = args.image_dir
output_dir = args.output_dir
mask_dir = args.mask_dir
csv_file = "scores_photoshop_scanned.csv"

# List all images in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith(('jpg', 'jpeg', 'png', 'bmp','JPG'))]
num_images = len(image_files)


# Initialize list to store file names and scores
file_scores = []

for idx, image_file in enumerate(image_files):
    image_path = os.path.join(image_dir, image_file)
    output_path = os.path.join(output_dir, f"{image_file}.npz")

    # Load result
    if not os.path.exists(output_path):
        print(f"Output file {output_path} not found, skipping.")
        continue

    result = np.load(output_path)
    # Store file name and score
    file_scores.append([image_file, result["score"]])


# Save file names and scores to CSV
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'Score'])
    writer.writerows(file_scores)

print(f"Scores saved to {csv_file}")
