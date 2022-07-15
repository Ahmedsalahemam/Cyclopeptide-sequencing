weightsFile = open("weight.txt")
weightREF = {}
mp={}
for f in weightsFile:
    line = f.rstrip()
    words = line.split(" ")
    aa = words[0]
    w = int(words[1])
    weightREF[w] = aa
    mp[aa] = w


inputList = [0, 97, 97, 99, 101,
             103, 196, 198, 200,
             202, 295, 297, 299,
             299, 301, 394, 396,
             398, 400, 400, 497]

# scanning the list
stlist = []  ##  the list contains 1 mers
for i in inputList:       # generate initial list
    keyamino = i
    if keyamino in weightREF:      #check if weight in input list is in our weight dictionary
        stlist.append(weightREF[keyamino])

def retu(summ):        # check if sum of weights of mers is in input list return 1
    return summ in inputList

def Is_Consistent(str):
    for i in range(1,len(str)+1):
        for j in range(0, len(str)):
            sum = 0
            if j+i <= len(str):
                s = str[j:j+i]  # generate substrings of mers to check their sum if in the input list
                for k in s :
                    sum += mp[k]  # calculate sum of weights of amino acids
                if retu(sum) == 0:
                    return 0

    return 1

valled = {}
def lsp(sl):# Generate subsets
    nl = sl  ## nl is the list I update mers in it
    sublist = ""
    inilist = []  ##   the list i put the 2 mers uptil the length of sequence and i clear it
    finallist = []  ##  the list contains all mers of sequence
    for k in range(len(sl)-1):  ##from 1 mers to the length of sequence
        for i in range(len(nl)): # combination of letters of sequence  assume ln= pv,vc,pc,pp  |   sl = p ,v ,c ,t
            for j in range(len(sl)):
                sublist += (nl[i])
                sublist += (sl[j])
                if Is_Consistent(sublist):   # check if mers is consistent then put it in our list
                    Is_Consistent(sublist)
                    inilist.append(sublist)
                sublist = ""
        finallist.append(inilist)
        nl = inilist
        inilist = []
    return finallist

f_list = lsp(stlist)
print(f_list)

#for i in f_list:
 #   for j in i:
  #      if Is_Consistent(j) == 0:
   #        i.remove(j)

#print(i)
#for i in range(len(f_list)):
 #   for j in range(len(f_list[i])):
  #      if Is_Consistent(f_list[i][j]) == 0:
   #        f_list[i].remove(f_list[i][j])