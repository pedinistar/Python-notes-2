# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 
def old_macdonald(text):
  if len(text) > 3:
    first_half = text[:3]
    second_half = text[3:]
    full_new_str = first_half.capitalize() + second_half.capitalize()
    return full_new_str
  else:
    return "Text is too short!"

print(old_macdonald('macdonald'))



# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
  words_list = sentence.split()
  reversed_words_list = words_list[::-1]
  joined_reversed_words_list = (" ").join(reversed_words_list)
  return joined_reversed_words_list

print(master_yoda('I am home'))
print(master_yoda('We are ready'))


