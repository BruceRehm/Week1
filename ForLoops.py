__author__ = 'BruceRehm'
age = [10,102,20,340];
username = ["Amit", "Brian", "Bruce", "Rob"]
print username;
print username[3];
print "Length of this array is", len(username);

print len(age);

sum_numbers = 0;
for index in range(len(age)):
    print "Print element at location ", index,age[index];
    sum_numbers = sum_numbers + age[index];

print sum_numbers;
print "Average ages is ", sum_numbers/len(age);

