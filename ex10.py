tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line."

#one of the backslashes prints
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

testy = "This \'is \" a \" test"
print testy
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

#\r to return to the start of the line
#comma to remove the newline char that python automatically add (actually replaces it with a space)
#Without going to a new line it overwrites the printed character to make the animation.
