#!/usr/bin/python3
import my_pkg


choice = int(input('Select menu: 1)conversion 2)union/intersection 3)exit ?'))

while choice != 3:
	if choice == 1:
		my_pkg.binary_to_others()
	elif choice == 2:
		my_pkg.union_intersection()
	else:
		print("please re-enter")
	choice = int(input('Select menu: 1)conversion 2)union/intersection 3)exit?'))


