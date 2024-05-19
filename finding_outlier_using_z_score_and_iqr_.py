# -*- coding: utf-8 -*-
"""finding outlier using z-score and iqr .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_cJ2WazBVKOTNDbsOZx-YBAU2JxTjBGm
"""

import random

data = [random.randint(0,20) for i in range (15)]

type(data)

print(data)

import numpy as np

average = np.mean(data)
SD = np.std(data)

print(average,SD)

outliers = [35,40,50]
type(outliers)

data = data + outliers

type(data)

average = np.mean(data)
SD = np.std(data)

print(average,SD)

Outliers = []
def detect_outliers(data):
  threshold = 3

  for i in data:
    z_score = (i - average)/SD
    if np.abs(z_score) > 3:
      outliers.append(z_score)
  return outliers

outlier_pt = detect_outliers(data)
print(outlier_pt)

"""<h1> interquartile range</h1>"""

print(data)

data = np.sort(data)

data

data.size

quartile1, quartile3 = np.percentile(data,[25,75])

print("quartile 1 : ", quartile1, "\n", "quartile 2 : ", quartile3)

## Find the IQR

iqr=quartile3-quartile1
print(iqr)

lower_bound_val = quartile1 -(1.5 * iqr)
upper_bound_val = quartile3 +(1.5 * iqr)

print("Lower_bound : ",lower_bound_val, "\n", "Upper_bound : ",upper_bound_val)

