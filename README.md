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


## Parameter explanation

- `__init__` : 
  - **data :** Data frame used for drawing bar chart
  - **error :** Data frame corresponding to error bars
  - **text :** Image text label
- `plot()`
  - **pic_px :** image size list , [width,height] , The unit is px
- `add_annotations()`
  - **annotation_list :** A two-dimensional list representing the position of the annotation, with each sublist representing an annotation. The length of 3 is the inter-group annotation, the length of 4 is the intra-group annotation, and the last value controls the y-axis position.

    `[0,1,1]` means that the annotation is between the 1/2th group, and the y-axis position drops 1 level relative to y_max; `[2,0,3,-1]` means that the annotation is within the 3rd group, and within the group In the 1/4th column, the y-axis position rises one level relative to y_max.
    > 表示注释在什么位置的二维列表，每一个子列表表示一个注释。长度为3的是组间注释，长度4为组内注释，最后一个值控制y轴位置。
    >
    > `[0,1,1]` 表示注释在第1/2个组之间，y轴位置相对于 y_max 下降1层；`[2,0,3,-1]` 表示注释在第3个组内，组内的第1/4个柱间，y轴位置相对于 y_max 上升一层。
  - **text :** annotation symbol, _default = "***"_ , which can also be 🪙🆙🏅⭐🔥🍋💔😃😭 ... symbols, visible https://www.emojiall.com/zh-hans/copy 
  - **size :**  symbol font size, _default = 16_
  - **line_width :** line width, _default = 1.5_
  - **color :** intergroup annotation color, _default = 'rgba(0,0,0,1)'_
  - **inne_color :**  annotation color within group, _default = "rgba(100,100,100,1)"_
  - **y_max_index :** The y-height of the annotation when layer is set to 0, _default = 1.15_ , multiply the height of the tallest bar in the chart by y_max_index to get y_max
  - **layer_down_index :** control the spacing between upper and lower layers, _default = 0.08_ , layer_down = layer_down_index $ \times $ y_max
  - **sign_d_index :** distance between line and symbol, _default = 4_ , layer_down / sign_d_index
  - **line_d_index :** the length of the hanging line, _default = 3.2_ , layer_down / line_d_index
- `show()`
  - **save_path :** path to save.
- `set_color()` : set the color of the column, given a list