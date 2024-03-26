def vol(rad):
    return (4/3)*3.14*(rad**3)

print(vol(2))


def ran_check(num,low,high):
  if num in range(low, high+1):
     return "{} is in the range between {} and {}".format(num,low,high)
  return "{} is not in the range between {} and {}".format(num,low,high)

print(ran_check(5,2,7))

def ran_bool(num,low,high):
    return num in range(low,high+1)

print(ran_bool(3,1,10))



def up_low(s):
  lower_counter = 0
  upper_counter = 0
  for letter in s:
    if letter.isupper():
      upper_counter+=1
    elif letter.islower():
      lower_counter+=1
    else:
       pass
  
  print("Original String :  {}".format(s))
  print("No. of Upper case characters :  {}".format(upper_counter))
  print("No. of Lower case Characters :  {}".format(lower_counter))

# def up_low(s):
#   d = {'upper':0,'lower':0}
#   for letter in s:
#     if letter.isupper():
#       d['upper']+=1
#     elif letter.islower():
#       d['lower']+=1
#     else:
#        pass
  
#   print("Original String :  {}".format(s))
#   print("No. of Upper case characters :  {}".format(d['upper']))
#   print("No. of Lower case Characters :  {}".format(d['lower']))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)




def unique_list(lst):
   return list(set(lst))

# or

# def unique_list2(lst):
#    seen_nums = []
#    for num in lst:
#       if num not in seen_nums:
#          seen_nums.append(num)
#    return seen_nums

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))




def multiply(numbers):
  mul = 1
  for num in numbers:
     mul*=num
  return mul

print(multiply([1,2,3,-4]))




def palindrome(s):
   return s[::-1] == s

# or 

def palindrome(s):
   s = s.replace(' ','')
   return s[::-1] == s

print(palindrome('helleh'))
print(palindrome('helo'))




import string

def ispangram(str1, alphabet=string.ascii_lowercase):
   str1 = str1.replace(" ","")
   unique_list = set(str1.lower())
   alphabet = set(alphabet)
   return unique_list == alphabet

print(ispangram("The quick brown fox jumps over the lazy dog")) 