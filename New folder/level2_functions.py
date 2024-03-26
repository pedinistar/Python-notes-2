# def has_33(nums):
#   for i in range(0,len(nums)-1):
#     if nums[i]==nums[i+1]:
#         return True
#   return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))



# def paper_doll(text):
#     temp_list = []
#     for letter in text:
#         temp_list.append(letter*3)
#     new_string = ("").join(temp_list)
#     print(new_string)

# paper_doll('Hello')
# paper_doll('Mississippi')




# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
  
# def blackjack(a,b,c):
#   sum = a+b+c
#   if sum <= 21:
#     return sum
#   else:
#     if a or b or c == 11:
#       sum -= 10
#       if sum > 21:
#         return 'BUST'
#       else:
#         return sum
  
# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))



# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
  sum = 0
  for i in range(0,len(arr)):
    if arr[i] == 6:
      if arr[i+1] == 9:
        if arr[i+2] == 9:
          continue
      else:
       sum = sum + arr[i]
    else:
      sum = sum + arr[i]
  return sum

def summer_69(arr):
  sum = 0
  index_of_6 = arr.index(6)
  index_of_9 = arr.index(9)
  for i in range(0,len(arr)):
    if i != index_of_6:
        sum = sum + arr[i]
    else:
        
        continue
  return sum

print(summer_69([4, 5, 6, 7, 8, 9]))

print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([1, 3, 5]))
# print(summer_69([2, 1, 6, 9, 11]))