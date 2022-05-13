def nfa (state , index):
    if index==len (string):
        if state=='q2':
            return True
        else:
            return False
    #___________________________________________________________________         
    if state=='q0'and string[index]=='a':
        if nfa('q0',index+1)==True:
            return True
    if state=='q0':
        if nfa('q1',index)==True:
            return True
    if state=='q1'and string[index]=='a':
        if nfa('q3',index+1)==True:
            return True    
    if state=='q1':
        if nfa('q2',index)==True:
            return True   
    if state=='q2'and string[index]=='a':
        if nfa('q2',index+1)==True:
            return True 
    if state=='q3'and string[index]=='b':
        if nfa('q1',index+1)==True:
            return True
    #___________________________________________________________________        
    return False
string =input()
if nfa('q0',0)==True:
    print('accept')
else:
    print('reject')