#!/usr/bin/python3


def union_intersection():
	value = int(input('Input binary number : '))

	def binary_to_decimal(bi_num):
		decimal_number = 0
		bi_num_str = str(bi_num)
		for i, digit in enumerate(bi_num_str):
			decimal_number += int(digit) * pow(2, len(bi_num_str) - 1 - i)
		return decimal_number

	num = binary_to_decimal(value)
	o = oct(num)
	h = hex(num)

	print("=> OCT> ", o)
	print("=> DEC> ", num)
	print("=> HEX> ", h)

