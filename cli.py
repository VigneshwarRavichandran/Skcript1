
from logic import Logic
import click


@click.group()
def main():
    pass

@main.command()
@click.option('--string1')
@click.option('--string2')
def magic(string1, string2):
    logic = Logic(string1, string2)
    if logic.match():
    	print("Yes, '{0}' can be created".format(string2))
    else:
    	print("No, '{0}' can't be created".format(string2))

@main.command()
@click.option('--string')
@click.option('--filename')
def longest(string, filename):
	try:
		file = open(filename, "r") 
	except:
		print("File Not Found")
		return None
		
	max_letter = ""
	for line in file.read().splitlines():
		logic = Logic(string, line)
		if logic.match():
			if len(max_letter) < len(line):
				max_letter = line
	print(max_letter)

if __name__ == '__main__':
    main()
