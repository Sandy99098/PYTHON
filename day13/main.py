#  string methods in python

# string are immutable,cannnot be change but can be made new 
a="!!sandy!!!";
a="!!sandy!!! ram !!";
print(a);
print(a.upper());
b="HELLO ";
print(b.lower());
print(a.rstrip("!")) #trailing character lai matra remove garxa
print(a.split(" "));
heading="introduction to js"
print(heading.capitalize()) #turn on the first letter capatilized

blogheading="introduction to js";
print(len(blogheading));
#align
print(blogheading.center(40)) #align the elements to the center according to the paramater given 
#count
print(a.count("sandy"))
print(a.count("!"))
      #ends with 
print(a.endswith("!"))
print(a.endswith("sandy")) 

b=" he is a good person but ";
#find
print(b.find("i"));
print(b.index("i")); #shows error  if id doesnot found
#check if the string is alpha  number or not ;

print( a.isalnum());
alphanum="wer1";
print( alphanum.isalnum())
#check if the number is number or not
num="12";
print(num.isnumeric());
print(a.isnumeric())
 # check if alphabet or not 
a="helllo";
print(a.isalpha());
print(num.isalpha());
#check if the string is in lower case or not
upper="AA";
print(upper.islower());
#to check if the string is printable or not 
print("#to check if the string is printable or not ")
str1="hello how are you \t i am fine \n"; #it contain \n and /t so it is not printanble
print(str1.isprintable()); 
a="ysrtve"
print(a.isprintable())
#to checck is there is white space or not . tab also is included as it is also white spaces "\t"
print(a.isspace());
b=" \n \t"
print(b.isspace());
# to check if thrhstring is title or not
str2="Is A Mocking Bird"
print(str2.istitle());
str2="how and what"
print(str2.istitle());

# to swap the cases
details='he is doing good things';
print(details.swapcase())
details='he is  DOING GOOD things';
print(details.swapcase())






