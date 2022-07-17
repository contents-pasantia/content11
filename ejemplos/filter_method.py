# numeros impares 

my_list = [1, 4, 5, 6, 9, 13, 19]

num = [i for i in my_list if i % 2 != 0]
print(num)

# usando filter
num_filter = list(filter(lambda x: x % 2 != 0, my_list))
print(num_filter)