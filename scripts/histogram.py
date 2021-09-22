#!/usr/bin/python3
import sys
import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('rna/expression_results.csv', quoting=2)
data.hist(bins=10)
plt.show()
plt.savefig('image.png')
