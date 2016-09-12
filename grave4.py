#More complex printing
formatter = "%r %r %r %r"

#Adding integers to string formatters from variable formatter
print formatter % (1, 2, 3, 4)

#Adding strings to string formatter
print formatter % ("one", "two", "three", "four")

#Adding booleans as string formatter
print formatter % (True, False, False, True)

#Adding variable 'formatter' as the string formatter for itself
#But it does not add a string to the formatters inside string formatters
print formatter % (formatter, formatter, formatter, formatter)

'''Using strings as string formatters - written on seperate lines
but print on same line with spaces inbetween due to comma
'''
print formatter % (
    "I had this thing."",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#Note-to-self: when using a string with %r, it will print with single quotes

#---------------------------------------------------------

#More printing practice, "\n" creates a new line
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApril\nMay\nJun\nJul\nAug"

#Using "%r" won't print with new lines
print "Here are the days: ", days
print "Here are the months: ", months

#Multiline string prints
print """
Triple quotes after a print allows us to do multi-line
comments or strings :-)
"""
