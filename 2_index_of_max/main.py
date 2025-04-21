"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return 'list can not blank'
        
        keep_max = None
        index_max_num = 0
        count_index = 0
        for num in numbers:
            if keep_max is None:
                keep_max = num
                index_max_num = count_index
            elif num >= keep_max:
                keep_max = num
                index_max_num = count_index

            count_index += 1

        return index_max_num

if __name__ == "__main__":
    my_solution = Solution()
    list_test = [1,2,1,3,5,6,4]
    print(my_solution.find_max_index(list_test))
