# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums_list):
  for i in range(0,len(nums_list)-1):
    if nums_list[i] == 3:
      if nums_list[i+1] == 3:
        return True
  return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]) )
print(has_33([3, 1, 3]) )



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(str):
  new_str = ''
  for letter in str:
    new_str += letter*3
  return new_str



print(paper_doll('Hello'))
print(paper_doll('Mississippi'))