
from logic import Logic

def longest(string, filename="enable1.txt"):
	file = open(filename, "r") 
	max_letter = ""
	for line in file.read().splitlines():
		logic = Logic(string, line)
		if logic.match():
			if len(max_letter) < len(line):
				max_letter = line
	return(max_letter)

print(longest("uruqrnytrois", "enable2.txt"))
print(longest("rryqeiaegicgeo??"))