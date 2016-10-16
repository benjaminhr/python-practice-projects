from sys import argv

#Creates input for user --> file
script, input_file = argv

#Read all contents
def print_all(f):
    print f.read()

#Read invidivual contents
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now lets rewind, kind of like a tape."

rewind(current_file)

print "Let's print all lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
