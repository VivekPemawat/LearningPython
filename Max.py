__author__ = 'vpemawat'

# num1 = raw_input();
#num2 = raw_input();
#print max(num1,num2);

# function to check if the character is vowel


def multiplyListNo(list):
    mul = 1;
    for item in list:
        mul = mul * item

    return mul;


def additionListNo(list) :
    add=0;
    for item in list :
        add = add+item;
    return add;

def reverseString(str) :
    output='';
    for x in str :
        output = x+ output

    return output;


def checkPalindrome(str) :
    length=len(str);
    j=0;
    for i in xrange(0,len-1) :
        if str[i] != str[j] :
            print 'not a palindrome';
            return False;
    print "Yes its palindrome";
    return True;







def checkIfVowel(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        return True
    else:
        return False;


list = ['physics', 'eng', 'hindi', 'maths'];
print len(list);
print checkPalindrome("viv");

count = 0;

for item in list:
    print item;
    count = count + 1;

print count

#check if character is vowel

# iterate through the string

name = "vivek";
print reverseString(name);
list = [1,2,3,4];
print additionListNo(list);
print multiplyListNo(list);

for x in name:
    #print x,"d";
    if checkIfVowel(x) != True:
        print "seomting wrong", x


# similarly we can iterate through the list






