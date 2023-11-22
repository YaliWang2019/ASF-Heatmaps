import os
import asf_search as asf
import pandas as pd
import numpy as np


opts = { 'platform': asf.SENTINEL1, 'processingLevel': asf.SLC}

result = asf.search(**opts)

with open("SLC_Data.csv", "w") as f:
	f.writelines(result.csv())