list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]

# 1. import module
# import double_list_helper
# re02 = double_list_helper.DoubleListHelper.get_elements(list01,double_list_helper.Vector(2,0), double_list_helper.Vector(0,1),3)
# print(re02)

# 2. import module as variable
# import double_list_helper as dlh
# re02 = dlh.DoubleListHelper.get_elements(list01, dlh.Vector(2,0), dlh.Vector(0,1), 3)
# print(re02)


# 3. from module import variable
# from double_list_helper import DoubleListHelper, Vector
# re02 = DoubleListHelper.get_elements(list01, Vector(2, 0), Vector(0, 1), 3)
# print(re02)

# 4. from module import variable as name
# from double_list_helper import DoubleListHelper as helper, Vector as vec
# from double_list_helper import DoubleListHelper as helper
# from double_list_helper import Vector as vec
# re02 = helper.get_elements(list01,vec(2,0),vec(0,1),3)
# print(re02)

# 5. from module import *
from double_list_helper import *
re02 = DoubleListHelper.get_elements(list01,Vector(2,0), Vector(0,1),3)
print(re02)
