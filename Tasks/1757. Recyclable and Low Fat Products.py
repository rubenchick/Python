import pandas as pd
from enum import Enum

df = pd.DataFrame ([[0, "Y", "N"],
                    [1, "Y", "Y"],
                    [2, "N", "Y"],
                    [3, "Y", "Y"],
                    [4, "N", "N"]])
df.columns = ['product_id', 'low_fats', 'recyclable']

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products.loc[:, 'low_fats'] == "Y") & (products.loc[:, 'recyclable'] == "Y")][['product_id']]

print (find_products(df))
