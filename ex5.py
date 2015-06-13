name = 'Zed A. Shaw'
age = 35
height = 74.0
height_feet = height / 12.0
height_inches = height % 12.0
weight = 180
eyes = 'Blue'
teeth = 'Purple'
hair = 'Green'

#sub in var name string
print "Let's talk about %s." % name
#subs in float # vars
print "He's %f feet %f inches tall." % (height_feet, height_inches)
#subs in digit var w/o floats
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
#subs in strings
print "He's got %s eyes and %s hair." % (eyes, hair)
#subs in string
print "His teeth are usually %s depending on the coffee." % (teeth)

#subs in each value and the sum of them
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)

#prints string
print "check it %s now" % (eyes)
#prints raw string w/ '' around it
print "check it %r now now" % (teeth)
