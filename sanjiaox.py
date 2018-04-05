def generate():
    """杨辉三角：
    1
    11
    121
    1331
    14641
    :type numRows: int
    :rtype: List[List[int]]
    """
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
n = 0
for t in generate():
    print(t)
    n += 1
    if n == 10:
        break
