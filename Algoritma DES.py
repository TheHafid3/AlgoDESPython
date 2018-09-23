def stringToBinary(stringtext):
    stringlist=list(stringtext)
    binofstring=[]
    for char in stringlist:
        binofstring.append(list(bin(ord(char))))
    for i in range(len(binofstring)):
        binofstring[i].remove('b')      
    return binofstring;

def bin2hex(chain):
    return ''.join((hex(int(chain[i:i+8], 2))[2:] for i in range(0, len(chain), 8)))

def initialPermutationLeft(binary):
    left=[]
    y=1
    x=7
    for i in range(4):
        y=y%8
        for j in range(8):
            x=x%8
            left.append(binary[x][y])
            x=x-1
        y=y+2
        
    return left;

def initialPermutationRight(binary):
    right=[]
    y=0
    x=7
    for i in range(4):
        y=y%8
        for j in range(8):
            x=x%8
            right.append(binary[x][y])
            x=x-1
        y=y+2
    return right;

def Ckey(binary):
    C=[]
    y=0
    x=7
    for i in range(4):
        y=y%7
        for j in range(8):
            if len(C)==28:
                break
            x=x%8
            C.append(binary[x][y])
            x=x-1
        y=y+1
    return C;

def Dkey(binary):
    D=[]
    y=6
    x=7
    for i in range(3):
        y=y%7
        for j in range(8):
            x=x%8
            D.append(binary[x][y])
            x=x-1
        y=y-1
    x=3
    y=3
    for k in range(4):
       x=x%8
       D.append(binary[x][y])
       x=x-1
    return D;

def leftShift(binary, shift):
    binary=binary[shift:]+binary[:shift]
    return binary

def permutationCompression(binary):
    new_binary=[]
    tableofPC=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    for i in range(len(tableofPC)):
        new_binary.append(binary[tableofPC[i]-1])
    return new_binary;

def expansionRight(binary):
    new_binary=[]
    tableofexpansion=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
    for i in range(len(tableofexpansion)):
        new_binary.append(binary[tableofexpansion[i]-1])
    return new_binary;

def sBox(binary):
    sbox1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    sbox2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    sbox3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
    sbox4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
    sbox5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
    sbox6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
    sbox7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
    sbox8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
    sbox=[sbox1,sbox2,sbox3,sbox4,sbox5,sbox6,sbox7,sbox8]
    result=''	
    for i in range(0,len(binary),6):
        tmp = binary[i:i+6]
        row = int(tmp[0]+tmp[5],2)
        col = int(tmp[1]+tmp[2]+tmp[3]+tmp[4],2)
        temp = bin(sbox[int(i/6)][row][col])[2:]
        if(len(temp)==4):
            result+=temp
        else:
            result+=(4-len(temp)%4)*'0'+temp
    return result

def pBox(binary):
    new_binary=['a' for i in range(32)]
    tableofpBox=[16,7,20,21,29,12,28,17,
                 1,15,23,26,5,18,31,10,
                 2,8,24,14,32,27,3,9,
                 19,13,30,6,22,11,4,25]
    for i in range(len(tableofpBox)):
        new_binary[i]=binary[tableofpBox[i]-1]
    return new_binary;

def initialPermutationInvers(binary):
    new_binary=[]
    tableofInvers=[40,8,48,16,56,24,64,32,
                   29,7,47,15,55,23,63,31,
                   38,6,46,14,54,22,52,30,
                   37,5,45,13,53,21,61,29,
                   36,4,44,12,52,20,60,28,
                   35,3,43,11,51,19,59,27,
                   34,2,42,10,50,18,58,26,
                   33,1,41,9,49,17,57,25]
    for i in range(len(tableofInvers)):
        new_binary.append(binary[tableofInvers[i]-1])
    return new_binary;

def roundProcess(right, left, kresult, rounds):
    xorresult=[]
    sboxresult=''
    pbox=''
    new_right=[]
    ipright_expanded=expansionRight(right)
    for i in range(len(ipright_expanded)):
        xorresult.append(str(ord(ipright_expanded[i])^ord(kresult[rounds][i])))
    sboxresult=sBox(xorresult)
    pbox=pBox(sboxresult)
    for i in range(len(pbox)):
        new_right.append(str(int(ord(pbox[i])^ord(left[i]))))
    return new_right;    

plaintext = input("Masukkan plaintext (8 karakter): ")
key = input("Masukkan keyword (8 karakter): ")


binofkey=[]
binofkey = stringToBinary(key)
ckey = Ckey(binofkey)
dkey = Dkey(binofkey)
shift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
kkey=[]
for i in range(16):
    ckey=leftShift(ckey,shift[i])
    dkey=leftShift(dkey,shift[i])
    CDkey=ckey+dkey
    kkey.append(permutationCompression(CDkey))


binofplain=[]
binofplain = stringToBinary(plaintext)
ipleft = initialPermutationLeft(binofplain)
ipright = initialPermutationRight(binofplain)
tmp=[]
ipgabungan=[]

for i in range(16):
    tmp=roundProcess(ipright, ipleft, kkey, i)
    ipleft=ipright
    ipright=tmp

ipgabungan=ipright+ipleft
binofcipher=initialPermutationInvers(ipgabungan)
ciphertext=''.join(binofcipher)

print('Ciphertext dalam biner: ', ciphertext)
print ("Ciphertext hex encoded: "+ bin2hex(ciphertext))
