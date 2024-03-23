# arbituary numbers

def myfunc(*args):
  print(args)
  return sum(args) * 0.05

# *args means user can pass as many parameters they want and i will store it as a tuple

# now i can pass as many parameters as i want
print(myfunc(40,60))
print(myfunc(40,60,3))
print(myfunc(40,60,3,10))


def myfunc2(*args):
  for item in args:
    print(item)

myfunc2(10,20,30,20)


# kwargs returns a dictionary
def myfunc3(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}.'.format(kwargs['fruit']))
  else:
    print("No fruit found here")

myfunc3(fruit="apple")
myfunc3()

def myfffunc(**kwargs):
  print(kwargs)

myfffunc(fruit="apple",veggies="lettuse")



# combination
def comb(*args,**kwargs):
  print(args)
  print(kwargs)
  print("I would like {} {}".format(args[0],kwargs['food']))

comb(10,20,30,food="dahi bhalle",fruit="apple", animal="dog")