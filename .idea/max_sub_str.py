

def max_sub1(num_list):
    sub_sum = 0
    max_sum = None
    for i in num_list:
        if sub_sum < 0:
            sub_sum = i
        else:
            sub_sum += i

        if not max_sum:
            max_sum = sub_sum
        if sub_sum > max_sum:
            max_sum = sub_sum
    return max_sum


def max_sub2(num_list):
    global sum
    sum = [-1000000 for _ in num_list]
    global result
    result = None

    def max_helper(i):
        print(i)
        global result
        global sum
        if result == None:
            result = num_list[i]

        if not sum:
            sum.append(num_list[i])
            return
        sum[i] = max(sum[i-1] + num_list[i], num_list[i])
        result = max(sum[i], result)
    for i in range(len(num_list)):
        max_helper(i)
    return result





if __name__ == "__main__":
    a = [1,-2,3,10,-4,7,2,-5]
    print(max_sub2(a))

