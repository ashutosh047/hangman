import random
import string
loss=0
win=0
#function to check and replace the letter
def check(a,f,t):
    f=list(f)
    global att
    global alphabet
    i=0
    flag=-1
    for i in range(len(t)):
        if(f[i]==a or a not in alphabet):
            print("You've already guessed this letter.")
            return "".join(f)
        elif(t[i]==a):
            f[i]=a
            flag=1
    if(flag==-1):
        att-=1
        print("That letter doesn't appear in the word.")
    return "".join(f)
#function for playing game
def play_game():
    
    l=['python', 'java', 'swift', 'javascript']
    t=random.choice(l)
    f=''
    pf=''
    m=len(t)
    for i in range(m):
        f=f+'-'
    while att!=0:
        print(f)
        pf=f
        a=input('Input a letter:')
        if(a.isalpha() and len(a)==1 and a.islower()):
            f=check(a,f,t)
            if a in alphabet:
                alphabet.remove(a)
            elif(pf==f and a not in t):
                pass
            print()
            if(f==t):
                global win
                win+=1
                print(f'You guessed the word {f}!\nYou survived!')
                break;
        elif(len(a)!=1):
            print('Please, input a single letter.')
        else:
            print('Please, enter a lowercase letter from the English alphabet.')
    if(f!=t):
        global loss
        loss+=1
        print('You lost!')
    return
# Write your code here
print("H A N G M A N")
while True:
    att=8
    alphabet = list(string.ascii_lowercase)
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    ch=input()
    if(ch=='play'):
        play_game()
    elif(ch=='results'):
        print(f'You won: {win} times.')
        print(f'You lost: {loss} times.')
    elif(ch=='exit'):
        break
    else:
        pass
