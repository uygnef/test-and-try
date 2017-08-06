'''
 题目一：买书
       有一书店引进了一套书，共有3卷，每卷书定价是60元，书店为了搞促销，推出一个活动，活动如下：
      
       如果单独购买其中一卷，那么可以打9.5折。
       如果同时购买两卷不同的，那么可以打9折。
       如果同时购买三卷不同的，那么可以打8.5折。
      
       如果小明希望购买第1卷x本，第2卷y本，第3卷z本，那么至少需要多少钱呢？（x、y、z为三个已知整数）。
 
       当然，这道题完全可以不用动态规划来解，但是现在我们是要学习动态规划，因此请想想如何用动态规划来做？
 
'''
import numpy as np

def solution(x, y, z):
    min_money = np.zeros((x+1, y+1, z+1))
    return helper(x,y,z, 0, min_money)


def helper(x, y, z, money, min_money):
    if ((x | y | z) == 0):
        return money

    if(min_money[x][y][z] != 0):
        return min_money[x][y][z]

    min_list = []
    if x != 0:
        min_list.append((helper( x-1, y, z, min_money + 60*0.95, min_money ), (x-1, y,z)))
        if y != 0:
            min_list.append((helper(x - 1, y - 1, z, min_money + 120 * 0.9, min_money), (x-1, y-1,z)))
            if z != 0:
                min_list.append((helper(x - 1, y -1, z - 1, min_money + 180 * 0.85, min_money), (x-1, y-1,z-1)) )
        else:
            if z != 0:
                min_list.append((helper(x - 1, y, z - 1, min_money + 120 * 0.9, min_money), (x-1, y,z -1)))

    elif y != 0:
        min_list.append((helper( x, y - 1, z, min_money + 60*0.95 , min_money),(x, y-1,z)))
        if z != 0:
            min_list.append((helper(x, y - 1, z - 1, min_money + 120 * 0.9, min_money), (x, y-1,z-1)))
    else:
        min_list.append((helper( x, y, z-1, min_money + 60*0.95, min_money ), (x, y,z-1)))

    print(min_list[0][0])
    index = min_list.index(min(i[0] for i in min_list))
    money = min_list[index][0]
    print(money)
    num = min_list[index][1]
    min_money[num[0]][num[1]][num[2]] = money
    return money


print(solution(3,4,5))





