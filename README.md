# plotly-signif
 A python example of drawing a box plot based on the plotly package, with freely definable statistical annotations


## How to use

```py
from plotly_signif import *
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df1 = iris.groupby("species").mean()
df2 = iris.groupby("species").sem()
```

```py
test = plotly_signif(data=df1,error=df2,text={"x":"","y":""})  
test.plot()
# Add statistical annotation
annotation_list = [[0,1,1],[2,0,3,-1],[2,1,2,2],[0,1,3,6],[0,2,3,10]]
test.add_annotations(annotation_list = annotation_list,text="***")   
test.add_annotations(annotation_list = [[1,2,3,4]],text="🏅",sign_d_index=2) 
test.add_annotations(annotation_list = [[1,1,2,5]],text="😭",sign_d_index=2) 
test.add_annotations(annotation_list = [[1,0,2,2]],text="⭐⭐⭐",sign_d_index=2,size=12) 
test.add_annotations(annotation_list = [[1,2,0]],text="ns",size=14,sign_d_index=2) 
# draw/save
test.show(save_path="./image/example.png")  # Save usage properties save_path = "./image/example.png" 
```

![](./image/example.png)