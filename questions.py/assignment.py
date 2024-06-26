#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_"+user_name + "!")     
hello_name("Andrew")        


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 101, 2):
        print(num)


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


def max_num_in_list(a_list):
    max_number= max(numbers)
    return max_number
numbers= [20,5,13,3]
print(max_num_in_list(numbers))



#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True   # if divisible to 400    (notes made to follow code for any mistakes)
            else:
                return False   #if its dividible by 100 not by 400
        else:
            return True   #  if its divisible by 4 but not by 100
    else:
        return False     #and not divisible by 4 
print(is_leap_year(2200))
print(is_leap_year(2000))
print(is_leap_year(2024))


               
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def are_consecutive_numbers(nums):
    if len(nums) < 2:
        return False 
    
    nums.sort() 
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            return False
    
    return True

print(are_consecutive_numbers([2, 3, 4, 5, 6, 7])) 
print(are_consecutive_numbers([1, 2, 4, 5]))             

    


