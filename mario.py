# Mario Challenge less comfortable:
# Implement a program that prints out a half-pyramid of a specified height, per the below.

# $ ./mario
# Height: 4
   #
  ##
 ###
####


while True:
    height = int(input("Height: "))
    if height in range(9):
        break

for i in range(height):
    print(" " * (height - 1 - i), end='')
    print('#' * (i + 2))




