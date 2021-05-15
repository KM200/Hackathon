def no_of_pairs(socks_list):
    uniq=set(socks_list)
    count=[]
    no_of_pair=0
    for sock in uniq:
        count.append(socks_list.count(sock))
     
    for i in count:
        no_of_pair+=i//2
    
    return no_of_pair

n=9
list=[10,20,20,10,10,30,50,10,20]
print(no_of_pairs(list))