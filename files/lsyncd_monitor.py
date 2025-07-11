#!/usr/bin/env python3

#
#uv run --directory /media/aleksei/home/MyProject/python/files lsyncd_monitor.py
#

from loguru import logger
import os
from dotenv import load_dotenv
load_dotenv()

if not os.path.isfile("log/lsyncd_monitor.log"):
    raise(Exception('not file path'))

logger.add("log/lsyncd_monitor.log", enqueue=True, rotation="500 MB",level='INFO')

import subprocess
import sys
import time
from datetime import datetime

# Конфигурация (измените под свои пути)
LSYNCD_LOG = "/var/log/syslog"  # или /var/log/messages
LSYNCD_SOURCE_DIR = os.getenv('LSYNCD_SOURCE_DIR')
LSYNCD_TARGET_DIR = os.getenv('LSYNCD_TARGET_DIR')
LSYNCD_CONF = "/etc/lsyncd.conf"
#TEST_FILE = "lsyncd_test_file.txt"  # Тестовый файл для проверки синхронизации

log_notify = []

def log_message(message,to_notify=False):
    global log_notify
    """Логирование сообщений с временем."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    m = f"[{timestamp}] {message}"
    if to_notify:
        log_notify.append(m)
    logger.debug(m)

def check_lsyncd_service():
    """Проверка статуса службы lsyncd."""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "lsyncd"],
            capture_output=True,
            text=True
        )
        if result.stdout.strip() == "active":
            log_message("✅ Служба lsyncd активна (running).",to_notify=True)
            return True
        else:
            log_message(f"❌ Служба lsyncd НЕ активна: {result.stdout.strip()}",to_notify=True)
            return False
    except Exception as e:
        log_message(f"❌ Ошибка проверки службы lsyncd: {str(e)}",to_notify=True)
        return False

def check_lsyncd_logs():
    """Поиск ошибок в логах lsyncd."""
    try:
        result = subprocess.run(
            ["grep", "-i", "lsyncd", LSYNCD_LOG],
            capture_output=True,
            text=True
        )
        if "error" in result.stdout.lower():
            log_message("❌ В логах lsyncd найдены ошибки:",to_notify=True)
            print(result.stdout)
            return False
        else:
            log_message("✅ В логах lsyncd нет ошибок.",to_notify=True)
            return True
    except Exception as e:
        log_message(f"❌ Ошибка чтения логов: {str(e)}",to_notify=True)
        return False

def check_rsync_diff():
    """Проверка расхождений через rsync (игнорируя вывод директорий)."""
    try:
        result = subprocess.run(
            ["rsync", "-avzi", "--delete", "--dry-run", f"{LSYNCD_SOURCE_DIR}/", f"{LSYNCD_TARGET_DIR}/"],
            capture_output=True,
            text=True
        )
        
        # Разбиваем вывод на строки и фильтруем
        output_lines = result.stdout.splitlines()
        relevant_changes = []
        
        for line in output_lines:
            # Игнорируем служебные строки и пустые строки
            if (
                not line.strip()
                or line.startswith("sending incremental file list")
                or line.startswith("./")
                or line.endswith("/")  # Игнорируем строки, заканчивающиеся на / (папки)
                or line.startswith("cd")  # Игнорируем строки смены директории
            ):
                continue
            
            # Если строка содержит указание на изменение файла (например, ">f+++++++++")
            if any(
                marker in line
                for marker in [">f", "*deleting", ">f+++++++"] #, "cd"
            ):
                #print(f'{line=}')
                relevant_changes.append(line)
        
        if relevant_changes:
            log_message("❌ Обнаружены расхождения между исходной и целевой директорией:",to_notify=True)
            print("\n".join(relevant_changes))
            return False
        else:
            log_message("✅ Расхождений между директориями нет.",to_notify=True)
            return True
            
    except Exception as e:
        log_message(f"❌ Ошибка при проверке rsync: {str(e)}",to_notify=True)
        return False

# def test_file_sync():
#     """Тестовая синхронизация файла."""
#     test_file_path = os.path.join(SOURCE_DIR, TEST_FILE)
#     try:
#         with open(test_file_path, "w") as f:
#             f.write(f"Тест синхронизации {datetime.now()}\n")
        
#         time.sleep(5)  # Ждём синхронизацию
        
#         target_file = os.path.join(TARGET_DIR, TEST_FILE)
#         if os.path.exists(target_file):
#             log_message("✅ Тестовый файл успешно синхронизирован.")
#             os.remove(test_file_path)
#             os.remove(target_file)
#             return True
#         else:
#             log_message("❌ Тестовый файл НЕ синхронизирован!")
#             return False
#     except Exception as e:
#         log_message(f"❌ Ошибка тестовой синхронизации: {str(e)}")
#         return False

def main():
    log_message("=== Начало проверки lsyncd ===")
    
    checks = [
        ("Служба lsyncd", check_lsyncd_service),
        ("Логи lsyncd", check_lsyncd_logs),
        ("Проверка rsync", check_rsync_diff),
        #("Тест синхронизации", test_file_sync),
    ]
    
    all_ok = True
    for name, check_func in checks:
        log_message(f"Проверка: {name}...")
        if not check_func():
            all_ok = False
    
    if all_ok:
        log_message("✅ Все проверки пройдены успешно!",to_notify=True)
    else:
        log_message("❌ Обнаружены проблемы с синхронизацией!",to_notify=True)
    
    log_message("=== Проверка завершена ===")
    #sys.exit(0 if all_ok else 1)

def notify():
    import time
    from notify import notification
    time.sleep(10)
    notification('lsyncd monitor', message='\n'.join(log_notify), app_name='lsyncd monitor',timeout = 10000)

if __name__ == "__main__":
    main()
    notify()