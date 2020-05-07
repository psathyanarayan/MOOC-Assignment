import json
def group_list(group, users):
  if users!="":
    members = group+": "+", ".join(users)
    return json.dumps(members)
  else:
    members = group+":"+"".join(users)
    return json.dumps(members)
    

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
