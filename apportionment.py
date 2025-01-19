#Apportionment calculation
#Apportionment Introduced in Mathematics in The Modern World



import math
def hamilton():
    rows = int(input("No. of column:"))
    amount = int(input("Amount to be apportion: "))
    Label = []
    population = []
    quotient = []
    DecQuotient = []
    SortedQuotient = []
    StandardQuota = []
    addition = []
    final = []


    for subject in range(1,rows+1):
        object = "SUBJECT"+str(subject)
        Label.append(object)


    for count in range(rows):
        column = int(input("POPULATION: "))
        population.append(column)
    TotalPopulation = sum(population)
    StandardDiv = TotalPopulation / amount

    for elements in range(len(population)):
        fraction = population[elements] / StandardDiv
        quotient.append(round(fraction,ndigits=2))
        StandardQuota.append(math.floor(quotient[elements]))
        final.append(math.floor(quotient[elements]))


#code below for locating where to add 1 in the list of quotient
#because in hamilton if there is a given amount of number that is missing from the result
#for example the target is 23 but the solution yielded 19 meaning that we are (23-19)  4 short and that we need to add a 4
#this code tell us where to add 1 to yield the target number


#code below for addition column and final column
    #getting the decimal value of each elements in quotient list
    for original in range(len(StandardQuota)):
        dec = quotient[original] % StandardQuota[original]
        DecQuotient.append(round(dec,ndigits=2))
        SortedQuotient.append(round(dec,ndigits=2))
    SortedQuotient.sort()
    #limits the decimal place to 2




    #array to store the larges number that is needed
    largeNum = []
    for position in range(1, amount - sum(StandardQuota)+1):
        sorting = SortedQuotient[-position]
        largeNum.append(sorting)
    
    
    #Locating the specif index position of the larges decimal
    #then adding 1

    for finding in range(len(quotient)):
        for a in range(len(largeNum)):
            re = "whitespace filler lang para hindi blangko ang inner for loop"
            if DecQuotient[finding] == largeNum[a]:
                final[finding] = final[finding]+1


    #para sa additional column
    for add in range(len(quotient)):
        wanzero = final[add] - StandardQuota[add]
        addition.append(wanzero)



    #the table where the data will be shown  or printed
    def ColumnGraph():
        boundary = ("________________________________________________________________________________________________________________")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tStandard Quota\t\tADDITIONAL\t\tFINAL\t│\n"+boundary+"│")
        
        for box in range(rows):
            for label in range(1):    
                print(Label[box],end="\t")
            for column1 in range(1):
                print(f'{population[box]:,}',end="\t\t\t")


            for column2 in range(1):
                
                print(quotient[box],end="\t\t\t")
            for column3 in range(1):
                
                print(StandardQuota[box],end="\t\t\t")

            for column4 in range(1):
                print(addition[box],end="\t\t\t")
            
            for column5 in range(1):
                print(final[box],end="\t")



            for side in range(1):
                print("│")

        print(boundary+"\nTOTAL: \t\t"+f'{TotalPopulation:,}'+"\t\t\t\t\t\t"+str(sum(StandardQuota))+"\t\t\t\t\t    "+str(sum(final))+'\t│')


    ColumnGraph()

def Jefferson():

    column = int(input("NO. OF COLUMNS: "))
    target = int(input("Amount To Apportion: "))
    FOCUS = []
    population = []
    quotient = []
    StanQuota = []
    secondQuotient =[]
    newStanQuota = []

    for subject in range(1,column+1):
        object = "SUBJECT"+str(subject)
        FOCUS.append(object)



    for x in range(column):
        rows = int(input("POPULATION: "))
        population.append(rows)

    StanDiv = round(sum(population)/target,ndigits=2)
    for y in range(column):
        quotient.append(round(population[y]/StanDiv,ndigits=2))
        StanQuota.append(math.floor(quotient[y]))
    print(StanDiv)
    if sum(StanQuota) < target:
