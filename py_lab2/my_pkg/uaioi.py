#!/usr/bin/python3
import re

def union_intersection():
	str1 = input('1st list: ')
	list1 = re.findall("\d+", str1)
	list1_int = [int (i) for i in list1]

	str2 = input('2nd list: ')
	list2 = re.findall("\d+", str2)
	list2_int = [int (i) for i in list2]

	list_intersect = [val for val in list1_int if val in list2_int]
	list_union = list1_int + list2_int

	list_union = list(set(list_union))
	list_union.sort()

	print("=> union ", list_union)
	print("=> intersection ", list_intersect)
