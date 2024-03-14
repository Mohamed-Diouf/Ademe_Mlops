import pandas as pd
import numpy as np

url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=10000&format=csv&after=10000%2C965634&header=true"

data = pd.read_csv(url)
print(data.shape)

assert(len(data))>0

print(data.head())

