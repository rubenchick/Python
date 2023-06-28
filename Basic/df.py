import pandas as pd

df = pd.DataFrame([[1,10],[2,20],[3,30]])
df.columns = ['home','zoo']

# df['Foot'] = df.apply(lambda row: row.home*10, axis = 1)
# df.info()
# df.describe()
#
#
# print(df)
from sklearn import datasets
import pandas as pd
iris_data = datasets.load_iris()
df_iris = pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
df_iris['target'] = pd.Series(iris_data.target)
df_iris.head()
print(df_iris)


#
# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)
#
# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x
#
# train_x = x[:80]
# train_y = y[:80]
#
# test_x = x[80:]
# test_y = y[80:]
#
# mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
#
# myline = numpy.linspace(0, 6, 100)
#
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()