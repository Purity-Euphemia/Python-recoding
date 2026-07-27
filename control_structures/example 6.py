list_of_lists = [[1 , 3, 5], [2, 4, 6], [9, 7, 5]]
for sublist in list_of_lists:
    for number in sublist:
        if number % 2 == 0:
            print("First even number in list:", number)
            break