# !/usr/bin/env python3
# encoding=UTF-8

"""
    基本的初等数学类
    最大公约数、公倍数、素因子分解、闰年判断、找零钱、斐波那列数列
"""

__author__ = 'linna'


# 闰年判断
def isLeapYear(year):
    return (not (year % 4 and year % 100)) or (not year % 400)

#找零钱
def mod(money):
    loop = True
    tmp = ['总金额：'+str(money)+'元']

    # 面值列表 单位：元
    cate = (100, 50, 20, 10, 5, 1, 0.5, 0.1)

    sy = int(money*10)
    while loop:
        if sy == 0:
            loop=False
        else:
            for row in cate:
                tmpStr = ''
                jine = int(row*10)
                if jine >= 10:
                    tmpUn = '元'
                else:
                    tmpUn = '角'

                if sy >= jine and tmpStr == '':
                    m = sy//jine
                    sy = sy%jine
                    if jine >= 10:
                        tmpStr = str(jine//10)+tmpUn+str(m)+'张'
                    else:
                        tmpStr = str(jine)+tmpUn+str(m)+'张'
                    tmp.append(tmpStr)
    return tmp


# 最大公约数， 辗转相除法
def maxcommondivisor(m, n):
    while True:
        remainder = m % n
        if not remainder:
            return n
        else:
            m, n = n, remainder


#最小公倍数
def maxCommonMultipe(m, n):
    return m * n // maxcommondivisor(m, n)

#素数的判断
def isprime(number):

    result = True
    for i in range(number//2, 1, -1):
        if number % i == 0:
            result = False
            break
    return result

# 获取n的所有因子
def getfactors(n):
    result = [n]
    for i in range(n/2, 0, -1):
        if n % i == 0:
            result.append(i)
    return result

# 素因子分解
def decompose(n):
    all_factors = getfactors(n)
    all_factors.remove(1)
    all_factors.remove(n)
    prime_factors = [x for x in all_factors if isprime(x)]

    prime_factors.sort(reverse=True)
    print(prime_factors)
    result = []
    remainder = n
    for f in prime_factors:
        while remainder >= f:
            qut, rem = divmod(remainder, f)
            #print(f, qut, rem)
            if rem != 0:
                break
            else:
                remainder = qut
                result.append(f)
    return result

# 获取前N个斐波那契数列 一生成器
def fibonacci(n):
    a = b = 1
    for i in range(2, n):
        yield a
        a, b = b, b + a

# 获取前N个斐波那契数列 二列表存储
def fibonacci_2(n):
    result = []
    if n == 1:
        result.append(n)
    elif n >= 2:
        result.append(1)
        result.append(2)
        for i in range(2, n):
            result.append(result[-1] + result[-2])
    return result


def main():
    # print(isLeapYear(1808))

    # a=mod(88.7)
    # print(a)

    print(maxcommondivisor(48, 72))
    print(maxCommonMultipe(21, 72))
    print(isprime(13))

    print(getfactors(28)) #[28, 14, 7, 4, 2, 1]
    print(decompose(28))  #[7, 2, 2]

    #for i in fibonacci(20):
    #    print(i)

    print(fibonacci_2(15))


if __name__ == '__main__':
    main()
