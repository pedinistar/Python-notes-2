def myfunc(str):
  all_letters_list = []
  for i in range(0,len(str)):
    if i%2==0:
      all_letters_list.append(str[i].upper())
    else:
      all_letters_list.append(str[i])
  new_str = ("").join(all_letters_list)
  return new_str

print(myfunc('standing next to you'))