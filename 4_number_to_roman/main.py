"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:

        if number < 0:
            return 'number can not less than 0'
        elif number == 0:
            return 'There is no zero in Roman numerals'

        dict_roman = {}
        dict_roman[5000] = 'V̅'
        dict_roman[1000] = "M"
        dict_roman[900] = "CM"
        dict_roman[500] = "D"
        dict_roman[400] = "CD"
        dict_roman[100] = "C"
        dict_roman[90] = "XC"
        dict_roman[50] = "L"
        dict_roman[40] = "XL"
        dict_roman[10] = "X"
        dict_roman[9] = "IX"
        dict_roman[5] = "V"
        dict_roman[4] = "IV"
        dict_roman[1] = "I"

        next_number = number
        roman_num = ''
        for key, value in dict_roman.items():
            divid_floor = next_number//int(key)
            divid_modulus = next_number%int(key)

            if divid_floor > 0:
                for i in range(0, divid_floor):
                    roman_num = roman_num + value
                next_number = divid_modulus
        return roman_num


if __name__ == "__main__":
    my_solution = Solution()
    for num_test in range(1, 120):
        print(num_test)
        print(my_solution.number_to_roman(num_test))
