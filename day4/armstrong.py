for num in range(1042000, 702648265):
    i = len(str(num))
    
  
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** i
       temp //= 10

   if num == sum:
       print("the first armstrong number is " ,num)
       break