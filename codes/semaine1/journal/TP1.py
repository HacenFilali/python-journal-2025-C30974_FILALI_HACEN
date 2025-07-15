import pandas as pd # Importing Pandas
import matplotlib.pyplot as plt # Importing matplotlib for visualisation
df = pd.read_csv('../DATA/pokemon_data.csv')
df.iloc[2, 4] # Here we can see the information from second row and fourth␣ ↪colum
df.iloc[:5, :5] # Here is the information of first five rows with first five␣↪column