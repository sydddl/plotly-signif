name = "plotly_signif"
help = ''' 
- `__init__` : 
  - **data :** Data frame used for drawing bar chart
  - **error :** Data frame corresponding to error bars, only used with `mode = "Bar"`
  - **text :** Image text label
  - **mode :** _default = "Bar"_ , and supports "Box" to plot
- `plot()`
  - **pic_px :** image size list , [width,height] , The unit is px
  - **Box_list :** If a box plot is drawn, the meaning of this list is `["which Group","which x","which y"] `
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
  `set_color()` need before use `plot()`
'''

from .plotly_signif import *