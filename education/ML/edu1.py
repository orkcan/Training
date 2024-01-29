# steps:
# 1. Load Data (usually csv)
# 2.Clean the Data  (such as removing duplicate data) data must be clean and in a good shape
# 3.Split into training and test sets 80% for training 20% for testing i.e.
# 4.Create a Model
# 5.choose the algorithm
# 6.scikit*learn learn is one of the most used
# 7. train the model
# 8. make the predictions. is it a cat or a dog?
# 9.evaluate and improve. measure accuracy
# 10.fine tune the model's parameters


#libraries: numpy :multidimensional array very popular
#pandas: data analysis lib. provides a concept called data frame(similar to excel rows and columns).
#matplotlib: for graphs and plots
#scikit-learn:provides all the common algorithm such as decision trees, neural networks and so on

#PANDAS FROM jupyter notebook:

import pandas as pd
df = pd.read_csv('vgsales.csv')
df
df.shape  #output is (16598, 11) lines and columns

df.describe() # output is  count(16598 for rank and 16327 for year i.e.),mean,std,min,25%,50%,75% and max  functions for the df

 df.values #output :
 array([[1, 'Wii Sports', 'Wii', ..., 3.77, 8.46, 82.74],
        [2, 'Super Mario Bros.', 'NES', ..., 6.81, 0.77, 40.24],
        [3, 'Mario Kart Wii', 'Wii', ..., 3.79, 3.31, 35.82],
        ...,
        [16598, 'SCORE International Baja 1000: The Official Game', 'PS2',
         ..., 0.0, 0.0, 0.01],
        [16599, 'Know How 2', 'DS', ..., 0.0, 0.0, 0.01],
        [16600, 'Spirits & Spells', 'GBA', ..., 0.0, 0.0, 0.01]],
       dtype=object)

music_data
    age	gender	genre
0	20	1	HipHop
1	23	1	HipHop
2	25	1	HipHop
3	26	1	Jazz
4	29	1	Jazz
5	30	1	Jazz
6	31	1	Classical
7	33	1	Classical
8	37	1	Classical
9	20	0	Dance
10	21	0	Dance
11	25	0	Dance
12	26	0	Acoustic
13	27	0	Acoustic
14	30	0	Acoustic
15	31	0	Classical
16	34	0	Classical
17	35	0	Classical




music_data.drop(columns=['genre'])  #dropped the genre
    age	gender
0	20	1
1	23	1
2	25	1
3	26	1
4	29	1
5	30	1
6	31	1
7	33	1
8	37	1
9	20	0
10	21	0
11	25	0
12	26	0
13	27	0
14	30	0
15	31	0
16	34	0
17	35	0


x = music_data.drop(columns=['genre'])
y = music_data['genre']
y

0        HipHop
1        HipHop
2        HipHop
3          Jazz
4          Jazz
5          Jazz
6     Classical
7     Classical
8     Classical
9         Dance
10        Dance
11        Dance
12     Acoustic
13     Acoustic
14     Acoustic
15    Classical
16    Classical
17    Classical
Name: genre, dtype: object



#let's use decision tree algorithm and make the program to predict what a 21yo m of 22yo fm would
#like to  listen based on the table we have.
#predict method uses 2 dimention array

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
music_data=pd.read_csv('music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)
predictions=model.predict([[21,1], [22,0]])
predictions
#output:
array(['HipHop', 'Dance'], dtype=object)

# let's call functions and split  train and test in our dataset. so far we had training inputs:
from sklearn.model_selection import train_test_split    (this function works as a tuple)
X_train, X_train, y_train, y_test = train_test_split(X,y,test_size=0.2)



import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data=pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test,predictions)
score
# score output is 1.0 >>>> means 100% ıt could have dıfferent resulsts function picks randomly
#increasing the test size to a greater value will give a less accuracy score since data is unsuffic.





import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals import joblib   #belongs to old sklearn
import joblib

music_data=pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'music-recommender.joblib')

# output is ['music-recommender.joblib']    DUMP METHOD BRINGS THE NAME OF THE FILE

# we don't want to train our model every time so:

model = joblib.load('music-recommender.joblib')
predictions = model.predict([[21,1]])
predictions

#output is array(['HipHop'], dtype=object)


exporting our model in visual format so we'll see how this model makes predictions:

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data=pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model,out_file='music-recommender.dot',
                    feature_names=['age','gender'],
                    class_names=sorted(y.unique()),   #unique for avoiding duplicates of class names
                    label='all',
                    rounded=True,
                    filled=True)

paste this code to VS CODE and download the visualizer dot extension