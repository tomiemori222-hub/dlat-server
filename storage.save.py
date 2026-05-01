import json
import os

DB_PATH = "system_data.json"

def save_data(key, value):
    """Сохраняет значение по ключу в файл"""
    data = {}
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    data[key] = value
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return {key: value}

def get_data():
    """Загружает все сохраненные данные в STORAGE системы"""
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def add_to_list(list_name, item):
    """Добавляет элемент в список (база данных)"""
    data = get_data()
    current_list = data.get(list_name, [])
    if isinstance(current_list, list):
        current_list.append(item)
        save_data(list_name, current_list)
    return {list_name: current_list}