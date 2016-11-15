import sys
import random

groups = []
done = []

def parse_file():
	filename = sys.argv[1]
	groups = []
	with open(filename) as f:
		group = {'type': 'restricted',
				 'names': []}
		for line in f:
			if line in ['\n', '\r\n']:
				if group['names']:
					groups.append(group)			
					group = {'type': 'restricted',
				 			 'names': []}
			elif line.lower().strip() in ['free', 'restricted']:
				group['type'] = line.strip()
			else:
				group['names'].append(line.strip())	

	return groups


def generate():

	generated_raffle = {}
	for group in groups:
		for name in group['names']:
			generated_raffle[name] = sort(name, group)

	print(generated_raffle)

def sort(name, group):
	
	groups_list = [g for g in groups if g != group] if group['type'] == 'restricted' else groups
	
	#do it again if list empty
	while True:
		group_sorted = random.choice(groups_list)
		print('done', done, 'grpup', group_sorted['names'], name)
		names_available = [n for n in group_sorted['names'] if n != name and n not in done]
		print(names_available)
		if names_available:
			break

	name_sorted = random.choice(names_available)
	done.append(name_sorted)

	return name_sorted



groups = parse_file()
generate()

