import pandas as pd

df = pd.DataFrame([[1, 100],
                   [2, 100],
                   [3, 300]])
df.columns = ['id', 'salary']
n = 3

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    columnName = "getNthHighestSalary(" + str (n) + ")"
    employee = (
        employee['salary']
        .sort_values(ascending=False)
        .drop_duplicates()
        .reset_index()
    )
    if len(employee) < n:
        return pd.DataFrame(["null"], columns=[[columnName]])[columnName]
    else:
        return pd.DataFrame([employee.loc[[n-1], "salary"][n-1]], columns=[[columnName]])[columnName]

#
print(nth_highest_salary(df,n))
