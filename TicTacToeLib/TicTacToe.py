#1==x
#0==o
class TicTacToe:
    def __init__(self,fp):
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
        if(fp=='x'):
            self.currentPlayer=1
        else:
            self.currentPlayer=0
        self.noOfMoves=0
        

    def nextPlay(self,x,y):
        if(noOfMoves<9):
            if(self.currentPlayer==1):
                self.board[x][y]='x'
                self.currentPlayer=0
            else:
                self.board[x][y]='o'
                self.currentPlayer=1
            self.noOfMoves+=1
    
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



def minimaxgenerator()

    
            
