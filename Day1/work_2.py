menu = {
    'North':{
        'Shandong':['Qingdao','Jinan'],
        'Heibei':['Shijiazhuang','Langfang']
    },
    'South':{
        'Jiangsu':['Nanjing','Suzhou'],
        'Zhejiang':['Hangzhou','Ningbo']
    }
}

while True:
    for first_key in enumerate(menu):                   #show the index
        use_first_key = list(first_key)                 #xian de mei shi
        print (str(use_first_key[0]+1)+":"+str(use_first_key[1]))

    choice_1 = input("Please input your choice:")
    use_choice_1 = str(int(choice_1)-1)

