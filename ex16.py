# coding=utf-8
__author__ = 'zengyue'


from sys import argv

script, filename = argv

txt = open(filename)

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file, Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

put = "'%s, %s, %s'" % (line1, line2, line3)

target.write(put)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()