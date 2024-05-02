from operator import index
import model
import view
import text

def start_up():
  view.print_message(text.text_items['welcome'])
  answer=0
  while text.command['Выход'] != answer:
    answer = view.panel(text.text_items['panel'],text.text_items['command'], text.command) 
    model.cache_list=model.to_list('r')
    match answer:
      case '1': #Создать
       new_note = view.add_user(text.text_items['notes'], text.text_items['request'])
       model.cache_list.append(new_note)
       model.to_file(model.cache_list,'w')
       view.print_message(f'{text.text_items["added"]}{new_note[1]}')
      case '2': #Изменить
        item=model.search(model.cache_list, view.search(text.text_items['correct']),'index')
        if(item=='NULL'):view.print_message(f'{text.text_items["not_note"]}')
        else:
          new_note = view.add_user(text.text_items['notes'], text.text_items['request'])
          model.cache_list[item]=new_note
          model.to_file(model.cache_list,'w')
          view.print_message(f'{text.text_items["added"]}{new_note[1]}')
        
      case '3': #Найти
        item_true=model.search(model.cache_list, view.search(text.text_items['search_text']))
        view.show_all(item_true, text.text_items['notes'])
      case '4': #Показать_все
        view.show_all(model.cache_list, text.text_items['notes'])
      case '5': #Удалить
        item=model.search(model.cache_list, view.search(text.text_items['remove_request']),'index')
        if(item=='NULL'):view.print_message(f'{text.text_items["not_note"]}')
        else:
          pop_item=model.cache_list.pop(item)
          model.to_file(model.cache_list,'w')
          view.print_message(f'{text.text_items["remove"]}{pop_item[1]}')
      case '9': #Выход
        view.exit(text.text_items['exit'])
      case ' ':
        view.print_message(text.text_items['error_command'])
        