import numpy as np
import pandas as pd

data=pd.read_csv("student_data.csv")
#to print starting 5 lines
print("starting 5 lines\n")
print(data.head())
#to pirnt last 5 lines
print("\nlast 5 lines\n")
print(data.tail())
#describing the data
print("\ndata describing\n")
print(data.describe())
print("\nshape of data\n")
print(data.shape)
print("\nunique values of a every attribute in dataset\n")
print(data.nunique())
data.columns
print("\nunique figures in gender column\n")
print(data['gender'].nunique())
print("\nunique figures in race/ethnicity column\n")
print(data['race/ethnicity'].nunique())

#output
"""
starting 5 lines

   gender race/ethnicity parental level of education         lunch  \
0  female        group B           bachelor's degree      standard   
1  female        group C                some college      standard   
2  female        group B             master's degree      standard   
3    male        group A          associate's degree  free/reduced   
4    male        group C                some college      standard   

  test preparation course  math score  reading score  writing score  
0                    none          72             72             74  
1               completed          69             90             88  
2                    none          90             95             93  
3                    none          47             57             44  
4                    none          76             78             75  

last 5 lines

     gender race/ethnicity parental level of education         lunch  \
995  female        group E             master's degree      standard   
996    male        group C                 high school  free/reduced   
997  female        group C                 high school  free/reduced   
998  female        group D                some college      standard   
999  female        group D                some college  free/reduced   

    test preparation course  math score  reading score  writing score  
995               completed          88             99             95  
996                    none          62             55             55  
997               completed          59             71             65  
998               completed          68             78             77  
999                    none          77             86             86  

data describing

       math score  reading score  writing score
count  1000.00000    1000.000000    1000.000000
mean     66.08900      69.169000      68.054000
std      15.16308      14.600192      15.195657
min       0.00000      17.000000      10.000000
25%      57.00000      59.000000      57.750000
50%      66.00000      70.000000      69.000000
75%      77.00000      79.000000      79.000000
max     100.00000     100.000000     100.000000

shape of data

(1000, 8)

unique values of a every attribute in dataset

gender                          2
race/ethnicity                  5
parental level of education     6
lunch                           2
test preparation course         2
math score                     81
reading score                  72
writing score                  77
dtype: int64

unique figures in gender column

2

unique figures in race/ethnicity column

5
​
"""