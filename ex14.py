# -*- coding:utf-8 -*-
from sys import argv

script, user_name, user_sex = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
print "What is your gender? %s" % user_sex
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
And I know you're %r
YOu live in %r, Not sure where that is.
And you have a %r computer.Nice.
""" % (likes, user_sex, lives,computer)
