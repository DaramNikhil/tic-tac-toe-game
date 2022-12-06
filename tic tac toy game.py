board=["" for i in range(10)]
import random,time,sys
n=[j for j in range(1,10)]
#print "board"
def print_board():
    row1="|   {}   |   {}   |   {}   |".format(board[1],board[2],board[3])
    row2="|   {}   |   {}   |   {}   |".format(board[4],board[5],board[6])
    row3="|   {}   |   {}   |   {}   |".format(board[7],board[8],board[9])
    
    print(row1)
    print(row2)
    print(row3)
     
def player_mode(icon):
    user=int(input("Enter number(1-9)"))
    if user<=9 and user>0:
        if board[user]=="":
            board[user]=icon
        else:
            print("place was taken")
            player_mode(icon)
    else:
       print("Enter valid number")
       player_mode()
       
                        
def computer_mode(icon):
        n1=random.choice(n)
        print(n1)  
        if board[n1]=="":
            board[n1]=icon
        else:
            print("place was taken")
            computer_mode(icon)

def player_vin():
    if(board[1]=="X" and board[2]=="X" and board[3]=="X") or\
    (board[4]=="X" and board[5]=="X" and board[6]=="X") or\
    (board[7]=="X" and board[8]=="X" and board[9]=="X") or\
    (board[2]=="X" and board[5]=="X" and board[8]=="X") or\
    (board[3]=="X" and board[6]=="X" and board[9]=="X") or\
    (board[1]=="X" and board[5]=="X" and board[9]=="X") or\
    (board[3]=="X" and board[5]=="X" and board[7]=="X"):   
        return True
    else:
        return False

def computer_vin():
    if(board[1]=="O" and board[2]=="O" and board[3]=="O") or\
    (board[4]=="O" and board[5]=="O" and board[6]=="O") or\
    (board[7]=="O" and board[8]=="O" and board[9]=="O") or\
    (board[2]=="O" and board[5]=="O" and board[8]=="O") or\
    (board[3]=="O" and board[6]=="O" and board[9]=="O") or\
    (board[1]=="O" and board[5]=="O" and board[9]=="O") or\
    (board[3]=="O" and board[5]=="O" and board[7]=="O"):
        return True
    else:
        return False
    

def draw():
    if "" not in board:
        return True   
    else:
        return False    


while True:        
    num=int(input("1.player vs computer: "))
    if num==1:
       while True:
           print_board()
           player_mode("X")
           print_board()
           if player_vin():
               print("player (X) win... congratulations")
               sys.exit()
           elif draw():
               print("it's draw")
               sys.exit()
           print("-------------")
           computer_mode("O")
           time.sleep(1)
           if computer_vin():
               print("player(O) win.... congratulations")
               sys.exit()
           elif draw():
               print("it's draw")
               sys.exit()
     
       
            
            
       
            
        
          
             
              
              
        


              