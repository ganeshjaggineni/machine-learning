import pandas as pd
import numpy as np

data=pd.read_csv("auto-mpg.csv")
print(data.head())
print("\nlast 5 rows using tail\n")
print(data.tail())
print("\nshape of the dataset\n")
print(data.shape)
numeric_columns=data.select_dtypes(include=[np.number])
print("\nonly numeric values in dataset\n")
print(numeric_columns)
#finding central tendancy
mean_data=numeric_columns.mean()
print("\nmean\n")
print(mean_data)
median_data=numeric_columns.median()
print("\nmedian\n")
print(median_data)
std_dev_data=numeric_columns.std()
print("\nstandard deviation\n")
print(std_dev_data)
variance_data=numeric_columns.var()
print("\nvariance\n")
print(variance_data)

statistics_df=pd.DataFrame({
    'Mean':mean_data,
    'Median':median_data,
    'standard deviation':std_dev_data,
    'variance':variance_data
})
print("tabulate form of central tendancy of data")
print(statistics_df)

print("\ndescribing the data\n")
print(data.describe())

#OUTPUT
"""
  mpg  cylinders  displacement horsepower  weight  acceleration  model year  \
0  18.0          8         307.0        130    3504          12.0          70   
1  15.0          8         350.0        165    3693          11.5          70   
2  18.0          8         318.0        150    3436          11.0          70   
3  16.0          8         304.0        150    3433          12.0          70   
4  17.0          8         302.0        140    3449          10.5          70   

   origin                   car name  
0       1  chevrolet chevelle malibu  
1       1          buick skylark 320  
2       1         plymouth satellite  
3       1              amc rebel sst  
4       1                ford torino  

last 5 rows using tail

      mpg  cylinders  displacement horsepower  weight  acceleration  \
393  27.0          4         140.0         86    2790          15.6   
394  44.0          4          97.0         52    2130          24.6   
395  32.0          4         135.0         84    2295          11.6   
396  28.0          4         120.0         79    2625          18.6   
397  31.0          4         119.0         82    2720          19.4   

     model year  origin         car name  
393          82       1  ford mustang gl  
394          82       2        vw pickup  
395          82       1    dodge rampage  
396          82       1      ford ranger  
397          82       1       chevy s-10  

shape of the dataset

(398, 9)

only numeric values in dataset

      mpg  cylinders  displacement  weight  acceleration  model year  origin
0    18.0          8         307.0    3504          12.0          70       1
1    15.0          8         350.0    3693          11.5          70       1
2    18.0          8         318.0    3436          11.0          70       1
3    16.0          8         304.0    3433          12.0          70       1
4    17.0          8         302.0    3449          10.5          70       1
..    ...        ...           ...     ...           ...         ...     ...
393  27.0          4         140.0    2790          15.6          82       1
394  44.0          4          97.0    2130          24.6          82       2
395  32.0          4         135.0    2295          11.6          82       1
396  28.0          4         120.0    2625          18.6          82       1
397  31.0          4         119.0    2720          19.4          82       1

[398 rows x 7 columns]

mean

mpg               23.514573
cylinders          5.454774
displacement     193.425879
weight          2970.424623
acceleration      15.568090
model year        76.010050
origin             1.572864
dtype: float64

median

mpg               23.0
cylinders          4.0
displacement     148.5
weight          2803.5
acceleration      15.5
model year        76.0
origin             1.0
dtype: float64

standard deviation

mpg               7.815984
cylinders         1.701004
displacement    104.269838
weight          846.841774
acceleration      2.757689
model year        3.697627
origin            0.802055
dtype: float64

variance

mpg                 61.089611
cylinders            2.893415
displacement     10872.199152
weight          717140.990526
acceleration         7.604848
model year          13.672443
origin               0.643292
dtype: float64
tabulate form of central tendancy of data
                     Mean  Median  standard deviation       variance
mpg             23.514573    23.0            7.815984      61.089611
cylinders        5.454774     4.0            1.701004       2.893415
displacement   193.425879   148.5          104.269838   10872.199152
weight        2970.424623  2803.5          846.841774  717140.990526
acceleration    15.568090    15.5            2.757689       7.604848
model year      76.010050    76.0            3.697627      13.672443
origin           1.572864     1.0            0.802055       0.643292

describing the data

              mpg   cylinders  displacement       weight  acceleration  \
count  398.000000  398.000000    398.000000   398.000000    398.000000   
mean    23.514573    5.454774    193.425879  2970.424623     15.568090   
std      7.815984    1.701004    104.269838   846.841774      2.757689   
min      9.000000    3.000000     68.000000  1613.000000      8.000000   
25%     17.500000    4.000000    104.250000  2223.750000     13.825000   
50%     23.000000    4.000000    148.500000  2803.500000     15.500000   
75%     29.000000    8.000000    262.000000  3608.000000     17.175000   
max     46.600000    8.000000    455.000000  5140.000000     24.800000   

       model year      origin  
count  398.000000  398.000000  
mean    76.010050    1.572864  
std      3.697627    0.802055  
min     70.000000    1.000000  
25%     73.000000    1.000000  
50%     76.000000    1.000000  
75%     79.000000    2.000000  
max     82.000000    3.000000  

"""