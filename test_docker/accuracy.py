
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv

csv_file="scores_bonafides.csv"

def count_high_scores(csv_file, threshold=0.95):
    total=0
    morph = 0
    bonafide=0
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            total+=1
            if float(row['Score']) > threshold:
                morph += 1
            else:
                bonafide+=1
    print(f'Bonafide: {bonafide}')
    print(f'Morph:    {morph}')
    print(f'Total:   {total}')
    print(f'Morphs Percentage: ',(morph/total)*100)
    print(f'Bonafide Percentage: ',(bonafide/total)*100)

# Count and print the number of scores greater than 0.95
count_high_scores(csv_file)

