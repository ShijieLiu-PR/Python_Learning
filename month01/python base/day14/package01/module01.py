"""
    module01
"""


def fun01():
    print("module01 - fun01")


# 调用module02

import package01.package02.module02 as ppm2
ppm2.fun02()