#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ initializes the Board object using 2 attributes height and width
        """
        self.height = height
        self.width = width
        self.slots = [[' ']*self.width for r in range(self.height)] 


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for col in range(self.width):
            s+= '--'
        s += '-'
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col%10) 
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = self.height-1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker
             
            
    
    ### add your reset method here ###
    def reset(self):
        """ should reset the Board object on which it is called by setting 
                all slots to contain a space character.
        """
        self.slots = [[' ']*self.width for r in range(self.height)] 
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the 
            column col on the calling Board object. Otherwise,
            it should return False.
        """
        if col < 0 or col > self.width-1:
            return False
        else:
            for x in range(0, self.height):
                if self.slots[x][col] == ' ':
                    return True
                else:
                    return False
                
    
    def is_full(self):
        """ returns True if the called Board object is completely 
            full of checkers, and returns False otherwise
        """
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.slots[x][y] == ' ':
                    return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
            object. If the column is empty, then the method should do nothing
        """
        row = 0
        n = 0
        while n == 0:
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                n += 1
            elif row == self.height-1:
                n += 1
            else:
                row += 1
    
                
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for a specific checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
    
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a downsloping diagonal win for a specific checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        return True
    
        return False
    
    
    def is_up_diagonal_win(self, checker):
        """ Checks for an upsloping diagonal win for a specific checker.
        """
        for row in range(self.height - 3):
            for col in range(3, self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col - 1] == checker and \
                    self.slots[row + 2][col - 2] == checker and \
                    self.slots[row + 3][col - 3] == checker:
                        return True
    
        return False
    
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O',
            and returns True if there are four consecutive slots containing
            checker on the board. Otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
        horiz = self.is_horizontal_win(checker)
        vert = self.is_vertical_win(checker)
        updiag = self.is_up_diagonal_win(checker)
        downdiag = self.is_down_diagonal_win(checker)
        
        if horiz == True or vert == True or updiag == True or downdiag == True:
            return True
        else:
            return False
         
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
