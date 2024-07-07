def operate_on_lists():
    my_list = [1, 2, 3, 4, 5]
    print("Original List : ", my_list)
    
    while True:
        print("\nList Operations Menu : ")
        print("1. Append an element")
        print("2. Reverse the list")
        print("3. Delete the first element")
        print("4. Exit")

        choice = input("Enter your choice (1-4) : ")
        
        if choice == '1':
            element = int(input("Enter element to append : "))
            my_list.append(element)
            print("List after appending element : ", my_list)
        elif choice == '2':
            my_list.reverse()
            print("Reversed List : ", my_list)
        elif choice == '3':
            del my_list[0]
            print("List after deleting the first element : ", my_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def operate_on_dictionaries():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original Dictionary : ", my_dict)
    
    while True:
        print("\nDictionary Operations Menu :")
        print("1. Add a key-value pair")
        print("2. Delete a key-value pair")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            my_dict[key] = value
            print("Updated dictionary : ", my_dict)
        elif choice == '2':
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print("Updated dictionary : ", my_dict)
            else:
                print("Key not found in dictionary.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def operate_on_sets():
    my_set = {1, 2, 3, 4, 5}
    print("Original Set : ", my_set)
    
    while True:
        print("\nSet Operations Menu : ")
        print("1. Add an element")
        print("2. Remove an element")
        print("3. Exit")

        choice = input("Enter your choice (1-3) : ")
        
        if choice == '1':
            element = int(input("Enter element to add : "))
            my_set.add(element)
            print("Updated set : ",my_set)
        elif choice == '2':
            element = int(input("Enter element to remove : "))
            if element in my_set:
                my_set.remove(element)
                print("Updated set : ", my_set)
            else:
                print("Element not found in set.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def operate_on_tuples():
    my_tuple = (1, 2, 3, 4, 5)
    print("Original Tuple : ", my_tuple)
    
    reversed_tuple = tuple(reversed(my_tuple))
    print("Reversed Tuple : ", reversed_tuple)


while True:
    print("\nOperations Menu : ")
    print("1. Operations on Lists")
    print("2. Operations on Dictionaries")
    print("3. Operations on Sets")
    print("4. Operations on Tuples")
    print("5. Exit")
    choice = input("Enter your choice (1-5) : ")
    
    if choice == '1':
        operate_on_lists()
    elif choice == '2':
        operate_on_dictionaries()
    elif choice == '3':
        operate_on_sets()
    elif choice == '4':
        operate_on_tuples()
    elif choice == '5':
        print("Exiting program!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")