__author__ = 'brehm'
#Print from 100 - 1

#Definitions
printnumber = 100;
#For Loop to print from 100 -1
for i in range(0,100):
    print "The number is:", printnumber;
    printnumber = printnumber - 1;


#Print without the For Loop


i = 100
numbers = []

while i > 0:
    # print "At the top i is %d" % i
    numbers.append(i)

    i = i - 1
    # print "Numbers now: ", numbers
    # print "At the bottom i is %d" % i


print "The numbers, from 100 down to 1: "

for num in numbers:
    print num