#finding the right modified stardard divisor 
        while sum(StanQuota) != target:
            StanDiv -= 0.01
            MSD = round(StanDiv,ndigits=2)
            for i in range(len(population)):            
                secondQuotient.append(round(population[i] / MSD,ndigits=2))
                newStanQuota.append(math.floor(secondQuotient[i]))
            print(secondQuotient)
            
            if sum(newStanQuota) != target:
                secondQuotient.clear()
                newStanQuota.clear()
                continue
            elif sum(newStanQuota) == target:
                
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tStandard Quota\t\tADDITIONAL\t\tFINAL\t│\n"+boundary+"│")
                    
                    for box in range(column):
                        for label in range(1):    
                            print(FOCUS[box],end="\t")
                        for column1 in range(1):
                            print(f'{population[box]:,}',end="\t\t\t")

                        for column2 in range(1):                        
                            print(quotient[box],end="\t\t\t")
                        for column3 in range(1):
                            
                            print(StanQuota[box],end="\t\t\t")

                        for column4 in range(1):
                            print(secondQuotient[box],end="\t\t\t")
                        
                        for column5 in range(1):
                            print(newStanQuota[box],end="\t")



                        for side in range(1):
                            print("│")

                    print(boundary+"\nTOTAL: \t\t"+f"{sum(population):,}"+"\t\t\t\t\t\t"+str(sum(StanQuota))+"\t\t\t\t\t    "+str(sum(newStanQuota))+'\t│')
                    print(f"\n\n\tTHE MODIFIED STANDARD DIVSOR IS {round(StanDiv,ndigits=2)}")

                GRAPH()
                break
            else:
                print("ERROR")
            
    elif sum(StanQuota) > target:
        
        while sum(StanQuota) != target:
            StanDiv -= 0.01
            MSD = round(StanDiv,ndigits=2)
            for i in range(len(population)):            
                secondQuotient.append(round(population[i] / MSD,ndigits=2))
                newStanQuota.append(math.floor(secondQuotient[i]))
            print(secondQuotient)
            
            if sum(newStanQuota) != target:
                secondQuotient.clear()
                newStanQuota.clear()
                continue
            elif sum(newStanQuota) == target:
                
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tStandard Quota\t\tADDITIONAL\t\tFINAL\t│\n"+boundary+"│")
                    
                    for box in range(column):
                        for label in range(1):    
                            print(FOCUS[box],end="\t")
                        for column1 in range(1):
                            print(f'{population[box]:,}',end="\t\t\t")

                        for column2 in range(1):                        
                            print(quotient[box],end="\t\t\t")
                        for column3 in range(1):
                            
                            print(StanQuota[box],end="\t\t\t")

                        for column4 in range(1):
                            print(secondQuotient[box],end="\t\t\t")
                        
                        for column5 in range(1):
                            print(newStanQuota[box],end="\t")



                        for side in range(1):
                            print("│")

                    print(boundary+"\nTOTAL: \t\t"+f"{sum(population):,}"+"\t\t\t\t\t\t"+str(sum(StanQuota))+"\t\t\t\t\t    "+str(sum(newStanQuota))+'\t│')
                    

                GRAPH()
                break
            else:
                print("ERROR")        
    else:
        print(404)

def Adam():

    column = int(input("NO. OF COLUMNS: "))
    target = int(input("Amount To Apportion: "))
    FOCUS = []
    population = []
    quotient = []
    StanQuota = []
    secondQuotient =[]
    newStanQuota = []

    for subject in range(1,column+1):
        object = "SUBJECT"+str(subject)
        FOCUS.append(object)



    for x in range(column):
        rows = int(input("POPULATION: "))
        population.append(rows)

    StanDiv = round(sum(population)/target,ndigits=2)
    for y in range(column):
        quotient.append(round(population[y]/StanDiv,ndigits=2))
        StanQuota.append(math.ceil(quotient[y]))
    print(StanDiv)

