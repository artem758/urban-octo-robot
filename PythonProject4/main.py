import os
import sys
import subprocess
import time

# 📌 Список файлов для запуска
modules = [
    "elvirix_llm.py",
    "elvirix_selfcheck.py",
    "bot.py"
]

# 🚀 Запуск всех модулей
def launch_modules():
    processes = []
    for file in modules:
        if os.path.exists(file):
            print(f"🚀 Запускаю: {file}")
            proc = subprocess.Popen([sys.executable, file])
            processes.append(proc)
        else:
            print(f"⚠️ Ошибка: файл {file} не найден!")
    return processes

# 🔄 Бесконечный цикл (ожидание ручного завершения)
def keep_alive():
    try:
        print("\n✅ Все модули запущены. Нажмите **Ctrl+C**, чтобы остановить.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⛔ Остановка всех процессов...")
        for proc in processes:
            proc.terminate()
        print("✅ Все процессы завершены.")

if __name__ == "__main__":
    processes = launch_modules()
    keep_alive()