"""
python 包就是一個文件夾，內含__init__.py文件，該文件夾可用於包含多個模塊文件
本質上依然是模塊。
注意，有init文件才算是包

"""

# 創建一個包
# 導入自定義的包中的模塊，並使用
# import my_package.my_module
# import my_package.my_module2
#
# my_package.my_module.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module
# from my_package import my_module2
# my_module.info_print1()
# my_module2.info_print2()
#
# from my_package.my_module import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()


# 通過__all__變量，控制import *
# init文件內空白，就是拿來寫__all__變量的
# 注意，all變量只能控制 * 號
from my_package import *
my_module.info_print1()
my_module2.info_print2()

"""
總結：
    1,python包是文件夾
裡面存放許多python的模塊，通過包在邏輯上將一批模塊歸為一類，方便使用
    2,__init__.py文件作用
創建包會默認自動創建的文件，通過這個文件來表示一個文件夾是否為包，而非普通文件夾
    3,__all__變量的作用
同模塊中學習到的是一個作用，控制import * 能夠導入的內容。
"""


""""
在python程序的生態中，有許多非常多的第三方包(非python官方)，可以極大的幫助我們提高開發效率，如：
    科學計算常用的：numpy包
    數據分析常用的：padndas包
    大數據分析常用的：pyspark,apache-flink包
    圖形可視化常用的：matplotlib,pyecharts
    人工智能常用的：tensorflow
    等
如何安裝第三方包?
只需使用python內置的pip程序即可
1,打開命令提示字元
2,輸入pip install 包名稱
即可快速安裝第三方包

總結：
1,第三方包是什麼以及作用
第三方包就是非python官方內置的包，可以安裝它們擴展功能，提高開發效率
2,如何安裝?
    在命令提示字元內輸入
    pip install [包名稱]
    pip insyall -i [網址]
    
    或
    
    pycharm中點擊版本，解釋器設置即可簡易安裝
"""