"""
DLL++ Advanced Math Library v2.1
Добавлены: deg, rad, sind, cosd, tand
"""

import math
import re

MATH_CONTEXT = {
    "abs": abs, "round": round, "sqrt": math.sqrt,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sind": lambda x: math.sin(math.radians(x)),
    "cosd": lambda x: math.cos(math.radians(x)),
    "tand": lambda x: math.tan(math.radians(x)),
    "deg": math.degrees,
    "rad": math.radians,
    "log": math.log, "log10": math.log10, "exp": math.exp,
    "pi": math.pi, "e": math.e, "pow": pow,
    "ceil": math.ceil, "floor": math.floor
}

def safe_eval(expr, variables):
    expr = re.sub(r'(\d+(\.\d+)?)%', r'(\1*0.01)', expr)
    expr = expr.replace('^', '**')
    for name, val in variables.items():
        if re.match(r'^[a-zA-Z_]\w*$', name):
            expr = re.sub(r'\b' + name + r'\b', str(val), expr)
    allowed = "0123456789+-*/().% ,"
    if not all(c in allowed + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_" for c in expr.replace(' ', '')):
        raise ValueError("Недопустимые символы в выражении.")
    return eval(expr, {"__builtins__": {}}, {**MATH_CONTEXT, **variables})

def execute(cmd):
    import sys
    mod = sys.modules.get("calc.math")
    if not mod or not hasattr(mod, "storage"):
        print("[calc] Ошибка: нет доступа к переменным.")
        return
    vars = mod.storage
    expr = cmd.strip()
    if not expr:
        print("[calc] Введите выражение (например: sind(30) или 45 rad)")
        return
    try:
        result = safe_eval(expr, vars)
        print(f"[calc] {expr} = {result}")
    except Exception as e:
        print(f"[calc] Ошибка: {e}")

def initialize(storage, registry=None):
    import sys
    mod = sys.modules.get("calc.math")
    if mod:
        mod.storage = storage
        mod.registry = registry or {}
