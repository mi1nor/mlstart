def my_fn(num, str):
    """
        Моя функция...
    """   
    
    res = ""
    alf = ' abcdefghijklmnopqrstuvwxyz'

    for symbol in str:
        i = 0
        for symbol_a in alf:
            if symbol_a == symbol:
                if(num < 0):
                    res += alf[i + num]
                else:
                    if(i + num) >= len(alf):
                        res += alf[(i + num) - len(alf)]
                    else:
                        res += alf[i + num]
                break
            i += 1
    return res
