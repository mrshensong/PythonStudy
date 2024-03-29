import random
import string

# 产生 1 到 10 的一个整数型随机数
print( random.randint(1,10) )
# 产生 0 到 1 之间的随机浮点数
print( random.random() )
# 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.uniform(1.1,5.4) )
# 从序列中随机选取一个元素
print( random.choice('tomorrow') )
# 生成从1到100的间隔为2的随机整数
print( random.randrange(1,100,2) )
# 多个字符中生成指定数量的随机字符：
print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
# 多个字符中选取指定数量的字符组成新字符串：
print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 将序列a中的元素顺序打乱
a=[1,3,5,6,7]
random.shuffle(a)
print(a)