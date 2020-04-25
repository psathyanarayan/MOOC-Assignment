def lucky_number(name):
  number = len(name) * 9
  check = "Hello " + str(name) + ". Your lucky number is " + str(number)
  return check
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
