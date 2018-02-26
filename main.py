# -- coding: utf-8 --
import sys
def divide(a,b):
  if b == 0:
    print("除数不能为0")
    sys.exit(1)
  return a*1.0/b

if __name__ == "__main__":
  a = int(input(u"输入被除数: "))
  b = int(input(u"输入除数: "))
  print(divide(a,b))
