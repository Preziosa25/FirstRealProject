import pandas as pd

df = pd.read_csv("data.csv")

df.head()

df.describe()

#Let's see waht the average value is for everyone
df["vlaue"].mean()