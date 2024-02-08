import random
print("                                   Welcome To The quiz Game                     \n              ")
int = a = input('''                         1:  Enter 1 To Play General Knowledge Question.
                         2:  Enter 3  To Quit .....''')
if a == "3":
    a=6
# Main While Starting
while a!=6:
 match a :
     # Case 1 Start
      case "1" :
          
        

        a_list=[["Who was the first woman Prime Minister of Pakistan?","A","A. Benazir Bhutto","B. Sheikh Hasina Wazed","C. Hina Rabbani Khar","D. None of the above"],
         ["Which among the following is not a neighboring country of Pakistan?","C","A. China","B. Iran","C. Iraq","D. Afghanistan"],
         ["The famous Badshahi mosque is situated in which city in Pakistan?","C","A. Karachi","B. Islamabad","C. Lahor","D. None of the above"],
         ["Who is known as the 'mother of the nation' of Pakistan?","B","A. Benazir Bhutto","B. Fatima Jinnah","C. Fatima Sughra","D. None of the above"],
         ["How many stanzas are there in Pakistan’s national anthem?","C","A. 1","B. 2","C. 3","D. None of the above"],
         ["What was the old name of PIA?","B","A. Pakistan Airways","B. Orient Airways","C. National Airways","D. None of the above"],
         ["What official name was given to Pakistan in 1956 constitution?","A","A. Islamic Republic Of Pakistan ","B. Republic Of Pakistan","C. The land Of Muslims","D. None of the above"],
         ["Who was the founder of Faraizi Movement in 1802?","D","A. Gajender Singh ","B. Allama Iqbal","C. Sir Syed Ahmed khan","D. Haji Shariatullah"],
         ["What is the meaning of Pakistan?","B","A. Land Of Muslims ","B. Holy Land","C. Islamic Republic of Pakistan","D. None of the above"],
         ["According to population, which is the largest city in Pakistan?","C","A. lahore ","B. Peshawar","C. Karachi","D. None of the above"],
         ]
        b=[]
        u=""
        c=[]
        con=0

        for q in range (5) :

         q=random.choice(a_list)
         con +=1
         print(con,":",q[0])
         print("     ",q[2])
         print("     ",q[3])
         print("     ",q[4])
         print("     ",q[5])
         a=input("\nEnter Your Answer : A , B , C Or D                               .......")
         print("\n")
         u=a.upper()
         c.append(q[1])
         b.append(u)
 
        if (con == 5):
         print("\nThe Correct Answer Is :",c)
         print("You Choose This answer",b,"\n")      
           
        break # Case 1 While Loop Ending
     #Case 1 End

      
      case _ :
               
       print("You Choose Wrong Answer")
       break
        