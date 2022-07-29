s_id = input() 
_1st = s_id[0] 
_2nd = s_id[1] 
_3rd = s_id[2] 
_4th = s_id[3] 
c_digit = s_id[5] 

if "?" in s_id[5]: 
    numc_digit = (int(_1st) * 2 + int(_2nd) * 3 + int(_3rd) * 5 + int(_4th) * 7) % 11
    if numc_digit == 10:
        print(_1st + _2nd + _3rd + _4th + "-" + "X")
    else:    
        print(str(_1st) + str(_2nd) + str(_3rd) + str(_4th) + "-" + str(numc_digit))

elif "?" not in s_id: 
    numc_digit = (int(_1st) * 2 + int(_2nd) * 3 + int(_3rd) * 5 + int(_4th) * 7) % 11
    if s_id[5] == "X" and numc_digit == 10:
        print("VALID")
    elif s_id[5] == str(numc_digit):
        print("VALID")
    else: 
        print("INVALID")

elif "?" in s_id[:4]: 
    if "?" in s_id[0]:
        if s_id[5] == "X":
            x = (10 - (int(_2nd) * 3 + int(_3rd) * 5 + int(_4th) * 7)) % 11
            y = (6 * x) % 11 
            print(str(y) + _2nd + _3rd + _4th + "-" + c_digit)
        else:    
            x = (int(c_digit) - (int(_2nd) * 3 + int(_3rd) * 5 + int(_4th) * 7)) % 11
            y = (6 * x) % 11 
            print(str(y) + _2nd + _3rd + _4th + "-" + c_digit)
    
    elif "?" in s_id[1]:
        if s_id[5] == "X":
            x = (10 - (int(_1st) * 2 + int(_3rd) * 5 + int(_4th) * 7)) % 11
            y = (4 * x) % 11 
            print(_1st + str(y) + _3rd + _4th + "-" + c_digit)
        else:
            x = (int(c_digit) - (int(_1st) * 2 + int(_3rd) * 5 + int(_4th) * 7)) % 11
            y = (4 * x) % 11 
            print(_1st + str(y) + _3rd + _4th + "-" + c_digit)
    
    elif "?" in s_id[2]:
        if s_id[5] == "X":
            x = (10 - (int(_1st) * 2 + int(_2nd) * 3 + int(_4th) * 7)) % 11
            y = (9 * x) % 11 
            print(_1st + _2nd + str(y) + _4th + "-" + c_digit)
        else: 
            x = (int(c_digit) - (int(_1st) * 2 + int(_2nd) * 3 + int(_4th) * 7)) % 11
            y = (9 * x) % 11 
            print(_1st + _2nd + str(y) + _4th + "-" + c_digit)
    
    elif "?" in s_id[3]:
        if s_id[5] == "X":
            x = (10 - (int(_1st) * 2 + int(_2nd) * 3 + int(_3rd) * 5)) % 11
            y = (8 * x) % 11  
            print(_1st + _2nd + _3rd + str(y) + "-" + c_digit)
        else:     
            x = (int(c_digit) - (int(_1st) * 2 + int(_2nd) * 3 + int(_3rd) * 5)) % 11
            y = (8 * x) % 11    
            print(_1st + _2nd + _3rd + str(y) + "-" + c_digit)