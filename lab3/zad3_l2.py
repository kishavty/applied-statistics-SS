import pandas as pd 

test = pd.read_csv("CreditCard".csv")
print()

print(test.columns)
test.value_counts()