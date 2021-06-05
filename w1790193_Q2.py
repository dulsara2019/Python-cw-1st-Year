#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: 2019745
R=[0,20,40,60,80,100,120] #credits range
progress_total=0
module_trailer_total=0
exclude_total=0
module_retriever_total=0
student_total=0

def error():
    print("Range error!!!")  #credits not in credits range
while True:
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
            if Defer_credits in R:
                pass
            else:
                while Defer_credits not in R:
                    error()
                    Defer_credits=int(input("Enter your defer credits:\n"))

            Fail_credits=int(input("Enter your fail credits:\n"))
            if Fail_credits in R:
                pass
            else:
                while Fail_credits not in R:
                    error()
                    Fail_credits=int(input("Enter your fail credits:\n"))

            Total=Pass_credits + Defer_credits + Fail_credits #checking total crredits

            if Total==120:
                if Pass_credits==120:
                    progress_total +=1
                    student_total +=1
                    print("Progress")
                    break
                elif Pass_credits==100:
                    module_trailer_total +=1
                    student_total +=1
                    print("Progress - module trailer")
                    break
                elif Fail_credits==80 or Fail_credits==100 or Fail_credits==120:
                    exclude_total +=1
                    student_total +=1
                    print("Exclude")
                    break
                else:
                    module_retriever_total +=1
                    student_total +=1
                    print("Donot Progress - module retriever")
                    break
                    
                break

            else:
                print("Total incorrect!!!")
                continue
        except ValueError:
            print("Integer required!!!")
            continue

    q=input("Enter q to quit programme or enter any key to continue:")#q to get outcomes in total                  
    if q=="q":
        break
    else:
        continue
    
print("")
print("Progress                         ",progress_total,":","*"*progress_total)
print("Progress - module trailer        ",module_trailer_total,":","*"*module_trailer_total)
print("Exclude                          ",exclude_total,":","*"*exclude_total)
print("Donot Progress - module retriever",module_retriever_total,":","*"*module_retriever_total)
print(student_total,"outcomes in total")
    




















                                   
                                       
