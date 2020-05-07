def email_list(domains):
	emails = []
	for i,users in domains.items():
	  for user in users:
	    user=user+"@"+i
	    emails.append(user)
	    
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
