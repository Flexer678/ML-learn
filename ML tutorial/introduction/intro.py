import numpy as np
import pandas as pd
import matplotlib as plt


cols = [
    "fLength",
    "fWidth",
    "fSize",
    "fConc",
    "fConc1",
    "fAsym",
    "fM3Long",
    "fM3Trans",
    "fAlpha",
    "fDist"
]

# gets the columns of the lists
df =pd.read_csv("./ML tutorial/introduction/magic04.data", names=cols)

#gets the first 5 things
df.head()

df['class'] = (df['class']== 'g').astype(int)




