def lesser_of_two_evens(a,b):
  if a%2==0 and b%2==0:
    return min(a,b)
  else:
    return max(a,b)


def animal_crackers(text):
  wordlist = text.lower().split()
  return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Level lamba'))


def makes_twenty(n1,n2):
  return (n1+n2)==20 or n1==20 or n2==20




# level 1
def old_macdonald(name):
  first_half = name[:3]
  second_half = name[3:]
  return first_half.capitalize()+second_half.capitalize()


def master_yoda(text):
  word_list = text.split()
  reversed_word_list = word_list[::-1]
  return ("").join(reversed_word_list)