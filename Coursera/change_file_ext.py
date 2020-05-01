filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
import json
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for index in range(len(filenames)):
  o=filenames[index]
  if(o.endswith("hpp")):
    n=o.replace("hpp","h")
  else:
    n=o
  newfilenames.append(n)  

print((json.dumps(newfilenames))) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
