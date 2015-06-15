formatter = "%r %r %r %r"

#prints in 4 num vals
print formatter % (1,2,3,4)

#subs in strings w/ ''
print formatter % ("one", "two", "three", "four")

#prints boolean vals (no string)
print formatter % (True, False, False, True)

#prints the formatter var value 4 times
print formatter % (formatter, formatter, formatter, formatter)

#prints string phrase surrounded by '' and separates by a space
#double quotes vs single quotes printing:
#Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for debugging and inspection, so it's not necessary that it be pretty.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
