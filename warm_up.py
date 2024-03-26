# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
  if a%2==0 and b%2==0:
    return min(a,b)
  else:
    return max(a,b)


print(lesser_of_two_evens(2,4) )
print(lesser_of_two_evens(2,5) )



# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
  text_list = text.split()
  first_word = text_list[0]
  second_word = text_list[1]
  first_letter_of_first_word = first_word[0]
  first_letter_of_second_word = second_word[0]
  return first_letter_of_first_word.upper() == first_letter_of_second_word.upper()


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))




# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
  if sum([a,b]) == 20 or a == 20 or b == 20:
    return True
  else:
    return False

print(makes_twenty(20,10))
print(makes_twenty(12,8) )
print(makes_twenty(2,3) )