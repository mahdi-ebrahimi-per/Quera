# https://quera.ir/problemset/72880/

def PriceCheck(a, b, c, d, m):
    a_resualt = a
    b_resualt = b       


    for i in range(m):
        a_resualt += c
        b_resualt += d


    a_profit = a_resualt - a
    b_profit = b_resualt - b


    # print(a, a_resualt, a_profit)
    # print(b, b_resualt, b_profit)
    
    if a_resualt > b_resualt :
        if a_profit > b_profit:
            return "Eyval baba!"
        return "Naaa, eshtebahe!"

    elif b_resualt > a_resualt :
        if b_profit > a_profit:
            return "Eyval baba!"
        return "Naaa, eshtebahe!"

    elif b_resualt == a_resualt :
        return "Eyval baba!"

# print( PriceCheck(1, 2, 7, 1, 10) )
# print( PriceCheck(40, 4, 1, 2, 6) )


# print( PriceCheck(7, 1, 1, 3, 6) )

UserInput = str(input())
UserInput = UserInput.split(" ")
UserInput = list(map(lambda x:int(x), UserInput))
print(PriceCheck(UserInput[0],
 UserInput[1],
  UserInput[2],
   UserInput[3],
    UserInput[4]))










