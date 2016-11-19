import sys
import random


"""

Get random, and insert in list

"""

constraints = {}
groups = {}

def parse_file(filename):
	groups = []
	with open(filename) as f:
		group = []
		for line in f:
			if line in ['\n', '\r\n']:
				if group:
					groups.append(group)			
					group = []
			else:
				group.append(line.strip())	

	return groups


def define_constraints(file):
	groups = parse_file(file)
	
	for group in groups:
		for name in group:
			constraints[name] = group


filename = sys.argv[1]

try: 
	define_constraints(sys.argv[2])
except IndexError as e:
	print("You do not have any constraints.")

with open(filename) as f:
	names = f.read().splitlines()

random.shuffle(names)

linear_list = []

while names:
	name = random.choice(names)
	if len(linear_list) == 0:
		linear_list.append(name)
		names.remove(name)
	else:
		if name not in constraints:
			linear_list.append(name)
			names.remove(name)
		else:	
			for index in range(len(linear_list)):
				# gamba
				i = len(linear_list) if index == 0 else index
				if linear_list[index] not in constraints[name] and linear_list[i-1] not in constraints[name]:
					linear_list.insert(index, name)
					names.remove(name)
					break

print 'The final list is: ',linear_list


