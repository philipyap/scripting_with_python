# open a file
rome_file = open('rome.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    rome_file.write('{}\n'.format(num))

#write to the file
# rome_file.write('')
rome_file.close()

# read a file
# print(rome_file.read())

# close a file
# rome_file.close()

# if file is not found, one ill be created
adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
adam_file.close()

new_file = open('new_file.txt')
file_items = new_file.readline()
print(file_items)

# for i in range(len(file_items)):
#     each_item = file_items[i]
#     print('Before: {}'.format(each_item))
#     print(each_item[0:-1])
#     file_items[i] = each_item[0:-1]
#     print(file_items)

# # print(file_items)

# new_file.close()