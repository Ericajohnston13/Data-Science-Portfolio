#!/usr/bin/env python
# coding: utf-8

# # Import Packages

import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats


# # Import Data

hybrid2013= pd.read_csv('C:/Users/baby_/python_course/hybrid2013.csv')

hybrid2013.head()


# # Determine whether a miles per gallon (mpg) rating of 40 is unusual for a hybrid car on the market in 2013

# # Create a Histogram

hybrid2013['mpg'].hist()


# # Run a single sample ttest

stats.ttest_1samp(hybrid2013['mpg'], 40)


# # Figure out the mean

hybrid2013.mpg.mean()

