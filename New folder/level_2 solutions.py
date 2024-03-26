# def has_33(nums):
#   for i in range(0,len(nums)-1):
#     if nums[i] == 3 and nums[i+1] == 3:  # or if nums[i:i+2] == [3,3]
#       return True
#   return False

# print(has_33([1,3,3]))
# print(has_33([1,3,1,3]))
# print(has_33([3,1,3]))



# def paper_doll(text):
#   str = ''
#   for char in text:
#     str += char*3
#   return str

# print(paper_doll('hi'))




# def blackjack(a,b,c):
#   if sum([a,b,c]) <= 21:
#     return sum([a,b,c])
#   elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
#     return sum([a,b,c])-10
#   else:
#     return 'BUST'

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))



def summer_69(arr):
  total = 0
  add = True
  for num in arr:
    while add:
      if num!=6:
        total += num
        break
      else:
        add = False
    while not add:
      if num !=9:
        break
      else:
        add = True
        break
  return total 

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))