def convert_distance(miles):
	km = miles * 1.6 
	result = "{miles} miles equals {km:0.1f} km".format(miles=miles,km=miles * 1.6 )
	return result

print(convert_distance(12)) 
print(convert_distance(5.5)) 
print(convert_distance(11))  
