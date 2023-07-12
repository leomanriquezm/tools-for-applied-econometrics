import itertools
import pandas as pd

#some dataframe
df = pd.DataFrame({'X1': [1, 2, 3],
                   'X2': [4, 5,6],
                   'X3': [7, 8, 9]})

#dataset variable names
variables = list(df.columns)

#generates all possible combinations of the variables
combinations = []
for r in range(1, len(variables) + 1):
    combinations.extend(list(itertools.combinations(variables, r)))
