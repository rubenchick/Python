# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).

import pandas as pd

df = pd.DataFrame ([['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
                    ['Albania', 'Europe', 28748, 2831741, 12960000000],
                    ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
                    ['Andorra', 'Europe', 468, 78115, 3712000000],
                    ['Angola', 'Africa', 1246700, 20609294, 100990000000]])
df.columns = ['name', 'continent', 'area', 'population', 'gdp']

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Var 1 runtime 15% memory 43%
    # return world[((world['population'] >= 25000000) | (world['area'] >= 3000000))][['name', 'population', 'area']]
    # Var 2 runtime 23% memory 97%
    return world.loc[(world.loc[:, 'population'] >= 25000000) | (world.loc[:, 'area'] >= 3000000)][['name', 'population', 'area']]

print(big_countries(df))

