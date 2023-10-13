"""A lazy economics teacher wants to write his reports really quickly. Create a Random report writer with a list of generic comments. It should ask for the number of students and then generate a random comment for each student."""

import random
comments = ["is a hardworking student and is constantly contributing to our class sessions", "is a smart and inquisitive student who loves to learn.","is a talented student who has a real passion for learning.","is a kind and caring student who always looks out for others.","is a quick learner who loves a challenge.","is a confident and enthusiastic student who is always willing to learn new things.","is progressing nicely and shows consistent improvement in many areas of schoolwork","is a role model in school and sets a good standard for classmates to follow."]

students = int(input("Please type in the number of students in your class"))
i = 0
while i in range (students):
  print("Student",i+1,random.choice(comments))
  i += 1 
