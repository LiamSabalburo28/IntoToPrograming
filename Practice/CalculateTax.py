def calctax():
    
    object = input("What is the object? ")
    cost = input("Cost of the object? ")
    num_float = float(cost)
    tax = 0.06875
    num_float2 = float(tax)
    print(" Total tax:", num_float*num_float2 )
    print( " Costs: ",(num_float*num_float2+num_float))
    


calctax()