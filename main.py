"""with open ('recipe.txt') as f:
    #for i in f:
    #    print(i.strip())
    for idx, l in enumerate(f):
        print(idx, l.strip())"""





"""ile_name = “Recieps"
def catalog_reader(file_name):
cook_book = {}
dish_ingridient = []
with open(file_name) as file:
for dish in file:
dish = dish.split()
quantity = file.readline()
for item in range(int(quantity)):
ingridient_dish = file.readline()
list_ingridient_dish = ingridient_dish.split(” | ")
dec_ingridient = {‘ingredient_name’: list_ingridient_dish[0], ‘quantity’: list_ingridient_dish[1], ‘measure’: list_ingridient_dish[2]}
dish_ingridient.append(dec_ingridient)
cook_book[dish] = dish_ingridient
fake = file.readline()
return cook_book
cook_book = catalog_reader(file_name)
print(cook_book)"""





    #    dish_name = f.readline().strip()
#    amount_ingredients = int(f.readline().strip())

#    for count in amount_ingredients:
#        ingredient_name = f.readline().strip()

#print(dish_name)
#print(type(amount_ingredients))
#print(amount_ingredients)
