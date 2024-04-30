#dictonary , store multiples and use curly brackets . and it is ordered after vesion 3.7
dic ={
    "Sandeep":"Human Beings",
    "Book":"object"
}
print(dic["Sandeep"])

details ={
    1:"Sandy",
    2:"Ram",
    4:"Shyam"  "class 6",
    "sandeep":"Human Being"
}
print("details of roll no 4 is ",details[4])

print("details are ",details)
print(details[2]) # it shows error if ram is not in the dictionary
print(details.get(1)) # it prints none if it 1 is no in the dictionary
print(details.keys())

for key in details.keys() :
    print(details[key])

for key in details.keys() :
    print(f"The value corresponding to the {key} is {details[key]}")


