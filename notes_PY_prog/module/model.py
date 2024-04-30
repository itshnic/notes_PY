import os
file='note_dir.txt'
path = 'c://Users//Пользователь//Desktop//GeekBR//PHP//phpLesson//OpenServer//domains//notes_PY//notes_PY_prog//bd//'
absolute_path = os.path.abspath(f'{path}{file}')
cache_list = []
SEPARATOR=';'

def to_list(flag:str):
  base_data=[]
  if os.path.isfile(absolute_path):
    with open(absolute_path, flag,encoding='utf-8') as data:
      base_data=[i for i in list(map(lambda x: x.strip().split(SEPARATOR), data))]
  return base_data

def to_file(cache_list, flag):
  with open(absolute_path, flag, encoding='utf-8') as data:
    for i in cache_list:
      data.write(f'{SEPARATOR.join(i)}\n')
  data.close()

def search(cache_list,word):
  item_true = []
  for i in range(len(cache_list)):
      if word.lower() in ' '.join(cache_list[i]).lower():
        item_true.append(cache_list[i])
        print(item_true)
  return item_true