def remove_duplicates_preserve_order(lst):
    checked = set()
    unique_list = []
    for item in lst:
        if item not in checked:
            unique_list.append(item)
            checked.add(item)
    return unique_list
user_input = input("Enter a list of elements separated by commas: ")
try:
    #listeye dönüştürdük
    user_list = [int(x.strip()) for x in user_input.split(',')]
    # Fonksiyonu çağırdık
    result = remove_duplicates_preserve_order(user_list)
    print("List after removing duplicates:", result)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")
