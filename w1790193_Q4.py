#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 2019745
progress_total=0
module_trailer_total=0
exclude_total=0
module_retriever_total=0

def function(a,b):
    c=[ [120,0,0] , [100,20,0] , [100,0,20] , [80,20,20] , [60,40,20] , [40,40,40] , [20,40,60] , [20,20,80] , [20,0,100] , [0,0,120] ]
    return(c[a][b])

for e in range (0,10):
        p = function(e,0) #p=pass
        d = function(e,1) #d=defer
        f = function(e,2) #f=fail



        if p == 120:
            progress_total +=1
                    
        elif p == 100:
            module_trailer_total +=1
                   
        elif f == 80 or f == 100 or f == 120:
            exclude_total +=1
                    
        else:
            module_retriever_total +=1
                    
    
print("Progress                         ",progress_total,":","*"*progress_total)
print("Progress - module trailer        ",module_trailer_total,":","*"*module_trailer_total)
print("Exclude                          ",exclude_total,":","*"*exclude_total)
print("Donot Progress - module retriever",module_retriever_total,":","*"*module_retriever_total)
print(progress_total+module_trailer_total+exclude_total+module_retriever_total,"outcomes in total")
    
    
