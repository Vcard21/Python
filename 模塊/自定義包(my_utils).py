"""
演示疫潮
"""

import my_utils.str_util
from my_utils import file_utils

print(my_utils.str_util.str_reverse("黑馬程序員"))
print(my_utils.str_util.substr("itheima",0,4))

file_utils.append_to_file("F:/test_append.txt","itheima")
file_utils.print_file_info("F:/test_append.txt")
