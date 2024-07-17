a=1 
b=100  
count=0 
my_list = [] 
for number in range (a, b + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            count+=1
            my_list.append(number)
print("No. of Prime Number",count)
print(my_list)
my_result = []
for elem in my_list:
   sum = 0
   for digit in str(elem):
      sum += int(digit)
   my_result.append(sum)
print ("The result after adding the digits is : " )
print(my_result)
prime=[] 
for i in my_result :
    c=0 
    for j in range(1,i): 
        if i%j==0: 
            c+=1 
    if c==1: 
        prime.append(i)
print("Prime No. Btw 1 To 100 Whose Digit Sum Is Also A Prime No.")
print(prime)
setprime=set(prime)
print("Prime No. Btw 1 To 100 Whose Digit Sum Is Also A Prime No. With No Duplicate values")
print(setprime)
