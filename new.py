

#print(get_shop_list_by_dishes(['Запеченный картофель', 'Жаренный картофель'], 5))
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for dish in dishes:
        for k in cook_book.get(dish):
            ingr = k['ingredient_name']
            measure = k['measure']
            quantity = int(k['quantity'])*person_count
            ingredient_dict.setdefault(ingr, {'measure': '', 'quantity': 0})
            ingredient_dict[ingr]['measure'] = measure
            ingredient_dict[ingr]['quantity'] += quantity
    return ingredient_dict


cook_book = {}

with open('recipe.txt', encoding='UTF-8') as f:
    for stroka in f:
        if '|' not in stroka and stroka.strip().isnumeric() is False and stroka.strip():
            ingr_quant = int(f.readline().strip())
            for i in range(ingr_quant):
                temp_list = f.readline().strip().split(' | ')
                cook_book.setdefault(stroka.strip(), []).append({'ingredient_name': temp_list[0],
                                                                 'quantity': temp_list[1],
                                                                 'measure': temp_list[2]})

print(get_shop_list_by_dishes(['Запеченный картофель', 'Жаренный картофель'], 5))