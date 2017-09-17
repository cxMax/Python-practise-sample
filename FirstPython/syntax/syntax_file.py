# coding=utf-8

# raw_input('请输入一个数字 : ')
# input('请输入 : ')

# write file
txt = open('/home/caixi/rx', 'wb')
txt.write('卢本伟牛逼')
txt.close()


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


# read file
try:
    txt = open('/home/caixi/rx', 'r')
    print txt.read(20)
except Networkerror:
    print 'IO exception'
finally:
    txt.close()
