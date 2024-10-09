
def chto(x,y,board):
    return 0<=x<8 and 0<=y<8 and board[x][y]==0
def sortedmoves(moves):
    sortmov=[]
    for i in range(8, 0,-1):
        for move in moves:
            if move[2]==i:
                sortmov.append(move)
    return sortmov

def knight_move(x,y,board):
    vozmoj_hodi_konia=[]
    moves=[(1,2),(1,-2),(-1,2),(-1,2),(2,1),
           (2,-1),(-2,1),(-2,-1)]
    for i in moves:
        new_x, new_y =x+ i[0],y+ i[1]
        if chto(new_x,new_y, board):
            count=sum(1 for n in moves if chto(new_x+n[0], 
                                               new_y+n[1],board))
            vozmoj_hodi_konia.append((new_x, new_y,count))
    return sortedmoves(vozmoj_hodi_konia)

board = [[0 for l in range(8)] for q in range(8)]
print(knight_move(x=0,y=6,board=board))



def m_k_t(x,y,board,count):  
    if count==64:
        return board
    for i in knight_move(3,4,board):
        new_x=i[0]
        new_y=i[1]
        board[i[0]][i[1]]=count
        if (m_k_t(new_x,new_y)):
            return True
        board[i[0]][i[1]]=0
        return False
    

