import vk
from datetime import datetime
import os

if __name__ == "__main__":
    token = ""  # Сервисный ключ доступа
    session = vk.Session(access_token=token)  # Авторизация
    vk_api = vk.API(session)


def get_members(groupid):  # Функция формирования базы участников сообщества в виде списка
    first = vk_api.groups.getMembers(group_id=groupid, v=5.124, fields = 'bdate, universities')  # Первое выполнение метода
    data = first["items"]  # Присваиваем переменной первую тысячу id'шников
    count = first["count"] // 1000  # Присваиваем переменной количество тысяч участников
    # С каждым проходом цикла смещение offset увеличивается на тысячу
    # и еще тысяча id'шников добавляется к нашему списку.
    #data = []
    for i in range(1, count+1):
        x = vk_api.groups.getMembers(group_id=groupid, v=5.124, offset = i*1000, fields = 'bdate, universities')["items"]
        #for item in vk_api.users.get(user_ids = x, v = 5.124):
            #data.append(item['response']['id'])
        data = data + x
    return data


poetry = get_members('groupid')


def func(data): #убираем закрытые и мертвые страницы
    c = []

    for item in data:
        try:
            if item['is_closed'] == 0:
                c.append(item)
                #c.append(item['id'])
        except TypeError:
            continue
        except KeyError:
            #удаленные страницы
            continue
    return c


filt_data = func(poetry)



def get_bdate(bdate): # примет дату и в ответ даст 1 если дата укладывается в ближайшие 3 недели либо 0
    string = ''
    left = datetime.strptime('15.11', '%d.%m') # здесь указываем левую границу вр интервала
    right = datetime.strptime('10.12', '%d.%m')
    c = 0
    for k in bdate:
        if k == '.':
            c += 1
            if c == 2:
                break
        string += str(k)
    date = datetime.strptime(string, '%d.%m')
    #print(date)
    if date>=left and date<=right:
        return 1
    else:
        return 0

def sovp(a,b):
    for i in a:
        for k in b:
            if k == i:
                return 1


def uni_fr(_user):
    # проверяем есть ли вуз у человека
    try:
        # unis = _user['universities']
        uni_gen = []
        for k in range(len(_user['universities'])):
            uni_gen.append(_user['universities'][k]['name'])

        if uni_gen == []:
            return 0

        # print(uni_gen)

    except KeyError:  # если нет, скипаем всю ф-ю
        return 0
    # если все таки есть вуз, начинаем майнить всех друзей из этого вуза
    friends = vk_api.friends.get(user_id=_user['id'], v=5.124, fields='bdate,universities')['items']
    c = 0

    for i in range(len(friends)):
        try:
            uni_soft = []
            for l in range(len(friends[i]['universities'])):
                uni_soft.append(friends[i]['universities'][l]['name'])
            if sovp(uni_gen, uni_soft) == 1 and get_bdate(friends[i]['bdate']) == 1:
                c += 1
                # print(friends[i]['id'])
        except KeyError:
            pass
    return c


def family_survey(_user):
    friends = vk_api.friends.get(user_id=_user['id'], v=5.124, fields='bdate')['items']
    c = 0

    general_name = _user['last_name']  # имя юзера
    # print(general_name)
    soft_name = []  # массив под имена его друзей
    # заполним массив
    c = 0
    for i in range(len(friends)):
        try:
            item = friends[i]['last_name']
            if general_name.startswith(item[:len(item) - 2]) and item.startswith(
                    general_name[:len(general_name) - 2]) and get_bdate(friends[i]['bdate']) == 1:
                # soft_name.append(friends[i])
                c += 1
        except KeyError:
            pass
    return c


def total_friends(_user):
    friends = vk_api.friends.get(user_id = _user['id'], v = 5.124, fields = 'bdate')['items']
    total = 0
    for item in friends:
        try:
            total += 1
        except KeyError:
            pass
    return total



def u_and_f(_user): #выводит количество совпадений по признаку семьи и университета для конкретного пользователя
    total = total_friends(_user)
    c = (family_survey(_user)+uni_fr(_user))*100/total
    return c


arr = []
# for i in range(len(filt_data)):
for i in range(len(filt_data)):
    # print(i)
    if i % 100 == 0:
        print(str(i) + ' из ' + str(len(filt_data)) + '   arr: ' + str(len(arr)))
    try:
        z = u_and_f(filt_data[i])
        if z >= 0.23:  # интервал рейтинга для каждого пользователя. Чем она выше, тем меньше будет arr[]
            arr.append(filt_data[i]['id'])


    except KeyError:
        pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except VkAPIError:
        pass
print(str(len(filt_data)) + ' из ' + str(len(filt_data)) + '   arr: ' + str(len(arr)))



def u_and_f_forcheck(_user): #выводит количество совпадений по признаку семьи и университета для конкретного пользователя
    c = family_survey(_user)+uni_fr(_user)
    return c
def check_function(_id):
    us = vk_api.users.get(user_id = _id, v = 5.124, fields = 'city, bdate,universities')
    #print(us[0])
    print('c: ' + str(u_and_f_forcheck(us[0])))





status_arr = []
for item in arr:
    try:
        arr_user = vk_api.users.get(user_id=item, v=5.124, fields='status')
        status = arr_user[0]['status']
        # print(status)
        if status.find('ig') != -1 or status.find('inst') != -1 or status.find('instagram') != -1 or status.find(
                '@') != -1 \
                or status.find('_') != -1:
            status_arr.append(str(status))

    except ValueError:
        pass
    except KeyError:
        pass
f = open('ig_status.txt', 'w')
for item in status_arr:
    print(item)
    for i in range(len(item)):
        try:
            f.write(str(item[i]))
        except UnicodeEncodeError:
            pass
    f.write('\n')
f.close()
