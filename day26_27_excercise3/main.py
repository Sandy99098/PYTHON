# create a program capable of displaying question to the use like kbc 
# use the data type to store the question and corrected answers 
# 3. display the final amount the person is taking home after playing game 
name=input("Hello sir , Enter your name \n")
print("Welcome in KBC ",name,"!")
questions=[
    "who is the father of computer\t ?",
    "what is the height of nigra fall ??",
    "which is the tallest mountain of the world ?"
    ]
answer=["Charles Babbage","10002","Mount Everest"]
# print(type(questions))
sum=0

for i in range(len(questions)):
    # print(questions[0])
    ans=input(questions[i])
    if ans.lower()==answer[i].lower():
     if i==0:
        print("congratulation you won rs 1000")
        sum=sum+1000
   
     elif i==1:
        print("congratulation you won rs 2000")
        sum=sum+2000
     elif i==2:
        print("congratulation you won rs 4000")
        sum=sum+4000  
    
     else:
        print(" your answer is wrong ")
   
   
if sum==0:
        print(" your didnot win this time , your all answer is wrong  ")
elif sum!=0:
    print(" Congratulaion",name ,"you have won Total of Rs",sum);    
