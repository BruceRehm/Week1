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


print "The numbers, from 100 down to 1: ";

for num in numbers:
    print num;

#Random Array of 50 with min and max values printed

#Set up array with 50 random numbers
bruce = [10,102,20,340,34,667,890,21,34,67,123,98,23,1,0,127,876,12,56,98,111,222,999,1011,234,965,12,4,9,19,27,27,34,36,12,555,888,19,27,80,39,12,45,76,77,87,9999,865,803,119];

#Call min and max functions

minbruce = min(bruce);
maxbruce = max(bruce);

#Print lenght of array and the min and max values of the array
print "The length of bruce array is " , len(bruce);
print "The minimum value of bruce array is " , minbruce;
print "The maximum value of bruce array is " , maxbruce;

# Read in a string and reverse the printing of the words

#Load a variable with a name
userName = "Why Amit Chavan";

#print orignal contents of string
print userName.split(' ');

#reverse the words in the list and print
alist = userName.split(' ');
alist.reverse();
alist = ' '.join(alist)
print alist;
