test_cases = int(input("Enter the number of test cases: "))
b= []
for i in range(test_cases):
    b.append(input("Please enter an input: "))

# check for palindrom 

for i in range(len(b)):
    # print(b[i])
    p=b[i][::-1]
    # print(p) 
    if p==b[i]:
        print(f"{p} is a pallindrom")
    elif p!=b[i]:
        print(f"{b[i]} is not a palindrome")
        # print(type(p))
        # find the next possible palindrome
        try :
            p=p[::-1]               
            q=""
            while p!=q:
                p=int(p)
                p+=1
                p=str(p)
                q=p[::-1]
            print(f"The Next possible palindrome is {q}")
        except ValueError:
            print("")

# print(b)



# print(n[0])
# # if n[0]:
# #     print("yes")
# # else:
# #     print("nope")
# c=n.copy()
# c[0].reverse()
# print(c[0])
# n= "613"
# p=n[::-1]
# print(p)