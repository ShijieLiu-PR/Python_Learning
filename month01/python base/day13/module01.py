__all__ = ["fun01", "MyClass01", "fun04"]
__doc__ = "this module is made by shijie."
print("i am module01")
print(__name__)
for i in range(10):
    print(i, end="")
    if (i+1) % 10 == 0:
        print("")
def fun01():
    print("fun01")


class MyClass01:
    def fun02(self):
        print("fun02")

def fun04():
    print("fun04")