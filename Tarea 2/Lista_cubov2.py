nums = []
print("Cuantos numeros ingresara? ")
n = int(input())
i = 0 
while i < n:
    print ("El valor numero: ", i + 1 )
    val = int(input())
    nums.append(val)
    i += 1
print(nums)
#cubo = val** 3
#print(cubo) 
print("{}".format(nums[0]**3))
print("{}".format(nums[1]**3))