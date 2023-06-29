# Группировка файлов по папкам
import os
import shutil
working_dir = r'C:\Users\maxch\Downloads' # Рабочая директория

# Словарь расширений
d = {'PDF': ['pdf'],
     'Картинки': ['jpg', 'jpeg', 'png', 'cdr', 'bmp', 'raw', 'tiff'],
     'Документы': ['doc', 'docx', 'xls','xlsx', 'ppt', 'pptx', 'txt', 'rtf', 'csv'],
     'Видео': ['avi', 'mkv', 'mpeg', 'mp4', 'mov', 'wmv'],
     'Торренты': ['torrent'],
     'Архивы': ['rar', 'zip', '7z'],
     'Python': ['py'],
     'Программы': ['exe']}

for file in os.listdir(path=working_dir):
     file_source = f'{working_dir}\\{file}'
     flag = False
     if os.path.isdir(f'{working_dir}\\{file}'): # Если попалась папка, пропускаем ее
          flag = True
          continue
     for i in d:
          if file.split('.')[-1].lower() in d[i]: # Если расширений в словаре
               os.makedirs(name=f'{working_dir}\\{i}', exist_ok=True) # Создать папку если ее еще нет
               file_destination = f'{working_dir}\\{i}'
               shutil.move(file_source, file_destination) # Переместить файл
               flag = True
               continue
     if flag == False:
          os.makedirs(name=f'{working_dir}\\Другое', exist_ok=True) # Если файл не попал ни в одну из папок, создать
          # папку Другое
          file_destination = f'{working_dir}\\Другое'
          shutil.move(file_source, file_destination) # Переместить файл
