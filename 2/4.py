# 字符串拼接
print("hello"+"world")
# 字符串复制
print("hello"*3)
# 字符串长度
print(len("hello"))
# 字符串索引
print("hello"[0])#h 正向的下标
print("hello"[-1])#o 从末尾开始的第几个元素

# 字符串切片 包前不包后
print("hello"[0:3]) #hel
print("hello"[0:5]) #hello
print("hello"[0:-1]) #hell 排除了最后一个
print("hello"[0:-2]) #hel 排除了最后两个

# 字符串切片 步长
print("hello"[0:5:2]) #hlo 步长为2
print("hello"[0:5:1]) #hello 步长为1
print("hello"[0:5:3]) #hl 步长为3

