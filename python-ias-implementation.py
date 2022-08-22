
memory = list(range(1, 1000))  # this would be our memory array


def assembler(x='', y=''):  # returns the 40 bit instruction

    z = x.split()
    p = y.split()
    
    # Load
    if ('Load' in z and len(z)==2 and z[1][0:2]!='MQ'):
        # if the Load is intiated, a binary address is created of that decimal number(the memory location)
        address = str(bin(int(z[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):  # we need to make the address 12 bit wide
            zeros = zeros+'0'

        address = zeros + address
        opcode = '00000001'
        LHS = opcode+address  # final LHS/RHS is opcode+address

    # Same procedure is followed for generating the LHS and RHS instructions for other commands

    #Load MQ, M[X]
    if ('Load' and 'MQ,' in z):
        address = str(bin(int(z[2][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):  
            zeros = zeros+'0'

        address = zeros + address
        opcode = '00001001'
        LHS = opcode+address 
        
    
    #Load MQ
    if (z[0] == 'Load' and z[1] == 'MQ'):

        LHS = "00001010"+"0"*12

    if ('Load' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'

        address1 = zeros + address1
        opcode1 = '00000001'
        RHS = opcode1+address1
        

    # Stor 
    if ('Stor' in z):
        address = str(bin(int(z[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):
            zeros = zeros+'0'
        address = zeros + address
        opcode = '00100001'
        LHS = opcode+address
        
    #Stor RHS
    if ('Stor' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'
        address1 = zeros + address1
        opcode1 = '00100001'
        RHS = opcode1+address1


    # Add RHS
    if ('Add' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'

        address1 = zeros + address1
        opcode1 = '00000101'
        RHS = opcode1+address1

    if ('Add' in z):
        address = str(bin(int(z[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):
            zeros = zeros+'0'

        address = zeros + address
        opcode = '00000101'
        LHS = opcode+address

    # Sub
    if ('Sub' in z):
        address = str(bin(int(z[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):
            zeros = zeros+'0'

        address = zeros + address
        opcode = '00000110'
        LHS = opcode+address

    #sub RHS
    if ('Sub' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'

        address1 = zeros + address1
        opcode1 = '00000110'
        RHS = opcode1+address1
        
    #Div
    if ('Div' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'

        address1 = zeros + address1
        opcode1 = '00001100'
        RHS = opcode1+address1

    #MUL
    if ('Mul' in p):
        address1 = str(bin(int(p[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address1), 12):
            zeros = zeros+'0'

        address1 = zeros + address1
        opcode1 = '00001011'
        RHS = opcode1+address1

    if ('Mul' in z):
        address = str(bin(int(z[1][2:4])).replace("0b", ""))
        zeros = ''
        for i in range(len(address), 12):
            zeros = zeros+'0'

        address = zeros + address
        opcode = '00001011'
        LHS = opcode+address

    if (p == []):
        final = LHS+'00000000000000000000'
        return final
    if (z == []):
        final = RHS+'00000000000000000000'
        return final

    final = LHS+RHS  # final store is the 40 bit address (LHS+RHS)
    return final


'''
     00000000; --> HALT
     00001010; --> LOAD MQ
     00001001; --> LOAD MQ,M(X)
     00100001; --> STOR M(X)
     00000001; --> LOAD M(X)
     00000010; --> LOAD -M(X)
     00000011; --> LOAD|M(X)|
     00000100; --> -LOAD|M(X)|
     00001101; --> JUMP M(X,0:19)
     00001110; --> JUMP M(X,10:39)
     00001111; --> JUMP + M(X,0:19)
     00010000; --> JUMP + M(X,20:39)
     00000101; --> ADD M(X)
     00000111; --> ADD |M(X)|
     00000110; --> SUB M(X)
     00001000; --> SUB |M(X)|
     00001011; --> MUL M(X)
     00001100; --> DIV M(X)
     00010100; --> LSH
     00010101; --> RSH
'''
AC = 0
PC = 0
MQ = 0


def compute(x):  # this function contains the fetch and execute cycle
    global AC   #defining the global variables
    global PC   
    global MQ
    MAR = PC 
    MBR = x
    IBR = MBR[20:40]
    IR = MBR[0:8]
    MAR = MBR[8:20]

    # Stor LHS
    if (x[0:8] == '00100001'):
        MBR = AC
        memory[(int(MAR, 2))] = MBR

    # Load LHS
    if (x[0:8] == '00000001'):
        MBR = memory[(int(MAR, 2))]
        AC = MBR

    # Add LHS
    if (x[0:8] == '00000101'):
        MBR = memory[(int(MAR, 2))]
        AC = AC+MBR

    # Sub LHS
    if (x[0:8] == '00000110'):
        MBR = memory[(int(MAR, 2))]
        AC = AC-MBR

    # Load MQ, MQ[X]
    if(x[0:8] == '00001001'):
        MQ = memory[(int(MAR, 2))]

    # Load MQ
    if (x[0:8] == '00001010'):
        
        AC = MQ

    # ADD RHS
    if (x[20:28] == '00000101'):
        IR = IBR[0:8]
        MAR = IBR[8:20]
        PC = PC+1
        MBR = memory[(int(MAR, 2))]
        AC = AC+MBR

    # Store RHS
    if (x[20:28] == '00100001'):
        IR = IBR[0:8]
        MAR = IBR[8:20]
        PC = PC+1
        MBR = AC
        memory[(int(MAR, 2))] = MBR

    # Sub #RHS
    if (x[20:28] == '00000110'):
        IR = IBR[0:8]
        MAR = IBR[8:20]
        PC = PC+1
        MBR = memory[(int(MAR, 2))]
        AC = AC-MBR

    # Div RHS
    if (x[20:28] == '00001100'):
        IR = IBR[0:8]
        MAR = IBR[8:20]
        PC = PC+1
        MBR = memory[(int(MAR, 2))]
        MQ = AC//MBR
        AC = AC % MBR

     # Mul RHS
    if (x[20:28] == '00001011'):
        IR = IBR[0:8]

        MAR = IBR[8:20]
        PC = PC+1
        MBR = memory[(int(MAR, 2))]
        z = (bin(MQ*MBR).replace("0b", ''))
        zeros = ''
        for i in range(len(z), 80):
            zeros = zeros+'0'
        z = zeros+z
        AC = int(z[0:40], 2)
        MQ = int(z[40:80], 2)
        
        

    # Halt
    if (x[20:28] == '00000000'):
        PC = PC + 1
        return


x = int(input('What is your choice? :\n 1) Addition of two numbers\n 2) Subtraction of two numbers\n 3) Alternate Sum and DIfference of 9 numbers\n 4) Division of two numbers\n 5) Average of 7 numbers\n 6) Multiplication of two numbers\n 7)Area and Perimeter of a rectangle or a square\n'))


# Simple addition
if (x == 1):
    y = int(input('Enter first number: '))
    z = int(input('Enter second number: '))

    memory[50] = y
    memory[51] = z

    memory[0] = assembler('Load M[50]', 'Add M[51]')  # 40bits of inst
    memory[1] = assembler('Stor M[52]')
    compute(memory[0])
    compute(memory[1])
    print(f'the sum is {memory[52]}')

# Simple subtraction
if(x == 2):
    y = int(input('Enter first number: '))
    z = int(input('Enter second number: '))

    memory[50] = y
    memory[51] = z

    memory[0] = assembler('Load M[50]', 'Sub M[51]')
    memory[1] = assembler('Stor M[52]')
    compute(memory[0])
    compute(memory[1])
    print(f'the difference is = {memory[52]}')

# sum and difference of 9 numbers
if (x == 3):
    print("Enter the 9 integers in a single line - ")
    l = [int(i) for i in input().split()]
    memory[50] = l[0]
    memory[51] = l[1]
    memory[52] = l[2]
    memory[53] = l[3]
    memory[54] = l[4]
    memory[55] = l[5]
    memory[56] = l[6]
    memory[57] = l[7]
    memory[58] = l[8]

    memory[0] = assembler('Load M[50]', 'Sub M[51]')
    memory[1] = assembler('Add M[52]', 'Sub M[53]')
    memory[2] = assembler('Add M[54]', 'Sub M[55]')
    memory[3] = assembler('Add M[56]', 'Sub M[57]')
    memory[4] = assembler('Add M[58]', 'Stor M[59]')

    compute(memory[0])
    compute(memory[1])
    compute(memory[2])
    compute(memory[3])
    compute(memory[4])

    print(f'the output is = {memory[59]}')

# Division of two numbers
if (x == 4):
    y = int(input('Enter first number: '))
    z = int(input('Enter second number: '))

    memory[50] = y
    memory[51] = z

    memory[0] = assembler('Load M[50]', 'Div M[51]')
    memory[1] = assembler('Load MQ', 'Stor M[52]')
    compute(memory[0])
    compute(memory[1])
    print(f'quotient = {memory[52]}')

# average of 7 numbers
if (x == 5):
    print("Enter the 7 integers in a single line - ")
    l = [int(i) for i in input().split()]
    memory[50] = l[0]
    memory[51] = l[1]
    memory[52] = l[2]
    memory[53] = l[3]
    memory[54] = l[4]
    memory[55] = l[5]
    memory[56] = l[6]
    memory[57] = 7

    memory[0] = assembler('Load M[50]', 'Add M[51]')
    memory[1] = assembler('Add M[52]', 'Add M[53]')
    memory[2] = assembler('Add M[54]', 'Add M[55]')
    memory[3] = assembler('Add M[56]', 'Stor M[60]')
    memory[4] = assembler('Load MQ, M[60]', 'Div M[57]')
    memory[5] = assembler('Load MQ', 'Stor M[58]')
    compute(memory[0])
    compute(memory[1])
    compute(memory[2])
    compute(memory[3])
    compute(memory[4])
    compute(memory[5])
    # average rounded off to nearest integer
    print(f'average is = {memory[58]}')

# mul
if (x == 6):
    y = int(input('Enter first number: '))
    z = int(input('Enter second number: '))

    memory[50] = y
    memory[51] = z

    memory[0] = assembler('Load MQ, M[50]', 'Mul M[51]')
    memory[1] = assembler('Load MQ','Stor M[52]') 
    compute(memory[0])
    compute(memory[1])
    
    print(f'product is = {memory[52]}')

# calculating area and perimeter of a rectangle/square
if (x == 7):
    y = int(input('Enter the length of first side: '))
    z = int(input('Enter the length of second side: '))
    a = y
    b = z

    memory[50] = y
    memory[51] = z
    memory[60] = a
    memory[61] = b

    memory[0] = assembler('Load MQ, M[50]', 'Mul M[51]')
    memory[1] = assembler('Load MQ','Stor M[52]')
    compute(memory[0])
    compute(memory[1])
    print(f"Area = {memory[52]}")
    memory[2] = assembler('Load M[60]', 'Add M[61]')
    memory[3] = assembler('Add M[60]', 'Add M[61]')
    memory[4] = assembler('Stor M[63]')
    compute(memory[2])
    compute(memory[3])
    compute(memory[4])

    print(f"Perimeter = {memory[63]}")
