#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:28:47 2023

@author: ko
"""

from sys import argv

scirpt, name, age, weight, height = argv 

print("{} is {} years old, weighs {} lbs, and is {} tall.".format(name, age, weight, height))



#command: (base) ko@x86_64-apple-darwin13 Module1-Intro_to_Python % python assignment6-2.py milk 4 9.2 30cm  
#output:  milk is 4 years old, weighs 9.2 lbs, and is 30cm tall.