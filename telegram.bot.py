"""
DLL++ Telegram Bot Builder
Позволяет запустить бота, который выполняет команды DLL++.
Команды бота:
  /start - приветствие
  /help  - список команд
  /calc <выражение> - вычислить через calc.math
  /vars  - показать переменные DLL++
  /run <код> - выполнить системный код DLL++ (например, 1, 15 2, !17 echo Привет)
"""

import asyncio
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Ссылки на объекты DLL++ (будут установлены движком при загрузке)
_storage = {}
_registry = {}
_dynamic_modules = {}   # словарь загруженных библиотек

# Переменные бота
_bot_app = None
_bot_thread = None

# Получаем доступ к окружению DLL++
def initialize(storage, registry=None, dynamic_modules=None):
    global _storage, _registry, _dynamic_modules
    _storage = storage
    _registry = registry or {}
    if dynamic_modules:
        _dynamic_modules = dynamic_modules

# ---------- Обработчики команд бота ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, работающий на DLL++. Используй /help, чтобы узнать, что я умею.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/calc <выр> - вычислить выражение (через calc.math)\n"
        "/vars - показать переменные DLL++\n"
        "/run <код> - выполнить системный код DLL++"
    )

async def calc_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expr = " ".join(context.args)
    if not expr:
        await update.message.reply_text("Пример: /calc 2+2*10%")
        return
    # Попробуем через библиотеку calc.math, если она загружена
    calc_mod = _dynamic_modules.get("calc.math")
    if calc_mod and hasattr(calc_mod, "execute"):
        try:
            # calc.math.execute ожидает строку выражения и может использовать _storage
            result = calc_mod.execute(expr)
            await update.message.reply_text(f"Результат: {result}")
        except Exception as e:
            await update.message.reply_text(f"Ошибка вычисления: {e}")
    else:
        # Запасной встроенный вариант
        try:
            res = eval(expr, {"__builtins__": {}}, dict(_storage))
            await update.message.reply_text(f"Результат: {res}")
        except Exception as e:
            await update.message.reply_text(f"Ошибка: {e}")

async def vars_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Переменные DLL++: {dict(_storage)}")

async def run_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = " ".join(context.args)
    if not code:
        await update.message.reply_text("Укажите код. Пример: /run 15 2")
        return
    # Перенаправляем вывод в строку, чтобы отправить в чат
    import io
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        # Выполняем системный код DLL++ (функция execute_combined должна быть импортирована)
        from dlat import execute_combined   # если dlat.py в sys.path
        execute_combined(code)
        output = sys.stdout.getvalue().strip()
    except Exception as e:
        output = f"Ошибка выполнения: {e}"
    finally:
        sys.stdout = old_stdout
    if not output:
        output = "Команда выполнена."
    await update.message.reply_text(output)

def execute(cmd):
    """
    Команды DLL++:
      telegram.bot=start=ТОКЕН
      telegram.bot=stop
    """
    global _bot_app, _bot_thread
    parts = cmd.split("=", 1)
    if len(parts) < 2:
        print("[telegram.bot] Используйте: telegram.bot=start=ТОКЕН или telegram.bot=stop")
        return
    action, value = parts[0].strip(), parts[1].strip()
    if action == "start":
        token = value
        # Запуск бота в отдельном потоке с event loop
        def bot_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            app = Application.builder().token(token).build()
            app.add_handler(CommandHandler("start", start))
            app.add_handler(CommandHandler("help", help_cmd))
            app.add_handler(CommandHandler("calc", calc_cmd))
            app.add_handler(CommandHandler("vars", vars_cmd))
            app.add_handler(CommandHandler("run", run_cmd))
            global _bot_app
            _bot_app = app
            print("[telegram.bot] Бот запущен. Нажмите Ctrl+C в DLL++ для остановки.")
            app.run_polling()
        if _bot_thread and _bot_thread.is_alive():
            print("[telegram.bot] Бот уже работает.")
            return
        _bot_thread = threading.Thread(target=bot_thread, daemon=True)
        _bot_thread.start()
    elif action == "stop":
        if _bot_app:
            _bot_app.stop_running()
            print("[telegram.bot] Бот остановлен.")
        else:
            print("[telegram.bot] Бот не запущен.")
    else:
        print("[telegram.bot] Неизвестная команда.")