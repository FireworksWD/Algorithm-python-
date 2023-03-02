'''在一个3×3的网格中，1~8这8个数字和一个“x”恰好不重不漏地分布在这3×3的网格中
1 2 3
x 4 6
7 5 8
在游戏过程中，可以把“x”与其上、下、左、右四个方向之一的数字交换（如果存在）。
我们的目的是通过交换，使得网格变为如下排列（称为正确排列）:
1 2 3
4 5 6
7 8 x
例如，示例中图形就可以通过让“x”先后与右、下、右三个方向的数字交换成功得到正确排列。
交换过程如下：
1 2 3   1 2 3   1 2 3   1 2 3
x 4 6   4 x 6   4 5 6   4 5 6
7 5 8   7 5 8   7 x 8   7 8 x
现在，给你一个初始网格，请你求出得到正确排列至少需要进行多少次交换。

输入格式

输入占一行，将3×3的初始网格描绘出来。

例如，如果初始网格如下所示：
1 2 3
x 4 6
7 5 8
则输入为：1 2 3 x 4 6 7 5 8
输出格式
输出占一行，包含一个整数，表示最少交换次数。
如果不存在解决方案，则输出”-1”
输入：
2  3  4  1  5  x  7  6  8
输出：
19
'''
line = '2  3  4  1  5  x  7  6  8 '
start = line.split()
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 交换方向
record = {''.join(start): True}


def bfs():
    target = '12345678x'
    queue = [start.copy()]  # 队列
    hh, tt = 0, 0
    res = 0
    while hh <= tt:
        for _ in range(hh, tt + 1):
            st = queue[hh];
            hh += 1
            if ''.join(st) == target: return res
            k = st.index('x')
            x = k // 3
            y = k % 3
            for oi, oj in move:
                xi, yj = x + oi, y + oj
                if not 0 <= xi < 3 or not 0 <= yj < 3: continue
                st[k], st[xi * 3 + yj] = st[xi * 3 + yj], st[k]  # 交换
                cur = ''.join(st)
                if cur not in record:  # 看是否已经达到过，到达就不走，跳过
                    record[cur] = True
                    tt += 1
                    queue.append(st.copy())
                st[k], st[xi * 3 + yj] = st[xi * 3 + yj], st[k]
        res += 1
    return -1


print(bfs())