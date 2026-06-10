#Данное Свободное Программное Обеспечение распространяется по лицензии GPL-3.0-only или GPL-3.0-or-later
#Вы имеете право копировать, изменять, распространять, взимать плату за физический акт передачи копии, и вы можете по своему усмотрению предлагать гарантийную защиту в обмен на плату
#ДЛЯ ИСПОЛЬЗОВАНИЯ ДАННОГО СВОБОДНОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ВАМ НЕ ТРЕБУЕТСЯ ПРИНЯТИЕ ЛИЦЕНЗИИ Gnu GPL v3.0 или более поздней версии
#В СЛУЧАЕ РАСПРОСТРАНЕНИЯ ОРИГИНАЛЬНОЙ ПРОГРАММЫ И/ИЛИ МОДЕРНИЗИРОВАННОЙ ВЕРСИИ И/ИЛИ ИСПОЛЬЗОВАНИЕ ИСХОДНИКОВ В СВОЕЙ ПРОГРАММЕ, ВЫ ОБЯЗАНЫ ЗАДОКУМЕНТИРОВАТЬ ВСЕ ИЗМЕНЕНИЯ В КОДЕ И ПРЕДОСТАВИТЬ ПОЛЬЗОВАТЕЛЯМ ВОЗМОЖНОСТЬ ПОЛУЧИТЬ ИСХОДНИКИ ВАШЕЙ КОПИИ ПРОГРАММЫ, А ТАКЖЕ УКАЗАТЬ АВТОРСТВО ДАННОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
#ПРИ РАСПРОСТРАНЕНИИ ПРОГРАММЫ ВЫ ОБЯЗАНЫ ПРЕДОСТАВИТЬ ВСЕ ТЕЖЕ ПРАВА ПОЛЬЗОВАТЕЛЮ ЧТО И МЫ ВАМ, А ТАКЖЕ ЛИЦЕНЗИЯ GPL v3
#Прочитать полную версию лицензии вы можете по ссылке Фонда Свободного Программного Обеспечения - https://www.gnu.org/licenses/gpl-3.0.html
#Или в файле COPYING.txt в архиве с установщиком
#Copyleft 🄯 NEO Organization, Departament K 2026
#Coded by @AnonimNEO (Telegram)

#Интерфейс
from tkinter import messagebox
#Работа с процессами
import win32process
import win32gui
import psutil
#Логирование
from loguru import logger
#Работа с файлами
import os
#Паузы сканирования
import time

from OF import get_user_name
from RS import random_string

anti_nhelper_version = "0.1.1 Beta"

def kill_process_by_name(process_name):
    #Проходим по всем запущенным процессам
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if process_name.lower() in proc.info["name"].lower():
                try:
                    p = psutil.Process(proc.info["pid"])
                    exe_file = p.exe()
                    p.kill()
                    p.wait()
                    logger.info(f"AN - Процесс с именем {proc.info["name"]} (PID:{proc.info["pid"]}) - убит.")
                except Exception as e:
                    logger.exception(f"AN - Ошибка при закрытии процесса с именем {proc.info["name"]} (PID:{proc.info["pid"]})")

                try:
                    os.remove(exe_file)
                    logger.info(f"AN - Файл процесса с именем {proc.info["name"]} - удалён.")
                except Exception as e:
                    logger.exception(f"AN - Ошибка при удалении исполняемого файла процесса с именем {proc.info["name"]} (PID:{proc.info["pid"]})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        except Exception as e:
            logger.exception(f"AN - Ошибка при закрытии процесса по имени {proc.info["name"]} (PID:{proc.info["pid"]})")



def kill_some_process_by_name(process_name_list):
    for process_name in process_name_list:
        kill_process_by_name(process_name)



def get_folder_names(target_path):
    try:
        #Проверяем, существует ли указанный путь
        if os.path.exists(target_path):
            #Получаем список всех объектов и фильтруем только папки
            folders = [name for name in os.listdir(target_path) if os.path.isdir(os.path.join(target_path, name))]
            return folders
        else:
            return 0
    except Exception as e:
        logger.exception(f"AN - неизвестная ошибка при переборе каталогов")
        return 0



def DOP(debug_mode=False):
    net_path = r"C:\Users\Adminus\AppData\Local\Temp\.net"

    folder_list = get_folder_names(net_path)

    if isinstance(folder_list, list):
        kill_some_process_by_name(folder_list)
        for i in folder_list:
            try:
                os.remove(f"{net_path}\\{folder_list[i]}")
                logger.success(f"AN - Каталог {net_path}\\{folder_list[i]} удалён.")
            except Exception as e:
                #logger.error(f"AN - ошибка при удалении подкаталога в {net_path}:\n{e}")
                pass

    dirs = [r"C:\Users\Adminus\AppData\Local\NHelperV3.4", r"C:\Users\Adminus\AppData\Local\NHelperV4", r"C:\Users\Adminus\AppData\Local\NHelperV4.1", r"C:\Users\Adminus\AppData\Local\NHelperV4.2"]

    for dir in dirs:
        try:
            os.remove(dir)
        except:
            pass

if __name__ == "__main__":
    logger.info(f"AntiNHelper v{anti_nhelper_version}")
    logger.info("Настройка логирования...")
    logger.add(f"AN_log.txt", format="{time} {level} {message}", rotation="10 MB", compression="zip")
    from elevate import elevate
    elevate()
    global user_name
    user_name = get_user_name()
    logger.success("AN - Успешная подготовка к работе, запуск...")
    while True:
        DOP(False)
        logger.info("AN - Цикл завершён, повтор...")
        time.sleep(0.5)