#finding the right modified stardard divisor 
    while sum(StanQuota) != target:
        StanDiv += 0.01
        MSD = round(StanDiv,ndigits=2)
        for i in range(len(population)):            
            secondQuotient.append(round(population[i] / MSD,ndigits=2))
            newStanQuota.append(math.ceil(secondQuotient[i]))
        print(secondQuotient)
        
        if sum(newStanQuota) != target:
            secondQuotient.clear()
            newStanQuota.clear()
            continue
        elif sum(newStanQuota) == target:
            
            def GRAPH():
                boundary = ("________________________________________________________________________________________________________________")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tStandard Quota(U)\tMODI QUOTIENT\tFINAL\t│\n"+boundary+"│")
                
                for box in range(column):
                    for label in range(1):    
                        print(FOCUS[box],end="\t")
                    for column1 in range(1):
                        print(f'{population[box]:,}',end="\t\t\t")

                    for column2 in range(1):                        
                        print(quotient[box],end="\t\t\t")
                    for column3 in range(1):
                        
                        print(StanQuota[box],end="\t\t\t")

                    for column4 in range(1):
                        print(secondQuotient[box],end="\t\t\t")
                    
                    for column5 in range(1):
                        print(newStanQuota[box],end="\t")



                    for side in range(1):
                        print("│")

                print(boundary+"\nTOTAL: \t\t"+f"{sum(population):,}"+"\t\t\t\t\t\t"+str(sum(StanQuota))+"\t\t\t\t\t    "+str(sum(newStanQuota))+'\t│')
                print(f"\n\n\tTHE MODIFIED STANDARD DIVSOR IS {round(StanDiv,ndigits=2)}")

            GRAPH()
            break
        else:
            print("ERROR")

def Webster():

    column = int(input("NO. OF COLUMNS: "))
    target = int(input("Amount To Apportion: "))
    FOCUS = []
    population = []
    quotient = []
    StanQuota = []
    secondQuotient =[]
    newStanQuota = []

    for subject in range(1,column+1):
        object = "SUBJECT"+str(subject)
        FOCUS.append(object)



    for x in range(column):
        rows = int(input("POPULATION: "))
        population.append(rows)

    StanDiv = round(sum(population)/target,ndigits=2)
    for y in range(column):
        quotient.append(round(population[y]/StanDiv,ndigits=2))
        StanQuota.append(round(quotient[y]))
    print(StanDiv)
    if sum(StanQuota) < target:
#finding the right modified stardard divisor 
        while sum(StanQuota) != target:
            StanDiv -= 0.01
            MSD = round(StanDiv,ndigits=2)
            for i in range(len(population)):            
                secondQuotient.append(round(population[i] / MSD,ndigits=2))
                newStanQuota.append(round(secondQuotient[i]))
            print(secondQuotient)
            
            if sum(newStanQuota) != target:
                secondQuotient.clear()
                newStanQuota.clear()
                continue
            elif sum(newStanQuota) == target:
                
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tStandard Quota(U)\tMODI QUOTIENT\tFINAL\t│\n"+boundary+"│")
                    
                    for box in range(column):
                        for label in range(1):    
                            print(FOCUS[box],end="\t")
                        for column1 in range(1):
                            print(f'{population[box]:,}',end="\t\t\t")

                        for column2 in range(1):                        
                            print(quotient[box],end="\t\t\t")
                        for column3 in range(1):
                            
                            print(StanQuota[box],end="\t\t\t")

                        for column4 in range(1):
                            print(secondQuotient[box],end="\t\t\t")
                        
                        for column5 in range(1):
                            print(newStanQuota[box],end="\t")



                        for side in range(1):
                            print("│")

                    print(boundary+"\nTOTAL: \t\t"+f"{sum(population):,}"+"\t\t\t\t\t\t"+str(sum(StanQuota))+"\t\t\t\t\t    "+str(sum(newStanQuota))+'\t│')
                    print(f"\n\n\tTHE MODIFIED STANDARD DIVSOR IS {round(StanDiv,ndigits=2)}")

                GRAPH()
                break
            else:
                print("ERROR")

    elif sum(StanQuota) > target:
