from sys import argv

script, filename = argv

#gets a file w/ param given
txt = open(filename)

#var can be put in a string
print "Here's your file %r:" % filename

#give the file a cmd w/ .command_name(params)
print txt.read()
txt.close()

print "Type the filename again:"
#this also works w/ raw input if given file name as a string but have to type exactly
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
