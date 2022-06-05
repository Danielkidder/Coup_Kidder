# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:32:49 2022
@author: Daniel Mishler
"""

"""
Objectives:
    - Understand what the terminal is and how to run a written python program
    - Understand basic usage of random numbers
    - Understand basic string parsing
    - Understand basic file input and out with open() and .close()
    - Understand how to build a class
    - Understand how to build and parse a text file
    - Programming philosophy: Understand defensive programming
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - If you want some extra practice, proceed to the extra practice document
"""

# Problem 1
# Print a random whole number in the range of [1,10] (inclusive)

# Problem 2
# Print all of the perfect squares in the range of [1,10000]
# Note: you should use a loop (100 print statements will get you 0 points),
#       but you don't have to use 'for i in range(10000)' as your statement

# Problem 3
# Open the file `abab.txt` and print the total number of times the character
# 'b' appears in the file
# This shouldn't be hard-coded. You should be printing from a variable!
# Don't forget to close the file when you're done!
# Note: you're allowed to look at how the file was generated if you want


# Problem 4
# Open the file `abab.txt` and print the following:
    # the longest sequence of 'a's in the file
    # the longest sequence of 'b's in the file
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
"""
    Created on Wed Jun  1 11:54:48 2022

    @author: danielkidder
    """
'''
    import random
    print(random.randint(1,10)) 
'''
'''
    a=1
    while (a<101):
        print(a**2)
        a=a+1 
'''
'''
    mylines=[]
    with open("abab.txt","r")as myfile:
       for myline in myfile:
           mylines.append(myline)
           
           substr="b"
           for line in mylines:
               index=0
               prev=0
               while index<len(line):
                   index=line.find(substr, index)
                   if index==-1:
                       break
                   print("" * (index-prev)+ "b", end='')
                   prev= index+len(substr)
                   index+= len(substr)
                   close myfile
'''
'''
    myFile = open("abab.txt", "r")
    b_count = 0
    for character in myFile.read():
        if character == "b":
            b_count = b_count + 1
    myFile.close()
    print(b_count)
    mylines=[]
    with open("abab.txt","r")as myfile:
       for myline in myfile:
           mylines.append(myline)
    '''      
'''
    myFile = open("abab.txt", "r")
    b_cons = 0
    a_cons = 0
    b_highest = 0
    for character in myFile.read():
        if character == "b":
            b_cons += 1
            a_cons = 0
        else:
            a_cons += 1
            b_cons = 0
        if b_cons > b_highest:
            b_highest = b_cons
    myFile.close()
    print(b_highest)
    '''
'''
    myFile = open("abab.txt", "r")
    b_cons = 0
    a_cons = 0
    a_highest = 0
    for character in myFile.read():
        if character == "a":
            a_cons += 1
            b_cons = 0
        else:
            b_cons += 1
            a_cons = 0
        if a_cons > a_highest:
            a_highest = a_cons
    myFile.close()
    print(a_highest)
    '''