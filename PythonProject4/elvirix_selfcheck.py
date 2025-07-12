import os
import subprocess
import sys
from datetime import datetime

EXCLUDE_FILES = {"main.py", "__init__.py"}
LAUNCHABLE = ["elvirix_llm.py", "elvirix_selfcheck.py", "bot.py"]

def log(msg):
    now = datetime.now().strftime("[%H:%M:%S]")
    print(f"{now} {msg}")

def scan_and_launch():
    processes = []
    for fname in LAUNCHABLE:
        full_path = os.path.join(".", fname)
        if os.path.exists(full_path):
            try:
                log(f"🚀 Запуск: {fname}")
                proc = subprocess.Popen([sys.executable, full_path])
                processes.append(proc)
            except Exception as e:
                log(f"❌ Ошибка запуска {fname}: {e}")
    return processes

if __name__ == "__main__":
    log("🧠 Elviryx Main — тотальный запуск включён")
    running = scan_and_launch()

    try:
        log("📡 Ожидание завершения всех модулей...")
        for proc in running:
            proc.wait()
    except KeyboardInterrupt:
        log("⏹ Принудительное завершение по Ctrl+C")