"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def num_to_thai_sub(self, number: int) -> str:
        list_thai_number_word = ['หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
        list_thai_digi_word = ['สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน', 'สิบล้าน']
        list_thai_number_extra_word = ['เอ็ด', 'ยี่']
        list_power_digi = [10,100,1000,10000,100000,1000000]

        max_digi = len(str(number)) - 2
        
        thai_word = ''
        temp_number = number
        for num in str(number):
            num = int(num) - 1
            # 10 - 19, 20 - 29
            if max_digi == 0 and temp_number < 30:
                if temp_number > 9 and temp_number < 20:
                    thai_word = thai_word + list_thai_digi_word[max_digi]
                    
                elif temp_number >= 20 and temp_number < 30:
                    thai_word = thai_word + list_thai_number_extra_word[num]
                    thai_word = thai_word + list_thai_digi_word[max_digi]
                
            


            else:
            
                if num >= 0:
                    if num == 0 and temp_number > 9 and temp_number < 100:
                        thai_word = thai_word + list_thai_number_extra_word[num]
                    else:
                        #thai_word = thai_word + list_thai_number_word[num]
                        if number == 101 and temp_number < 100:
                            thai_word = thai_word + list_thai_number_extra_word[num]
                        else:
                            thai_word = thai_word + list_thai_number_word[num]
                
                if max_digi >= 0 and num >= 0:
                    thai_word = thai_word + list_thai_digi_word[max_digi]
            
            if max_digi >= 0:
                temp_number = list_power_digi[max_digi] * (num+1)
            
            max_digi -= 1
            

        return thai_word

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return 'number can not less than 0'
        elif number == 0:
            return ' ศูนย์'
        elif number < 110:
            return self.num_to_thai_sub(number)
        elif number == 10000000:
            return 'สิบล้าน'
        elif number > 10000000:
            return 'number can not more than 10000000'
        else:
            sum_word = ''
            temp_num = number
            for num in str(number):

                #clear_num = round(temp_num, -(len(str(temp_num)) - 1))
                clear_num_str = str(num)
                for item in range(0, (len(str(temp_num))-1)):
                    clear_num_str = clear_num_str + '0'
                clear_num = int(clear_num_str)
                
                sum_word = sum_word + self.num_to_thai_sub(clear_num)
                
                temp_num = temp_num-clear_num
                if temp_num < 100:
                    sum_word = sum_word + self.num_to_thai_sub(temp_num)
                    break
                
            return sum_word


        


if __name__ == "__main__":
    my_solution = Solution()
    input = 100
    for num_test in range(99,120):
        print(num_test)
        print(my_solution.number_to_thai(num_test))
    #print(my_solution.number_to_thai(input))
            
