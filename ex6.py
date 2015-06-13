#sub in 10
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
#sub in 2 vars
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

#prints the string value w/ surrounding '' for %r
print "I said: %r" % x
#prints same format w/ surrounding '' b/c of '' in the string
print "I also said: '%s'." % y

hilarious = False
joke_evolution = "Isn't that joke so funny?! %r"

#%r prints the word False
print joke_evolution % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#concats w and e
print w + e
