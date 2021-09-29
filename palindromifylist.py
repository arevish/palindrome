n=input("Enter your list seprated by ',' ").split(",")
print(n)
li=[]
for i in range(len(n)):
    p=n[i][::-1]
    if n[i]==p:
        # print(f"{n[i]} is a palindrome")
        li.append(int(n[i]))
    else:
        # print(f"{n[i]} not a palindrome")
        # find next palindrome
        p=p[::-1]          
        if int(p)> 17 :
            # p=p[::-1]               
            q=""
            while p!=q:
                p=int(p)
                p+=1
                p=str(p)
                q=p[::-1]
            # print(f"The next possible palindrome is {q}")
            li.append(int(q))
        else:
            li.append(int(n[i]))
print(li)

## Other method
# def pallindrom(n):
#     return str(n)==str(n)[::-1]
        
# def next_palindrome(n):
#     while not pallindrom(n):
#         n=int(n)
#         n+=1
#     return n
#     # print(f"next posslble palindrome is {n}")

# if __name__=="__main__":
#     size=int(input("Enter size of list: "))
#     list1=[]
#     for i in range(size):
#         m=int(input("Enter you number "))
#         list1.append(m)
#     print(list1)

#     out_list=[]
#     for i in list1:
#         
#         if i>10:
#             next_palindrome(i)
#             out_list.append(next_palindrome(i))
#         else:
#             pallindrom(i)
#             out_list.append(i)
#     print(out_list)