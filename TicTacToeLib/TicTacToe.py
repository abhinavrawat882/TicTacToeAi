#1==x
#0==o
class TicTacToe:
    def __init__(self,fp):
        self.board=[[2,2,2],[2,2,2],[2,2,2]]
        if(fp=='x'):
            self.currentPlayer=1
        else:
            self.currentPlayer=0
        self.noOfMoves=0
        self.row=[[2,2,2],[0,0,0]]
        self.column=[[2,2,2],[0,0,0]]
        self.rd=[2,0]
        self.ld=[2,0]

        
        

    def nextPlay(self,x,y):
        if(noOfMoves<9):
            np=self.currentPlayer
            if(self.currentPlayer==1 and self.board==2):
                self.board[x][y]='x'
                self.currentPlayer=0
            elif(self.currentPlayer==0 and self.board==2)):
                self.board[x][y]='o'
                self.currentPlayer=1
            self.noOfMoves+=1

            
            #update row status 
            if(self.row[0][x]!=-1):##-1 means that that row can not be won as there are 2 or more moves on the row by two different players


                ##first case that that row only has your moves in it
                if self.row[0][x]==self.np:
                    self.row[1][x]+=1



                ##Second case the row has other players move making it imposible to win in that row
                elif self.row[0][x]==self.currentPlayer:
                    self.row[0][x]=-1
                    #this means that that row can be skipped while checking for a win
               
                #third the row was empty so its can be won and you will mark it with your name               
                else:

                    self.row[0][x]=np
                    #mark it with your name
                    ##thn add the no of moves to the board making it one
                    self.row[1][x]=1
            
            #Update column status
            if(self.column[0][y]!=-1):


                if self.column[0][y]==self.np:
                    self.column[0][y]+=1


                elif self.column[0][y]==self.currentPlayer:
                    self.column[0][y]=-1

                else:

                    self.column[0][y]=np
                    
                    self.column[0][y]=1

            #move on to right diagonal 
            if self.rd[0]!=-1 and x==y:
                if self.rd[0]==np:
                    self.rd[1]+=1


                elif self.rd[0]==self.currentPlayer:
                    self.rd[1]=-1

                else:

                    self.rd[1]=np
                    
                    self.rd[1]=1

            #move on to right diagonal 
            if self.ld[0]!=-1 and y==2-x:
                if self.ld[0]==np:
                    self.ld[1]+=1


                elif self.ld[0]==self.currentPlayer:
                    self.ld[1]=-1

                else:

                    self.ld[1]=np
                    
                    self.ld[1]=1

                


    
    def copyBoard(self):
        newob=TicTacToe()
        for i in range(3):
            for y in range(3):
                newob.board[i][y]=self.board[i][y]
        
        newob.currentPlayer=self.currentPlayer
        
        newob.noOfMoves=self.noOfMoves
        return(newob)
    
    def getVal(self,x,y):
        return(self.board[x][y])

    def whoWon(self):
        ##tells if any one won or not




class minimax:

def minimaxgenerator(boardob,compp):
    ##gets 2 values the board object and which one is computer
     



    
            
