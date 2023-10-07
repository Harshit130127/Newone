import matplotlib.pyplot as plt


class Mortgage:
    def __init__( self,l,y,p,k):
        self.loan =l
        self.years =y
        self.interest =p
        self.r_frequency = k
        print('success')
        
    def repayments(self):
   
   
        q= ((1+(((self.interest)/100)/365))**(365*self.years))
        w=((1+(((self.interest)/100)/365))**(self.r_frequency))
        r=((1+(((self.interest)/100)/365))**(365*self.years))
        P=( self.loan*q)*((w-1)/(r-1))
        return P

    
    def balance_after(self,n):
        i= self.interest/100
        q2=((1+(i/365))**(365*n))
        w2= ((1+(i/365))**(365*n))
        r2=((1+(i/365))**(self.r_frequency))
        B=(self.loan*q2)-((self.repayments())*((w2-1)/(r2-1)))
        return B
    
    def __str__(self):
        print('Program Plot:')
        print(f"Loan amount {l}")
        print(f"Loan terms (in years) {y}")
        print(f"Interest:{p}%")
        print(f"Fortnightly repayments:{a.repayments()} AUD")
        
    def draw_balance_graph(self):
        
        balance_remains = [self.balance_after(year) for year in range(1, self.years + 1)]
        
        plt.figure(figsize=(10, 6))  
        plt.plot(range(1, self.years + 1), balance_remains, marker='o', linestyle='-')
        plt.title("Remaining Principal Balance by Year")
        plt.xlabel("Year")  
        plt.ylabel("Remaining Balance (AUD)")  
        plt.grid(True)  
        plt.show()  
            
        


while True:
    try:
        l=int(input('enter the loan (in AUD)'))
        assert(l>0)
        break
        # 
    except :
        print('value must not be float,string or negative.Try again...')
        

        
while True:
            try:
                y=int(input("enter loan terms(in years)"))
                assert(y>0)
                break
            except:
                print('not a valid int value.Try again...')


while True:
    try:
        
      p=float(input("enter the bank's interest"))  
      assert(p>0)
      break 
      
    except:
        print("value of 'interest'should be positive.Try again")
        
     
while True:
      k=int(input('enter the repayment frequency in days in (7,14 or 30)'))

      if (k==7 or k==14 or k==30):
      
         break
     
      else:
        print('Value of frequency should be 7,14 or 30.Try again...') 
        
        
a=Mortgage(l,y,p,k)
a.__str__()
n=int(input('enter the n years'))
a.balance_after(n)
a.draw_balance_graph()