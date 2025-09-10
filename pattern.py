

   # N = int (input("enter a number")):
    #for i in range(1,N+1):
     #       for j in range(1,N+1):
      #          if (j==1) or (j==n):
       #             print("*", end="*")
        #        else:
         #           print(i,end="*")
          #          print()
                                    
              
              
#N = int(input("N: "))
#for i in range(1, N+1):
    #for j in range(N+1-i):   
     #   print("*", end="")
    #print()

n = int (input())

for i in range(1, n+1):
    for j in range(1,i+1):
        if j % 2 == 1:
            print(j,end=" ")
        else:
            print("*", end=(" "))
            print()
                  
                
                
                
                        
        