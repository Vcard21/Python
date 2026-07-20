# 導入自定義模塊使用

# from modle_test1 import test
# test(1,2)

# 導入不同模塊的同名功能
# from modle_test1 import test
# from modle_test2 import test
# test(1,2)
# 當導入重複同名功能時，後者覆蓋前者


# __main__變量
# from modle_test1 import test_a
# 當導入的模塊本身有執行時，調用的本文件也會產生結果
# 簡單來說用main變量時可以決定是否是當前文件所執行，若不是則不輸出


# all變量，如果一個模塊文件中有__all__變量，當使用from xxx import * 導入時，只能導入__all__這個列表中的元素
# 主要就是 限制這個 * 的作用，有寫__all__就可以限制 * 到底要用哪些功能，不寫__all__就全部都可以用
from modle_test1 import *
test_a(1,2)
test_b(2,1)
"""
    1,如何自定義模塊並導入?
在python代碼文件中正常寫代碼即可，通過import,from關鍵字和導入python內置模塊一樣導入即可使用
    2,_main_變量的功能是?
if _main_ == " _main_"表示，只有當程序是直接執行的才會進入if內部，如果是被導入的則無法進入
    3,注意事項
不同模塊，同名的功能，如果都被導入，那麼後導入的會覆蓋先導入的
__all__變量可以控制import * 的時候那些功能可以被導入
"""