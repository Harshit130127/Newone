# Lab 2  New password

b=1234#constant number 
k=0

for a in range(1,5):

    a=int(input('enter your password\n'))
    
    if(a==b):
        print('move  to the next part')#checking against the constant
        break
        
    if(k==3):#four valid attempts
        print("locked")
        exit
        
    else:
        print('Try again')
        k+=1
                

                
    
def fun(k):

    Specialsymbol=['!','@','#','$','%','^','&','*','()','.']
    t=0
#   Restrictions are:-
        
    if 8<=len(k)<16:
        print('Must have at least 8 characters and no more than 16 characters')
        t=1

    if not any(character.isupper() for character in k):
        print("Must have at least 1 upper case alphabetic character.")
        t=1
        
    if not any(character.islower() for character in k):
        print('Must have at least 1 lower case alphabetic character.')
        t=1

    if not any(character in Specialsymbol for character in k):
        print('enter one of the special symbol')
        t=1

    if (t==1):
         print('the new password is invalid and has not been changed.')  #criteria is not match
         
    if(t==0):
        print(f'Your updated password is {d}\n') 
          
    return t

if(a==b):
    i=0
    while (i<10):
        
        c=(input('enter the  new password\n'))
      
        d=(input('enter the new password again\n' ))#new password twice
    
        if(c==d):#matching the new password
        
            m=fun(d)
            break
    
        else:
             print('passwords does not match\n')
        i+=1

    

        
    
    
          
        

        
        

      
            
            