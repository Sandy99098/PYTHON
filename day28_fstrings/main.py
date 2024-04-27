#fstrings in python
sentence="Hey I am {} and I am from {}";
# name=input("Enter your name \t")
name="Sand"
# country=input("Enter your country name \t")
country="america"
# sentence="Hey I am {0} and I am from {1}";
print(sentence.format(name,country))

print(f" Hey I am {name} and I am from {country}")

price=40.29302;
txt=f"for only {price:.2f}" #to print only two digit after decimal.must use .
# txt=f"for only {{price:.2f}} #to print only two digit after decimal.must use .

print(txt)
# f string 
print(f"{2+3}")