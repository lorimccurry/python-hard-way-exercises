from sys import argv

script, user_name = argv
blue = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(blue)

print "Where do you live %s?" % user_name
lives = raw_input(blue)

print "What kind of computer do you have?"
computer = raw_input(blue)


print """
Aright, so you said %r about liking me.
You live in %r. Not sure what that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
