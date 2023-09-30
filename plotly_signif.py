import pandas as pd
import numpy as np
import plotly.graph_objects as go
from kaleido.scopes.plotly import PlotlyScope

class plotly_signif():
    def __init__(self,data=pd.DataFrame,error=pd.DataFrame,text={},json={}) -> None:
        self.fig = go.Figure()
        self.df = data
        self.error = error
        self.text = text
        self.Group_name = list(self.df.index)
        self.inne_num = self.df.shape[1] #一组几个柱
        self.width = 0.5 / self.inne_num  # 柱宽
        self.bargap = 0.25 # 表示类内间隔
        self.color = ["#5044f3",'#8ca0f7',"rgba(104, 135, 255,0.4)",'#4DECB9', "rgba(154, 225, 155,0.4)"]  #默认颜色

    def plot(self,pic_px=[500,550]):
        for i, column in enumerate(self.df.columns):
            self.fig.add_trace(go.Bar(
                x=self.df.index,
                y=self.df[column],
                name=column,
                marker_color=self.color[i % len(self.color)],  # 根据索引获取循环的颜色
                width=self.width,
                marker=dict(
                    line=dict(color='rgba(22, 24, 27, 0.7)', width=0)
                ),
                error_y=dict(
                    type='data',
                    array=self.error[column],
                    visible=True,
                    color='black',
                    width = 16/self.inne_num ,thickness=1.6
                    )
            ))
        self.fig.update_xaxes(title_text=self.text["x"], showline=True, linewidth=3, linecolor='black', tickangle=0,gridcolor='#EEEEEE',
                    title_font=dict(size=16, color='black'),ticks='outside',
                    tickfont=dict(size=18, color='black'))
        self.fig.update_yaxes(title_text=self.text["y"],showline=True, linewidth=3, linecolor='black', tickfont=dict(size=16),
                 title_standoff=10,tickmode='auto',showticklabels=True,ticks='outside',
                 title_font=dict(size=20, color='black'))
        self.fig.update_layout(
                plot_bgcolor='#ffffff',  # 设置背景色为白色
                hovermode='closest',
                dragmode='select',
                barmode='group',
                bargap=self.bargap,
                legend=dict(
                    orientation='h', 
                    x=0.1,
                    y=-0.1,
                    traceorder="normal",
                    font=dict(size=16,),
                    ),
                width=pic_px[0],height=pic_px[1], # 图 -> 宽/高
            )
        self.fig.update_traces(textfont_family="Raleway", selector=dict(type='bar'))

    def show(self,save_path=None,scale=400/96):
        self.fig.show()
        if save_path is None:
            pass
        else:
            scope = PlotlyScope()
            with open(save_path, "wb") as f:  
                f.write(scope.transform(self.fig, format="png",scale=scale))

    def add_annotations(self,annotation_list=list(),
                        text="***",size=16,color = 'rgba(0,0,0,1)',inne_color="rgba(100,100,100,1)",line_width=1.5,  # 传到annotation的
                        y_max_index = 1.15,layer_down_index = 0.08,sign_d_index = 4,line_d_index = 3.2,
                        ):
        '''
        annotation_list: 显著标识的位置, list | tuple,
            (最后一个数值表示y轴位置,0 最高, 最高位置由 y_max 设置, 增大1下落一个part_down的间隔,传进annotationq前会删去) 
            如[0,1,0]表示要画的两个组的x轴次序,[1,0,1,1]表示要画在第2个组内的1、2两个bar间。
        text: 标识符号，也可以为 🪙🆙🏅⭐🔥🍋💔😃😭 等符号。可见 https://www.emojiall.com/zh-hans/copy
        size: 标识符号字体大小
        color: 线框颜色; width:线宽度 ; 
        d : 线和标识符号的距离 ; line_d : 线下沿的长度
        layer_down : 上下间距, y_max : 最上层y轴位置
        '''
        bar_max = self.fig.data[0]["y"].max()
        y_max = bar_max * y_max_index
        layer_down = y_max * layer_down_index
        d = layer_down / sign_d_index
        line_d = layer_down / line_d_index
        for i in annotation_list:
            y_layer = i[-1]
            y = y_max - layer_down * y_layer
            self.annotation(anno_at = i[:-1],y_max = y,text=text,size=size,color =color,inne_color=inne_color,line_width=line_width,d = d,line_d = line_d)        

    def annotation(self,anno_at,inne=False,**kwargs):
        '''
        inne: 是否为组内标识,bool
        '''
        assert isinstance(anno_at, list or tuple), "标识指示为空或格式错误, list | tuple"
        d = kwargs["d"]
        line_d = kwargs["line_d"]
        y_max = kwargs["y_max"]
        if len(anno_at) == 3:
            inne = True
        if inne is True:
            line_d = line_d * 0.7
            group_at = anno_at[0]
            mean = int(self.inne_num / 2)
            between = self.width*(1 + self.bargap*2)
            if self.inne_num % 2 == 0:
                diff1 = (anno_at[1] - mean + 0.5) * between
                diff2 = (anno_at[2] - mean + 0.5) * between
            else:
                diff1 = (anno_at[1] - mean) * between
                diff2 = (anno_at[2] - mean) * between
            self.fig.add_annotation(text=kwargs["text"],name="p-value",xref="x", yref="y",
                x=group_at + (diff1+diff2)/2 , y=y_max + d, showarrow=False,font=dict(size=kwargs["size"], color=kwargs["inne_color"]),)
            self.fig.add_shape(type="line",x0=group_at + diff1,y0=y_max, x1=group_at + diff2, y1=y_max,
                               line=dict(color=kwargs["inne_color"],width=kwargs["line_width"]))
            self.fig.add_shape(type="line",x0=group_at + diff1,y0=y_max-line_d, x1=group_at + diff1, y1=y_max,
                               line=dict(color=kwargs["inne_color"],width=kwargs["line_width"]))
            self.fig.add_shape(type="line",x0=group_at + diff2,y0=y_max-line_d, x1=group_at + diff2, y1=y_max,
                               line=dict(color=kwargs["inne_color"],width=kwargs["line_width"]))

        else:
            x_local = np.array(anno_at).mean()
            self.fig.add_annotation(text=kwargs["text"],name="p-value",xref="x", yref="y",
                        x=x_local, y=y_max+d, showarrow=False,font=dict(size=kwargs["size"], color="black"),)
            self.fig.add_shape(type="line",x0=self.Group_name[anno_at[0]],y0=y_max, x1=self.Group_name[anno_at[1]], y1=y_max,
                               line=dict(color=kwargs["color"],width=kwargs["line_width"]))
            self.fig.add_shape(type="line",x0=self.Group_name[anno_at[0]],y0=y_max-line_d, x1=self.Group_name[anno_at[0]], y1=y_max,
                               line=dict(color=kwargs["color"],width=kwargs["line_width"]))
            self.fig.add_shape(type="line",x0=self.Group_name[anno_at[1]],y0=y_max-line_d, x1=self.Group_name[anno_at[1]], y1=y_max,
                               line=dict(color=kwargs["color"],width=kwargs["line_width"]))

    def set_color(self,color):
        self.color = color