def func02(x,y,z):
    model = int( input("please input the model: "))
    if model == 1:
        result = x + y + z
    elif model == 2:
        result = (x + y) * z
    else:
        result = 0
    print ('the model is '+ str(model) + ' and the result is ' + str(result))
    return 
