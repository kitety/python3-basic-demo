b = [1, 2, 3]
b.append(4)
print(b)

# 元组
a = (1, 2, 3)
print(a)

# 元组不可变
# a[0] = 100  # error

tu = (1, 2, 3, [1, 2, 4])
print(tu[3][2])
