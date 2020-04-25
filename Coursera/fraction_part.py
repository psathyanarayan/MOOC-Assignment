def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
  if (denominator!=0):
    return (numerator/denominator)-(numerator//denominator)
	  
# keep just the fractional part of the quotient
  else:
	  return 0

print(int(fractional_part(5, 5))) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(int(fractional_part(0, 5))) # Should be 0
