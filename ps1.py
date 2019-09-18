#!/usr/bin/python3
#parity-check
#input binary message
input_bin =str(input ("Enter binary bit data that has to be transmitted:"))
#Defining a function to count no. of occurrences of 1
count = 0
for i in input_bin: 
	if i == '1': 
		count = count + 1
#taking binary digits as input 
#count checking if even or odd
#n=len(bin_list)
if (count%2==0):
	input_bin = input_bin + "1"
	#bin_list = bin_list.split("")
	print ("Parity bit data:{0}".format(input_bin))
else:
	input_bin = input_bin + "0"
	#bin_list = bin_list.split("")
	print ("Parity bit data:{0}".format(input_bin))

#Bit-oriented framing
string = input_bin
   
# Prints the string by replacing only 3 occurence  
str2 = string.replace("010", "0100", 3)
#appending 0101 at end
str1=str2+"0101"
print("Transmitting data:{0}".format(str1))
