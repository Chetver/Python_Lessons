
import random

# список аудио-записей
audio_list = [{"Beatles": "Yesterday"}, {"Madonna":"Frozzen"}, {"Bonney M": "Money Money Money"}, {"Beatles":"Yellow Submarine"}, {"Madonna":"Else"}]

def decorator (func):
	def wrap():
		print ("~~~~~~~~~~~~~"*5)  # элемент декора: "<~~==\|/==~~>"
		func()
		print ("<~~##+++##~~>"*5)
	return wrap


def print_by_name (lst3):
	for each in lst3:
		print ("Автор "+ list(each.keys())[0] + "    спел песню " + list(each.values())[0] )

print ("Третий вариант вывода на  печать - поименно:")
print_by_name (audio_list) 
print ("")


def count_artists (lst4):
	artists = list()
	for each in lst4:
		artists.append(list(each.keys())[0])
	
	artists_dict  = dict ()
	for each in artists:
		artists_dict[each]  =  artists.count (each)


	print ("Список всех артистов:")
	print (artists)
	print ("")
	print ("Словарь Артистов и кол-во их песен:")
	print (artists_dict)
		
print ("А теперь выполняем задание №3:")
decorator (count_artists(audio_list))

print ("")
# Начинаем выполнять Задание 4 из Практикума.
# Нужно создать функцию test_count_artists, которая будет проверять корректность работы
# функции count_artist

def test_count_artists ():
	#r = input ("Введите размер тестового списка:")
	size_of_list = random.randint(0,100)
	#сгенерим лист из певцов
	list_of_singers = list()
	i = 0
	for i in range(0,size_of_list-1):
		#list_of_singers[i] = "Singer"+ str(i) 
		list_of_singers.append("Singer"+ str(i))

	#сгенерим лист из словарей-пар Певец-Песня
	list_of_tracks = list()
	for i in range(0,size_of_list-1):
		list_of_tracks.append( {random.choice(list_of_singers): 1})
	
	#print (list_of_tracks)

	return list_of_tracks
	


print ('\033[1;32mТеперь будем тестировать как работает функция test_count_artists:\033[1;m')

print ("")
test_count_artists()
print ("")
print_by_name (test_count_artists)
#count_artists (list_of_tracks) 
input("Введите Enter, для выхода!")


#Вопрос к преподам: Блин, не понял я как выпонить это задание ((()))
