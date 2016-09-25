#!/usr/bin/env python3

money = 10000
mall = ['Motherboard','CPU','Memory','Mouse''Keyboard','Display']
cash = ['1000','2000','600','100','200','1200']
cart = {}

while True:
    for dis_mall_cash in range(5):
        print ("%s:%s,%sRMB"%(dis_mall_cash+1,mall[dis_mall_cash],cash[dis_mall_cash]))

    mall_choice_temp = int(input("Please choose what you want or input '0' to bill:"))
    mall_choice = mall_choice_temp - 1       #get what you want

    if mall_choice_temp == 0:          #go into billing step
        total_price = 0
        for mall_index in cart:
            total_price = total_price + int(cash[mall_index]) * int(cart[mall_index])
        print ("The total price is %d"%(total_price))
        if total_price < money:
            money = money - total_price
            print("Bill suuceed!Your balance is %d"%(money))
            break
        else:
            print("Sorry,you don't have enough money.Go get some!")

    mall_choice_count = input("Please input how many you want:")      #get how many you want

    cart[mall_choice] = int(mall_choice_count)