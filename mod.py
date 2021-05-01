class TicTacToe():
    
    grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def __init__(self):
        pass


    def welcome_message(self):
        print("""
 _________                               _________                                   _________
|_________| ______   _______            |_________|     ___       _______           |_________| ________    ______
    | |    |______| | ______|               | |        // \\\     |  _____|              | |    |  ____  |  | _____|
    | |       ||    | |         _____       | |       //   \\\    | |         _____      | |    | |    | |  | |____
    | |       ||    | |        |_____|      | |      //_____\\\   | |        |_____|     | |    | |    | |  |  ____|
    | |     __||__  | |_____                | |     //-------\\\  | |_____               | |    | |____| |  | |_____
    |_|    |______| |_______|               |_|    //         \\\ |_______|              |_|    |________|  |______|
        








Welcome to the Tic-Tac-Toe Game!!""" + '\n')


    def reference_key(self):
        print('''Following is the reference key for the game grid-
        
        -------------
        | 1 | 2 | 3 |
        -------------
        | 4 | 5 | 6 |
        -------------
        | 7 | 8 | 9 |
        -------------
        
        ''')


    def game_grid(self):

        for _ in range(48):
            print()

        

        print('''
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        ''')

    
    def player(self,name,character):

        self.name = name
        self.character = character

        return [self.name,self.character]
    
    
    def gameplay(self,box,character):

        self.box = box
        self.character = character

    
        if self.box in [1,2,3]:
            if self.grid[0][self.box - 1] != ' ':
                print('The box has already been used, choose another box')
                print()
                
                result = 0
            
            else:
                self.grid[0][self.box - 1] = self.character
                
                for _ in range(50):
                    print()
                
                print(f'''
        -------------
        | {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} |
        -------------
        | {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} |
        -------------
        | {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} |
        -------------
        ''')
                
                result = 1


        elif self.box in [4,5,6]:
            if self.grid[1][self.box - 4] != ' ':
                print('The box has already been used, choose another box')
                print()

                result = 0

            else:
                self.grid[1][self.box - 4] = self.character
                
                for _ in range(50):
                    print()
                
                print(f'''
        -------------
        | {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} |
        -------------
        | {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} |
        -------------
        | {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} |
        -------------
        ''')

                result = 1


        elif self.box in [7,8,9]:
            if self.grid[2][self.box -7] != ' ':
                print('The box has already been used, choose another box')
                print()
                result = 0

            else:
                self.grid[2][self.box - 7] = self.character
                
                for _ in range(50):
                    print()
                
                print(f'''
        -------------
        | {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} |
        -------------
        | {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} |
        -------------
        | {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} |
        -------------
        ''')

                result = 1

        else:
            print("Invalid box chosen, try again")
            print()
            result = 0
        
        return result
                
    def winner_check(self):
        if self.grid == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]:
            return (0,'Initialize')
        
        elif self.grid[0][0] == self.grid[1][0] and self.grid[1][0] == self.grid[2][0] and self.grid[2][0] != ' ':
            return (1,self.grid[0][0])
        
        elif self.grid[0][1] == self.grid[1][1] and self.grid[1][1] == self.grid[2][1] and self.grid[2][1] != ' ':
            return (1,self.grid[0][1])
        
        elif self.grid[0][2] == self.grid[1][2] and self.grid[1][2] == self.grid[2][2] and self.grid[2][2] != ' ':
            return (1,self.grid[0][2])
        
        elif self.grid[0][0] == self.grid[0][1] and self.grid[0][1] == self.grid[0][2] and self.grid[0][2] != ' ':
            return (1,self.grid[0][0])
        
        elif self.grid[1][0] == self.grid[1][1] and self.grid[1][1] == self.grid[1][2] and self.grid[1][2] != ' ':
            return (1,self.grid[1][0])
        
        elif self.grid[2][0] == self.grid[2][1] and self.grid[2][1] == self.grid[2][2] and self.grid[2][2] != ' ':
            return (1,self.grid[2][0])
        
        elif self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2] and self.grid[2][2] != ' ':
            return (1,self.grid[0][0])
        
        elif self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0] and self.grid[2][0] != ' ':
            return (1,self.grid[0][2])

        elif self.grid[0][0] != ' ' or self.grid[0][1] != ' ' or self.grid[0][2] != ' ' or self.grid[1][0] != ' ' or self.grid[1][1] != ' 'or self.grid[1][2] != ' 'or self.grid[2][0] != ' ' or self.grid[2][1] != ' ' or self.grid[2][2] != ' ':
            return (2,'tie')   