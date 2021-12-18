import re


'''
Задача:
Написать код (с помощью регулярных выражений и без них) для удаления из строки 
незакрытых скобок вместе с их содержимым, если после них нет закрытых блоков: 
'esdfd((esdf)(esdf' -> 'esdfd((esdf)'. 

Написать тесты для этого кода.
'''

def delete_unclosed_brackets_content(expression):
    '''
    Если следовать приведенному примеру, где закрывающей скобки все равно нет
    'esdfd((esdf)(esdf' -> 'esdfd((esdf)'
    '''

    print("(".join(expression.split('(')[:-1]))


def delete_unclosed_brackets_content_and_close(expression):
    '''
    Но предыдущий пример не имеет разумного применение, т.к. скобку все равно надо закрывать.
    Поэтому без regexp можно втупую плюсануть
    '''

    print(f"Со скобкой: {'('.join(expression.split('(')[:-1]) + ')'}")


def delete_unclosed_brackets_with_regexp(expression):
    '''
    Проверка  скобок регекспом
    '''
    result = re.compile() #TODO Долелать

    print(result)



if __name__ == '__main__':
    delete_unclosed_brackets_content('esdfd((esdf)(esdf')
    delete_unclosed_brackets_content_and_close('esdfd((esdf)(esdf')