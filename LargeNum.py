# 大数加法算法

import unittest


def large_sum(num1, num2):
    num1, num2 = str(num1), str(num2)
    num1 = num1[::-1]
    num2 = num2[::-1]
    n1 = len(num1)
    n2 = len(num2)
    n = max(n1, n2)
    num1 += '0' * (n - n1)
    num2 += '0' * (n - n2)
    add = 0
    res = ''
    for i in range(n):
        su = int(num1[i]) + int(num2[i]) + add
        res += str(su % 10)  # 取个位数的结果
        add = su // 10  # 进位数
    if add != 0:
        res += str(add)
        print(res)
    res = int(res[::-1])
    return res


# 测试代码
class TestLargeSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(large_sum(5649554, 966664), 6616218)
        self.assertTrue(large_sum(998764654313, 65453158786), 9903187124601)


if __name__ == '__main__':
    unittest.main()
