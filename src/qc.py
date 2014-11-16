import csv

profiles = {}
users = []
pairs = []

def read_profiles(file):
	file_read = csv.reader(file)
	dic = csv.DictReader(open(file,'rbU'))
	for row in dic:
		profiles[row["USER_ID"]] = row
		users.append(row["USER_ID"])

def pairing():
	for i, u in enumerate(users):
		interested_in = profiles[u]["INTERESTED_IN"]
		for u2 in users[i+1:]:
			if interested_in is profiles[u2]["GENDER"]:
				pairs.append((u,u2))
	
	print pairs


read_profiles("profiles.csv")
# print profiles
# print users
pairing()
