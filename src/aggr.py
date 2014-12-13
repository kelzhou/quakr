import csv

profiles = {}
users = []
# match = {"user1id-user2id": approval rating}
match = {}
# sucessful_match = {"user": [list of matches]}
successful_match = {}
def read_profiles(file):
	file_read = csv.reader(file)
	dic = csv.DictReader(open(file,'rbU'))
	for row in dic:
		profiles[row["USER_ID"]] = row
		users.append(row["USER_ID"])

def read_match(file):
	file_read = csv.reader(file)
	dic = csv.DictReader(open(file,'rbU'))
	for row in dic:
		key = row["USER1_ID"] + "-" + row["USER2_ID"]
		if key in match:
			match[key].append(row["MATCH"])
		else:
			match[key] = [row["MATCH"]]
def aggr_match():
	for m in match:
		prob = 0
		for v in match[m]:
			prob += int(v)
		prob = prob / (len(match[m]) + 0.0)
		match[m] = prob
def match_output():
	for m in match:
		if match[m] > 0.5:
			m1 = m.split("-")[0]
			m2 = m.split("-")[1]
			if m1 in successful_match:
				successful_match[m1].append(m2)
			else:
				successful_match[m1] = [m2]
			if m2 in successful_match:
				successful_match[m2].append(m1)
			else:
				successful_match[m2] = [m1]
	print successful_match


read_profiles("profiles.csv")
read_match("matches.csv")
aggr_match()
match_output()
