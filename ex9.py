days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#print days on same line b/c of ,
print "Here are the days: ", days

#\n is new line
print "Here are the months: ", months

#%r doesn't work with /n
print "Here are the months %r" % months

# """ prints a block of text however input between quotes; don't put spaces between quotes
print """
"There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
