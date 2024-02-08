from func import load_json_from_file
from func import filter_date
from func import filter_score
from func import sort_obj_from_date
import transction_obj as tr_obj

if __name__ == '__main__':
    path1 = "operations"
    file_name = "operations.json"
    # Считали файл json
    dictionary_data = load_json_from_file(path1, file_name)
    # Создаем список из объектов и заполняем параметры для объекта
    Dict_objs = []
    for item in dictionary_data:
        if len(item) > 0:
            Dict_obj = tr_obj.transaction()
            Dict_obj.set_param_from_json(item)
            Dict_objs.append(Dict_obj)
    # Сортируем полученный список по ключу (по дате)
    Dict_objs.sort(key=sort_obj_from_date)
    #Переворачиваем список
    Dict_objs.reverse()
    Dict_obj_EXECUTED = []
    #Получаем объекты в которых поле item state = "EXECUTED"
    for item in Dict_objs:
        if item.get_state() == "EXECUTED":
            Dict_obj_EXECUTED.append(item)
    Dict_obj_resume = Dict_obj_EXECUTED[0:5]
    print_dict = []
    print("**********************************************************************")
    print("**************СВЕДЕНИЯ О ОПЕРЕЦИЯХ************************************")
    # Далее проходимся по списку и составляем список из 5 элементов
    # Их выводим на печать, а список обнуляем
    for index, item in enumerate(Dict_obj_resume):
        print_dict.append(item)
        if ((index + 1) % 5) == 0:
            for item_2 in print_dict:
                # Печать даты и названия операции
                print(f"{filter_date(item.get_date())} {item.get_description()}")
                # Проверка на наличие поля from и печать перевода откуда и куда
                if item_2.get_from() != None:
                    print(f"{filter_score(item_2.get_from())} -> {filter_score(item_2.get_to())}")
                elif item_2.get_from() == None:
                    print(f"Нет сведений -> {filter_score(item_2.get_to())}")
                # Получаем и печатаем количество денег и в каой валюте
                print(f"{item_2.get_many_cont()} {item_2.get_many_id()}")
                print("")
                print("")
            print("**********************************************************************")
            print("**********************************************************************")
            print_dict = []
    # Далее проверяем остаток в print_dict, если больше 0 значит цифра не делится на 5 и следует вывести остатаок
    # С теми же фильтрами
    if len(print_dict) > 0:
        for item in print_dict:
            print(f"{filter_date(item.get_date())} {item.get_description()}")
            if item_2.get_from() != None:
                print(f"{filter_score(item_2.get_from())} -> {filter_score(item_2.get_to())}")
            elif item_2.get_from() == None:
                print(f"Нет сведений -> {filter_score(item_2.get_to())}")
            print(f"{item_2.get_many_cont()} {item_2.get_many_id()}")
            print("")
            print("")
        print("**********************************************************************")
        print("**********************************************************************")
