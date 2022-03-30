documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

command_list = ['s', 'p', 'l', 'a']
command = input('Введите команду: ')

def people(document):
    for d in documents:
        if d['number'] == document:
            return d['name']
    return 'Unknown'


def shelf(document_id):
    for shelf_number, shelf_documents in directories.items():
        if document_id in shelf_documents:
            return (f'Номер полки: {shelf_number}')
    return 'Не найдено'

def my_list():
    for a in documents:
        type = a['type']
        number = a['number']
        name = a['name']
        result = (f'{type} "{number}" "{name}"')
        print(result)
    return

def add_doc(new_doc, new_doc_number, new_doc_name, new_shelf_item):
    new_dict = {"type": new_doc, "number": new_doc_number, "name": new_doc_name}
    exist_values = ''
    for key, value in directories.items():
        if new_shelf_item == key:
            exist_values = directories[f'{new_shelf_item}']

    if len(exist_values):
        exist_values.append(new_doc_number)
        directories[f'{new_shelf_item}'] = exist_values
    else:
        directories[f'{new_shelf_item}'] = [new_doc_number]
    documents.append(new_dict)
    return f'Создан новый список: {new_dict}, Номер полки: {new_shelf_item}'

if command == 'p':
    document = input('Введите номер документа: ')
    result = people(document)
    print(result)

elif command == 's':
    document_id = input('Введите номер документа для поиска на полке: ')
    result = shelf(document_id)
    print(result)

elif command == 'l':
    my_list()

elif command == 'a':
    new_doc = input('Введите название документа: ')
    new_doc_number = input('Введите номер документа: ')
    new_doc_name = input('Введите имя владельца документа: ')
    new_shelf_item = input('Введите номер полки хранения документа: ')
    result = add_doc(new_doc, new_doc_number, new_doc_name, new_shelf_item)
    print(result)
else:
        print('Неизвестная комманда.')





