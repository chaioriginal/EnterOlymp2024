
def chto(x,y,board):
    return 0<=x<8 and 0<=y<8 and board[x][y]==0
def knight_move(x,y,board):
    vozmoj_hodi_konia=[]
    moves=[(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),
           (y+1,x+2),(y+1,x-2),(y-1,x+2),(y-1,x-2)]
    for i in moves:
        new_x, new_y = i[0], i[1]
        if chto(new_x,new_y, board):
            #count=sum(i for n in moves if chto(n,board))
            vozmoj_hodi_konia.append(i)
    return vozmoj_hodi_konia
board = [[0 for l in range(8)] for q in range(8)]
print(knight_move(x=3,y=4,board=board))
def sorted()
def m_k_t(x,y,board,count):  
    if count==64:
        return board
    for i in knight_move(3,4,board):
        board[i[0]][i[1]]=count
        if (m_k_t()):
            return True
        board[i[0]][i[1]]=0
        return False
    

