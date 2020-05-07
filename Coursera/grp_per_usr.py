def groups_per_user(group_dictionary):
	user_groups = {}
	grp=[]
	# Go through group_dictionary
	for i,j in group_dictionary.items():
		# Now go through the users in the group
		for k in j:
		  grp.append(k)
		  user_groups[k]=i
		  
		  
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
