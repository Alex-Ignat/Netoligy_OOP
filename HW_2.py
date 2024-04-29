import pprint


def load_recipes(file_path):
    cook_book = {}

    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    index_lines = 0
    while index_lines < len(lines):
        dish_name = lines[index_lines].strip()
        index_lines += 1

        if not dish_name:
            continue

        ingredient_cnt = int(lines[index_lines].strip())
        index_lines += 1

        ingredients = []
        for i in range(ingredient_cnt):
            ingredient_info = lines[index_lines].strip().split(' | ')
            ingredient_name, quantity, measure = ingredient_info
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
            index_lines += 1

        cook_book[dish_name] = ingredients

    return cook_book


def create_shopping_list(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        else:
            print(
                f"Ошибка: рецепт для '{dish}' отсутствует")

    return shop_list


cook_book = load_recipes('list_of_recipes.txt')

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shopping_list = create_shopping_list(dishes, person_count)
pprint.pprint(shopping_list, width=50)