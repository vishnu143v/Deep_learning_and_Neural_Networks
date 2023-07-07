import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


X = np.asarray([20,5,10,13,12])
y = np.asarray([44,22,25,32,27])

# Create pandas dataframe to store our X and y values
df = pd.DataFrame(
    {'X': X,
     'y': y}
)
rows = df.shape[0]
cols = df.shape[1]

print("Total Rows: " + str(rows))
print("Total Columns: " + str(cols))

x_mean = np.mean(X)
y_mean = np.mean(y)

xy=np.sum(X*y)
xymean=np.mean(X*y)
x2s=X**2
x2smean=np.mean(x2s)
xmean2s=x_mean**2
beta=(xymean-x_mean*y_mean)/(x2smean-xmean2s)
alpha=y_mean-(beta*x_mean)
print(f'Intercept = {alpha}')
print(f'slope = {beta}')
