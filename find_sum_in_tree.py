NO_RESULT = 0
EQUAL = 2


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_sum(target, node, cur_sum):
    if node.left == None:
        return NO_RESULT, None
    if cur_sum + node.left.value == target:
        return EQUAL, node.left
    find_sum(target, node.left, cur_sum + node.left.value)

    if node.right == None:
        return NO_RESULT, None
    if cur_sum + node.right.value == target:
        return EQUAL, node.left
    find_sum(target, node.left, cur_sum + node.right.value)


if __name__ == "__main__":



