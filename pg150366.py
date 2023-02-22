class Cell :
    def __init__(self,rc,value) -> None:
        ''' rc : Cell 자신의 row, column
            pcell : 부모Cell
            value : Cell value
        '''
        self.rc = rc
        self.pcell = self
        self.value = value
    
    def is_parent(self) :
        return self is self.pcell
    
    def get_rc(self) :
        return self.rc
    
    def get_parent(self) :
        return self.pcell
    
    def set_parent(self, cell) :
        if cell is None :
            self.pcell = self
        else :
            self.pcell = cell
    
    def __str__(self) -> str:
        return f'me:{self.rc},p:{self.pcell.rc},value:{self.value}'
    
    def get_value(self) :
        return self.value
    
    def set_value(self, value) :
        self.value =  value
    
def find(grid,cell) :
    result = None
    if  cell.is_parent() :
        result =  cell
    else :
        result = find(grid,cell.get_parent())
    return result

def print_grid(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid[0])) :
            print(f'{grid[i][j].get_value():>10} {find(grid,grid[i][j]).get_rc()}',end=',')
        print('\n')

def solution(commands):
    answer = []
    grid = [[Cell((j,i),'EMPTY') for i in range(51)] for j in range(51)]

    for command in commands :
        coms = command.split(' ')
        # print(f'{coms=}')
        if coms[0] == 'UPDATE' and len(coms) ==4:
            r,c = int(coms[1]), int(coms[2])
            pcell = find(grid,grid[r][c])          
            pcell.set_value(coms[3])
        elif coms[0] == 'UPDATE' and len(coms) ==3:    
            for i in range(len(grid)) :
                for j in range(len(grid[0])) :
                    if grid[i][j].get_value() == coms[1] :
                        grid[i][j].set_value(coms[2])
        elif coms[0] == 'MERGE' :
            r1,c1 = int(coms[1]), int(coms[2])
            r2,c2 = int(coms[3]), int(coms[4])
            pcell1 = find(grid,grid[r1][c1])
            pcell2 = find(grid,grid[r2][c2])
            if pcell1 is pcell2 :
                continue
            value = pcell1.get_value() if pcell1.get_value() != 'EMPTY' else pcell2.get_value()
            pcell2.set_parent(pcell1)
            pcell2.set_value('EMPTY')
            pcell1.set_value(value)

        elif coms[0] == 'UNMERGE' :
            r,c = int(coms[1]), int(coms[2])
            pcell = find(grid,grid[r][c])
            value = pcell.get_value()
            unmerge_target = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if pcell is find(grid,grid[i][j])]
            for  t in unmerge_target :
                grid[t[0]][t[1]].set_parent(None)
                grid[t[0]][t[1]].set_value('EMPTY')
            grid[r][c].set_value(value)
        elif coms[0] == 'PRINT' :
            r,c = int(coms[1]), int(coms[2])
            pcell = find(grid,grid[r][c])
            answer.append(pcell.get_value())
        # print_grid(grid)

    return answer

p = ["UPDATE 1 1 menu", "UPDATE 1 2 category"
   , "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean"
   , "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon"
   , "UPDATE 3 2 korean", "UPDATE 3 3 noodle"
   , "UPDATE 3 4 instant", "UPDATE 4 1 pasta"
   , "UPDATE 4 2 italian", "UPDATE 4 3 noodle"
   , "MERGE 1 2 1 3", "MERGE 1 3 1 4"
   , "UPDATE korean hansik", "UPDATE 1 3 group"
   , "UNMERGE 1 4"
   , "PRINT 1 3"
   , "PRINT 1 4"]
# p = ["UPDATE 1 1 a", "UPDATE 1 2 b"
#    , "UPDATE 2 1 c", "UPDATE 2 2 d"
#    , "MERGE 1 1 1 2", "MERGE 2 2 2 1"
#    , "MERGE 2 1 1 1", "PRINT 1 1"
#    , "UNMERGE 2 2", "PRINT 1 1"]

# p =["UPDATE 1 1 A", "UPDATE 2 2 B"
#   , "UPDATE 3 3 C", "UPDATE 4 4 D"
#   , "MERGE 1 1 2 2", "MERGE 3 3 4 4"
#   , "MERGE 1 1 4 4", "UNMERGE 3 3"
#   , "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]
print(solution(p))