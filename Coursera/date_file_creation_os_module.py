import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  path = os.path.join(os.getcwd(),filename)
  with open(path,"w") as fl:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  d = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”?
  year = d.date()
  return ("{}".format(year))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
