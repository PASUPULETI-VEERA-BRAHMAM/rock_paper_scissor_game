import random
l=['r','p','s']
while(1):
    c = random.choice(l)
    u = input("Enter your choice [r,p,s]: ")
    if c==u:
        print(f'Draw')
    elif ((c=='r' and u=='s') or (c=='p' and u=='r') or (c=='s' and u=='p')):
        print(f'You Lost')
    else:
        print(f'You Won')
    print(f'User : {u} and computer : {c}')
    n=input(f'do you want to continue y/n : ')
    if n=='n':
        print(f'Thank You for playing')
        break