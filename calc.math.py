"""
DLL++ Math Library - безопасное вычисление арифметических выражений.
Использует переменные из STORAGE.
"""

def evaluate(expr, variables):
    # Разрешённые символы: цифры, операторы, скобки, пробелы, точка, запятая для чисел
    import re
    # Заменяем имена переменных на их значения (если есть в variables)
    # Простой парсинг: разрешаем только безопасные символы
    allowed = set("0123456789+-*/().% ,")
    # Проверим, что в выражении нет запрещённых символов после подстановки переменных
    test_expr = expr
    for var, val in variables.items():
        # Имена переменных должны состоять из букв/цифр/_
        if re.match(r'^[a-zA-Z_]\w*$', var):
            test_expr = re.sub(r'\b' + var + r'\b', str(val), test_expr)
    if not all(c in allowed for c in test_expr.replace(' ', '')):
        raise ValueError("Недопустимые символы в выражении после подстановки переменных.")
    # Вычисляем с пустыми builtins
    return eval(test_expr, {"__builtins__": {}}, {})

def execute(cmd):
    """
    cmd: математическое выражение, можно использовать переменные из STORAGE (если они переданы)
    Перед вычислением библиотека должна получить доступ к STORAGE через initialize.
    """
    # STORAGE будет передан глобально через initialize
    from sys import modules
    this_mod = modules.get("calc.math")
    if not this_mod or not hasattr(this_mod, "storage"):
        print("[calc] Ошибка: нет доступа к переменным. Сначала загрузите библиотеку и вызовите initialize.")
        return
    vars = this_mod.storage
    try:
        result = evaluate(cmd.strip(), vars)
        print(f"[calc] {cmd} = {result}")
    except Exception as e:
        print(f"[calc] Ошибка: {e}")

# Функция, вызываемая движком при загрузке библиотеки для передачи объектов
def initialize(storage, registry=None):
    import sys
    mod = sys.modules.get("calc.math")
    if mod:
        mod.storage = storage
        mod.registry = registry or {}
