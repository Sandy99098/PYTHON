 # reqular module inpython 
import re
pattern=r"[a-z]oing"
text='''
i was doing work  and was doing   homework 
''' 

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
    
    
import re

pattern=r"past"

text= '''Past Tense: Explanation and Examples - Grammar Monster
    Examples. Uses. simple past tense. I went to work. The Martians landed
    near the aqueduct. The simple past tense is used to describe a completed activity 
    that started in the past and ended in the past. 
    past progressive tense. I was going to work. We were painting the
    door when a bird struck the window. '''
    
matches=re.finditer(pattern,text)
print(match)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
    
#  or we can use the re.findall

matches = re.findall(pattern,text)
for  match  in enumerate( matches):
    print(match)
