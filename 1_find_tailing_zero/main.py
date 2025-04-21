"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return 'number can not be negative'
        
        sum_from1 = 1
        for num in range(1, number):
            sum_from1 += sum_from1*num
        
        count_zero = 0
        for item in str(sum_from1)[::-1]:# [::-1] reverse str
            
            if item == '0':
                count_zero += 1
            else:
                break
        
        return count_zero
        

if __name__ == "__main__":
    my_solution = Solution()
    # 7 10 15
    print(my_solution.find_tailing_zeroes(0))