#finding the right modified stardard divisor 
        while sum(StanQuota) != target:
            StanDiv += 0.01
            MSD = round(StanDiv,ndigits=2)
            for i in range(len(population)):            
                secondQuotient.append(round(population[i] / MSD,ndigits=2))
                newStanQuota.append(round(secondQuotient[i]))
            print(secondQuotient)
            
            if sum(newStanQuota) != target:
                secondQuotient.clear()
                newStanQuota.clear()
                continue
            elif sum(newStanQuota) == target:
                
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\t\tROUNDED VALUE\t\tMODI QUOTIENT\tFINAL\t│\n"+boundary+"│")
                    
                    for box in range(column):
                        for label in range(1):    
                            print(FOCUS[box],end="\t")
                        for column1 in range(1):
                            print(f'{population[box]:,}',end="\t\t\t")

                        for column2 in range(1):                        
                            print(quotient[box],end="\t\t\t")
                        for column3 in range(1):
                            
                            print(StanQuota[box],end="\t\t\t")

                        for column4 in range(1):
                            print(secondQuotient[box],end="\t\t\t")
                        
                        for column5 in range(1):
                            print(newStanQuota[box],end="\t")



                        for side in range(1):
                            print("│")

                    print(boundary+"\nTOTAL: \t\t"+f"{sum(population):,}"+"\t\t\t\t\t\t"+str(sum(StanQuota))+"\t\t\t\t\t    "+str(sum(newStanQuota))+'\t│')
                    print(f"\n\n\tTHE MODIFIED STANDARD DIVSOR IS {round(StanDiv,ndigits=2)}")

                GRAPH()
                break
            else:
                print("ERROR")

