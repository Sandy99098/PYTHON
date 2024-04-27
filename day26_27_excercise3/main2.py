questions = [
    "What is the capital of Nepal?",
    "Which is the tallest mountain in the world?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "What is the tallest mammal on Earth?",
    "What is the largest planet in our solar system?",
    "Who is the father of computer?",
    "Who painted the Mona Lisa?",
    "What is the square root of 64?",
    "How many zones are there in Nepal?"
]

answers = [
    "Kathmandu",
    "Mount Everest",
    "William Shakespeare",
    "H2O",
    "Giraffe",
    "Jupiter",
    "Charles Babbage",
    "Leonardo da Vinci",
    "8",
    "14"
]

name=input("ENter your name ");
print("Hello ",name ,"Welcome in quiz !!")
totalMoney=0;
for i in range(len(questions)):

    user_ans=input(questions[i])
    if user_ans.lower()==answers[i].lower() :
        if i==0:
            print("Congratulation you won rs 1000");
            totalMoney=totalMoney+1000
            
        if i==1:
              print("Congratulation you won rs 4000");
              totalMoney=totalMoney+4000
              

    
        if i==2:
         print("Congratulation you won rs 5000");
         totalMoney=totalMoney+5000;
        
        elif user_ans.lower()==answers[i].lower() and i not in[0,1,2]  :
            print(" Congratulation you won rs 1000")
            totalMoney=totalMoney+1000
        # elif user_ans.lower()==answers[i].lower() and i != [0,1,2 ]:
        #      print(" Congratulation you won rs 2000")
        #      totalMoney=totalMoney+2000
        else:
             print(" Congratulation you won rs 2000")
             totalMoney=totalMoney+2000
    else:
     print(" your answer is wrong ") ;
if totalMoney==0:
    print(" Better luck next Time !! ");
elif totalMoney!=0:
    print("you won rs ",totalMoney)
    