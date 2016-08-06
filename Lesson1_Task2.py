
# список аудио-записей
audio_list = [{"Beatles": "Yesterday"}, {"Madonna":"Frozzen"}, {"Bonney M": "Money Money Money"}]


def print_audio_list (lst):
	print (lst)

print ("Первый вариант вывода на  печать - одна строка:")
print_audio_list (audio_list)
print ("")

def print_by_line (lst2):
	for each in lst2:
		print (each)

print ("Второй вариант вывода на  печать - построчно:")
print_by_line (audio_list) 
print ("")

def print_by_name (lst3):
	for each in lst3:
		print ("Автор "+ list(each.keys())[0] + "    спел песню " + list(each.values())[0] )

print ("Третий вариант вывода на  печать - поименно:")
print_by_name (audio_list) 
print ("")


audio_list2 = [{'artist': 'Beatles', 'title': 'Yesterday'}]


def print_by_name (lst3):
	for each in lst3:
		print ("Автор "+ each['artist'] + "    спел песню " + each['title'] )

print ("Четвертый вариант вывода на  печать - поименно:")
print_by_name (audio_list2) 