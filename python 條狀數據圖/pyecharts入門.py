"""
pyecharts 入門
"""
# 1, 導入包
from pyecharts.charts import Line
# 2, 得到折線圖對象
line = Line()
# 3, 添加x軸數據
line.add_xaxis(["中國","美國","英國"])
# 4, 添加y軸數據
line.add_yaxis("GDP",[30,20,10])
# 5, 生成圖表
line.render()

# 設置全局配置項