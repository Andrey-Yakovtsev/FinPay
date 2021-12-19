'''
Есть таблица phones с полями:
    phone - varchar
    users - int[]   # ТРУДНО ПРЕДСТАВИТЬ СИТУАЦИЮ, когда у одного номера есть несколько пользователей.
                    # Но допустим...

Есть вторая таблица Items
    id serial
    user_id int
    status smallint (3 - не продан, 7 - продан, 5 - резерв) # ЗДЕСЬ ЛУЧШЕ ПРИМЕНИТЬ TYNYINT (0-255)

1. Надо написать запрос который на заданные телефоны возвращает количество проданных вещей.
'''

SELECT COUNT(id) FROM Items WHERE status=7 LEFT JOIN Items ON Items.user_id WHERE Items.user_id IN phones.users


'''
2. Который возвращает в одном запросе количество и проданных, и непроданных.
'''

SELECT COUNT(id) FROM Items WHERE status=7 AND status=3 LEFT JOIN Items ON Items.user_id WHERE Items.user_id IN phones.users



'''
This text for commit which will be deleted after
'''