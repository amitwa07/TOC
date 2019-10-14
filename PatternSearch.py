NO_OF_CHARS = 256

def main(): 
    Text = input("Enter Text : ")
    Pattern = input("Enter Pattern : ")
    search(Pattern, Text) 

def search(Pattern, Text): 
    global NO_OF_CHARS 
    M = len(Pattern) 
    N = len(Text) 
    TF = computeTF(Pattern, M)   

    # Process Text over FA. 
    state=0
    for i in range(N): 
        state = TF[state][ord(Text[i])] 
        if state == M: 
            print("Pattern found at index: {}". 
                format(i-M+1)) 

def computeTF(Pattern, M): 
    global NO_OF_CHARS 

    TF = [[0 for i in range(NO_OF_CHARS)] 
        for _ in range(M+1)] 

    for state in range(M+1): 
        for x in range(NO_OF_CHARS): 
            z = getNextState(Pattern, M, state, x) 
            TF[state][x] = z 

    return TF 

def getNextState(Pattern, M, state, x): 
    if state < M and x == ord(Pattern[state]): 
        return state+1

    i=0
    for ns in range(state,0,-1):# ns store next state and give longest preffix 
        if ord(Pattern[ns-1]) == x: 
            while(i<ns-1): 
                if Pattern[i] != Pattern[state-ns+1+i]: 
                    break
                i+=1
            if i == ns-1: 
                return ns 
    return 0

if __name__ == '__main__': 
    main()

