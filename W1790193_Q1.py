#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: 2019745
R=[0,20,40,60,80,100,120] # R=credits range
def error():
    print("Range error!!!")

while True:
    try:
        Pass_credits=int(input("Enter your pass credits:\n"))
        if Pass_credits in R:
            pass
        else:
            while Pass_credits not in R:
                error()
                Pass_credits=int(input("Enter your pass credits:\n"))
    

        Defer_credits=int(input("Enter your defer credits:\n"))
        if Defer_credits  in R:
            pass
        else:
            while Defer_credits not in R:
                error()
                Defer_credits=int(input("Enter your defer credits:\n"))


        Fail_credits=int(input("Enter your fail credits:\n"))
        if Fail_credits  in R:
            pass
        else:
            while Fail_credits not in R:
                error()
                Fail_credits=int(input("Enter your fail credits:\n"))

        Total=Pass_credits + Defer_credits + Fail_credits #check Total credits
        if Total==120:
            if Pass_credits==120:
                print("Progress")
                break
            elif Pass_credits==100:
                print("Progress – module trailer")
                break
            elif Fail_credits==120 or Fail_credits==100 or Fail_credits==80:
                print("Exclude")
                break
            else:
                print("Do not Progress – module retriever")
                break
        else:
            print("Total incorrect!!!") #Total is not 120
            break
                

    except:
        print("Integer required!!!") #Value Error
            


            
