#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 定义数字与字母的映射关系
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # 递归函数，用于生成所有可能的组合
        def backtrack(combination, next_digits):
            # 如果没有下一个数字需要处理，将当前组合添加到结果中
            if len(next_digits) == 0:
                output.append(combination)
            # 如果还有下一个数字需要处理，递归生成组合
            else:
                # 获取下一个数字
                digit = next_digits[0]
                # 获取数字对应的字母列表
                letters = phone[digit]
                # 遍历字母列表，递归生成组合
                for letter in letters:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output