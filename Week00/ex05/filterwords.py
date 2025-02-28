import sys
import string 

if(len(sys.argv) != 3):
	print("ERROR")
	sys.exit()
if  sys.argv[1].isnumeric():
	print("ERROR")
	sys.exit()

line = sys.argv[1]
num = int(sys.argv[2])
for char in line:
	if char in string.punctuation:
		line = line.replace(char, ' ')

line = line.split()
res = [a for a in line if len(a) > num ]
print(res)