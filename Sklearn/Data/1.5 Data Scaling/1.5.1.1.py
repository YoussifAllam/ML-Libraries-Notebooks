#Import Libraries
from sklearn.preprocessing import StandardScaler
#----------------------------------------------------

#Standard Scaler for Data
X = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
y = scaler.fit_transform(X)

#showing data
print('X \n' , X[:10])
print('y \n' , y[:10])