def HuntingHill():
    column = int(input("NO. OF COLUMNS: "))
    target = int(input("Amount To Apportion: "))
    population = []
    quotient = []
    L = []
    U = []
    GM = []
    FINAL = []
    TOGGLE = []
    FOCUS = []
    for subject in range(1,column+1):
        object = "SUBJECT"+str(subject)
        FOCUS.append(object)


    for i in range(column):
        data = int(input("POPULATIONS: "))
        population.append(data)
    
    StanDiv = round(sum(population)/ target,ndigits=2)

    for x in range(column):
        quotient.append(round(population[x] / StanDiv,ndigits=2))
        L.append(math.floor(quotient[x]))
        U.append(round(quotient[x]))
        GM.append(round(math.sqrt(L[x]*U[x]),ndigits=2))

    for y in range(column):
        if quotient[y] < GM[y]:
            FINAL.append(math.floor(GM[y]))
            TOGGLE.append(math.floor(GM[y]))
        elif quotient[y] >= GM[y]:
            FINAL.append(math.ceil(GM[y]))
            TOGGLE.append(math.ceil(GM[y]))

    if sum(FINAL) != target:
        quotient.clear()
        L.clear()
        U.clear()
        GM.clear()
        FINAL.clear()
    else:
        print(404)

    if sum(TOGGLE) < target:
        gate = False
        while gate == False:
            StanDiv -= 0.01
            MSD = round(StanDiv,ndigits=2)

            for x in range(column):
                quotient.append(round(population[x] / MSD,ndigits=2))
                L.append(math.floor(quotient[x]))
                U.append(round(quotient[x]))
                GM.append(round(math.sqrt(L[x]*U[x]),ndigits=2))

            for y in range(column):
                if quotient[y] < GM[y]:
                    FINAL.append(math.floor(GM[y]))
                elif quotient[y] >= GM[y]:
                    FINAL.append(math.ceil(GM[y]))

            if sum(FINAL) != target:
                quotient.clear()
                L.clear()
                U.clear()
                GM.clear()
                FINAL.clear()
                continue
            elif sum(FINAL) == target:
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\tUPPER QUOTA\tLOWER QUOTA\tGEOMETRIC MEAN\t\tFINAL\t│\n"+boundary+"│")
                    for box in range(column):
                        for label in range(1):
                            print(FOCUS[box],end="\t\t")
                        for A in range(1):
                            print(population[box],end="\t\t\t")
                        for B in range(1):
                            print(quotient[box],end="\t\t")
                        for C in range(1):
                            print(L[box],end="\t\t")
                        for D in range(1):
                            print(U[box],end="\t\t")
                        for E in range(1):
                            print(GM[box],end="\t\t\t\t")
                        for F in range(1):
                            print(FINAL[box],end="\t")
                        for side in range(1):
                            print("│")
                    print()
                    print(boundary+"\nTOTAL: \t\t"+str(sum(population))+"\t\t\t\t\t"+str(sum(L))+"\t\t"+str(sum(U))+"\t\t\t\t    \t"+str(sum(FINAL))+"\t│")                
                GRAPH()
                gate = True
                break
            else:
                print(404)
        
    elif sum(TOGGLE) > target:
        gate = False
        while gate == False:
            StanDiv -= 0.01
            MSD = round(StanDiv,ndigits=2)

            for x in range(column):
                quotient.append(round(population[x] / MSD,ndigits=2))
                L.append(math.floor(quotient[x]))
                U.append(round(quotient[x]))
                GM.append(round(math.sqrt(L[x]*U[x]),ndigits=2))

            for y in range(column):
                if quotient[y] < GM[y]:
                    FINAL.append(math.floor(GM[y]))
                elif quotient[y] >= GM[y]:
                    FINAL.append(math.ceil(GM[y]))

            if sum(FINAL) != target:
                quotient.clear()
                L.clear()
                U.clear()
                GM.clear()
                FINAL.clear()
            elif sum(FINAL) == target:
                def GRAPH():
                    boundary = ("________________________________________________________________________________________________________________________")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+boundary+"\nSUBJECT\t\tPopulations\t\tQuotient\tUPPER QUOTA\tLOWER QUOTA\tGEOMETRIC MEAN\t\tFINAL\t│\n"+boundary+"│")
                    for box in range(column):
                        for label in range(1):
                            print(FOCUS[box],end="\t\t")
                        for A in range(1):
                            print(population[box],end="\t\t\t")
                        for B in range(1):
                            print(quotient[box],end="\t\t")
                        for C in range(1):
                            print(L[box],end="\t\t")
                        for D in range(1):
                            print(U[box],end="\t\t")
                        for E in range(1):
                            print(GM[box],end="\t\t\t\t")
                        for F in range(1):
                            print(FINAL[box],end="\t")
                        for side in range(1):
                            print("│")
                    print()
                    print(boundary+"\nTOTAL: \t\t"+str(sum(population))+"\t\t\t\t\t"+str(sum(L))+"\t\t"+str(sum(U))+"\t\t\t\t    \t"+str(sum(FINAL))+"\t│")                
                GRAPH()
            else:
                print(404)

    else:
        print("THE STANDARD DIVISOR IS ALREADY RIGHT")


def main():
    print('---- APPORTIONMENT METHOD ----')
    print('\n\n\n[1] HAMILTON\n[2] JEFFERSON\n[3] ADAM\n[4] WEBSTER\n[5] HUNTING-HILL')
    choice = (input("OPTION: "))
    if choice.isnumeric:
        choice = int(choice)
        if choice == 1:
            print("\n\nHAMILTON\n\n")
            hamilton()
        elif choice == 2:
            print("\n\nJEFFERSON\n\n")
            Jefferson()
        elif choice == 3:
            print("\n\nADAM\n\n")
            Adam()
        elif choice == 4:
            print("\n\nWEBSTER\n\n")
            Webster()
        elif choice == 5:
            print("\n\nHUNTING - HILL\n\n")
            HuntingHill()
        else:
            print('ERROR')
            main()
    else:
        print("ERROR")
        main()

main()

"""
def count_sheeps(sheep):
  # TODO May the force be with you
    sheep = [True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,]
    count = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            count += 1
        else:
            f=4
    print(f"There are {count} of sheep")
mylist=[True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,]
count_sheeps(mylist)
"""
