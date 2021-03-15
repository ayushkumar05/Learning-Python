def drawboard():
    print('__|__|__');print('__|__|__');print('  |  |  ');print();print('format is');print();print('1   2   3 ');print('4   5   6 ');print('7   8   9 ')
def end():
        ply = input('if you want to play again enter y ')
        if ply == 'y':
            tictactoe()        
def tictactoe():
    drawboard()
    x = 0
    def checkboard1():
        if inputar1[0] == inputar1[1] and inputar1[1] == inputar1[2] and inputar1[2] =='X':
            print(inputar1[0],'wins') 
            end()
        if inputar2[0] == inputar2[1] and inputar2[1] == inputar2[2] and inputar2[0] =='X':
            print(inputar2[0],'wins')
            end()   
        if inputar3[0] == inputar3[1] and inputar3[1] == inputar3[2] and inputar3[1] =='X':
            print(inputar3[0],'wins')
            end()
        if inputar1[0] == inputar2[1] and inputar2[1] == inputar3[2] and inputar1[0] =='X':
            print(inputar1[0],'wins')
            end()
        if inputar1[1] == inputar2[1] and inputar2[1] == inputar3[1] and inputar1[1] =='X':
            print(inputar1[1],'wins')
            end()
        if inputar1[0] == inputar2[0] and inputar2[0] == inputar3[0] and inputar2[0] =='X':
            print(inputar1[0],'wins')
            end()
        if inputar1[2] == inputar2[2] and inputar2[2] == inputar3[2] and inputar1[2] =='X':
            print(inputar1[2],'wins')
            end()
        if inputar1[2] == inputar2[1] and inputar2[1] == inputar3[0] and inputar1[2] =='X':
            print(inputar1[2],'wins')
            end()

    def checkboard2():
        if inputar1[0] == inputar1[1] and inputar1[1] == inputar1[2] and inputar1[2] =='O':
            print(inputar1[0],'wins') 
            end()
        if inputar2[0] == inputar2[1] and inputar2[1] == inputar2[2] and inputar2[0] =='O':
            print(inputar2[0],'wins')
            end()       
        if inputar3[0] == inputar3[1] and inputar3[1] == inputar3[2] and inputar3[1] =='O':
            print(inputar3[0],'wins')
            end()
        if inputar1[0] == inputar2[1] and inputar2[1] == inputar3[2] and inputar1[0] =='O':
            print(inputar1[0],'wins')
            end()

        if inputar1[1] == inputar2[1] and inputar2[1] == inputar3[1] and inputar1[1] =='O':
            print(inputar1[1],'wins')
            end()
        if inputar1[0] == inputar2[0] and inputar2[0] == inputar3[0] and inputar2[0] =='O':
            print(inputar1[0],'wins')
            end()
        if inputar1[2] == inputar2[2] and inputar2[2] == inputar3[2] and inputar1[2] =='O':
            print(inputar1[2],'wins')
            end()
        if inputar1[2] == inputar2[1] and inputar2[1] == inputar3[0] and inputar1[2] =='O':
            print(inputar1[2],'wins')
            end()
    def turn1():
        player1input = int(input('enter your selection,an x will be placed there'))
        if player1input >=0 and player1input<=3:
            if  inputar1[(player1input-1)] != 'X' and inputar1[(player1input-1)] != 'O' :
                inputar1[(player1input-1)] = 'X'
            else:
                print('you cant go there')
                turn1()
        elif player1input >=4 and player1input<=6:
            if inputar2[(player1input-4)] != 'X' and inputar2[(player1input-4)] != 'O':
                inputar2[(player1input-4)] = 'X'
            else: 
                print('you cant go there')
                turn1()
        elif player1input >=7 and player1input<=9:
            #if inputar3[player1input-7] == 'X' and inputar3[player1input-7] != 'O':
            inputar3[player1input-7] = 'X'
            '''else:
                print('you cant go there')
                turn1()
               ''' 
        print(inputar1[0],'|',inputar1[1],'|',inputar1[2]);print('----------');print(inputar2[0],'|',inputar2[1],'|',inputar2[2]);print('----------');print(inputar3[0],'|',inputar3[1],'|',inputar3[2]);print('_________________________')
    def turn2():
        player2input = int(input('enter your selection,an O will be placed there'))  
        if player2input >=0 and player2input<=3:
            if inputar1[(player2input-1)] != 'O' and inputar1[(player2input-1)] != 'X':
                 inputar1[(player2input-1)] = 'O'
            else:
                print('you cant go there')
                turn2()      
        elif player2input >=4 and player2input<=6:
            if inputar2[(player2input-4)] != 'O' and inputar2[(player2input-4)] != 'X':
                inputar2[(player2input-4)] = 'O'
            else:
                print('you cant go there')
                turn2()
        elif player2input >=7 and player2input<=9:
            #if inputar3[player2input-7] != 'O' and inputar3[player2input-7] != 'X':
            inputar3[player2input-7] = 'O'
            '''else:
                print('you cant go there')
                turn2()
                '''
        print(inputar1[0],'|',inputar1[1],'|',inputar1[2]);print('----------');print(inputar2[0],'|',inputar2[1],'|',inputar2[2]);print('----------');print(inputar3[0],'|',inputar3[1],'|',inputar3[2]);print('_________________________')
    inputar1 = [ ' ',' ' , ' ' ];inputar2 = [ ' ', ' ', ' '];inputar3 = [ ' ',' ' ,' ' ]
    while x!=1:
        checkboard1();checkboard2();turn1();checkboard1();checkboard2();turn2()
tictactoe()

    
    
