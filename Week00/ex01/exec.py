import sys

for i in range(len(sys.argv) , 2, -1):
    word = sys.argv[i-1].swapcase();
    print (word[::-1], end=' ')
word = sys.argv[1].swapcase();
print (word[::-1])
