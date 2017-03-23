# coding=utf-8
__author__ = 'zengyue'


from sys import argv

script, filemane = argv

txt = open(filemane)

print "Here's your file %r :" % filemane
print txt.read()
txt.write("hello")
# txt.close()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
# txt_again.close()