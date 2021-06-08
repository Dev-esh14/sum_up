"""
Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
"""
def sum_up_digits():
    sum =0
    i = 1001


    for i in range(22000):
        while(i!=0):
            sum=sum+int(i%10)
            i = i/10
    return sum
print(sum_up_digits()) 

"""
OUTPUT:
402000
"""
