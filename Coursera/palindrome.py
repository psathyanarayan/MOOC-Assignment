def is_palindrome(new_string):
	# We'll create two strings, to compare them
	input_string = ""
	input_string = new_string.replace(" ","")
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in range(len(input_string)):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if input_string[i] !="" and (input_string[i].lower()==input_string[-i-1].lower()):
			c= True
			i+=1
		else:
		  return False
	if c==True:
	  return True
	  
	# Compare the strings


print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kayak")) 
