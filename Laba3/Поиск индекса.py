# TODO Напишите функцию для поиска индекса товара
def suck(items_list, find_item):
    for item_index in range(len(items_list)):
        if items_list[item_index] == find_item:
            return item_index
    return None




items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = suck(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
