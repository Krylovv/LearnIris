import pickle

with open('../model.pkl', 'rb') as f:
    clf = pickle.load(f)

print('Type in sepal length, sepal width, petal length, petal width in cm with comma separation:')
input_list = input()
input_list = input_list.split(',')
try:
    prediction_list = [float(ele) for ele in input_list]
except ValueError:
    print('Wrong input type')

#[6.7, 3.1, 5.6, 2.4]

value = clf.predict([prediction_list])
if value == [0]:
    print('It is setosa iris')
elif value == [1]:
    print('It is versicolor iris')
elif value == [2]:
    print('It is virginica iris')
else:
    print('Somethings wrong')