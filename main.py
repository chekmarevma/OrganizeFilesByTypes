# Grouping files by folder
import os
import shutil
working_dir = r'C:\Users\maxch\Downloads' # Work directory

# Extension dictionary
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
     if os.path.isdir(f'{working_dir}\\{file}'): # If a folder comes up, skip it
          flag = True
          continue
     for i in d:
          if file.split('.')[-1].lower() in d[i]: # If the extension in the dictionary
               os.makedirs(name=f'{working_dir}\\{i}', exist_ok=True) # Create a folder if it does not already exist
               file_destination = f'{working_dir}\\{i}'
               shutil.move(file_source, file_destination) # Move the file
               flag = True
               continue
     if flag == False:
          os.makedirs(name=f'{working_dir}\\Другое', exist_ok=True) # If the file does not appear in any of the folders, create a folder Other
          file_destination = f'{working_dir}\\Другое'
          shutil.move(file_source, file_destination) # Move the file
