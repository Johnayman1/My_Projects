# File   : CS112_A1_T2_1_20230109.py
#purpose : Two players starts from 0 and alternatively add a number from 1 - 10 to the sum . The player who reaches 100 first wins
# Author : John ayman demian 
# ID : 20230109 
 
# set the counter
score = 0 

# put valids numbers 
valid_numbers=[1,2,3,4,5,6,7,8,9,10]

# welcome message 
print("Welcom to 100 game ")

# Game play 
while score < 100 :
    print("player 1 ")
  #check input validaiton
    while True: 
       choice = input("please select any number 1 - 10 : ")
       if choice.isdigit():
        choice = int(choice)
        if choice in valid_numbers:
         score += choice
         # If score exceeds 100
         if score> 100:
            score = score - score % 100
         print(f"SCORE NOW  = ",score)
         break
        else:
          continue  
    # show winning message      
    if score==100 :
        print("player 1 wins")
        break 
    else :
      print("player 2")
      while True: 
          choice = input("please select any number 1 - 10 : ")
          if choice.isdigit():
           choice = int(choice)
           if choice in valid_numbers:
            score += choice
            if score> 100:
                score = score - score % 100
            print(f"SCORE NOW  = ",score)
            break
          else:
            continue     
      if score==100 :
        print("player 2 wins")
        break 
  
   
    
    

   
    

    


       
   