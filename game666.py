from random import *
from time import *
seed(clock())
from colorama import Fore, Back, Style, init
init()
i = 0
hp = 100
exp = 0
orchp = 150
sgolemhp = 300
goblinhp = 50
life = 1
items1 = ['загадочный ключ','пивная кружка','металлический кастет','стальной кинжал','мешочек с золотом']
items2 = ['огранённый рубин','камень','табличка с непонятным текстом']
items3 = ['сырая рыба','мешочек с золотом','деревянная дубинка','факел']
mana = 0
strenght = 0
agility = 0
intellegence = 0
while 1:
	a = randrange(6)
	print(Fore.YELLOW + 'Ваше имя:' + Style.RESET_ALL)
	q = input()
	break
while 1:
	print(Fore.YELLOW + 'Выберите персонажа:' + Style.RESET_ALL)
	q = int(input(' 1 - Орк\n 2 - Человек\n 3 - Гном\n 4 - Эльф\n 5 - Тролль\n'))
	if q==1:
		print(Fore.YELLOW + 'Орк - Характеристики' + Style.RESET_ALL)
		strenght += 20
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		agility += 15
		print(Fore.GREEN + 'Ловкость ' + Style.RESET_ALL,agility)
		intellegence += 10
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		mana += 0
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==2:
		print(Fore.YELLOW + 'Человек - Характеристики' + Style.RESET_ALL)
		strenght += 15
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		agility += 10
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		intellegence += 20
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		mana += 50
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==3:
		print(Fore.YELLOW + 'Гном - Характеристики' + Style.RESET_ALL)
		strenght += 20
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		agility += 10
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		intellegence += 15
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		mana += 25
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==4:
		print(Fore.YELLOW + 'Эльф - Характеристики' + Style.RESET_ALL)
		strenght += 10
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		agility += 20
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		intellegence += 15
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		mana += 75
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==5:
		print(Fore.YELLOW + 'Тролль - Характеристики' + Style.RESET_ALL)
		strenght += 15
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		agility += 15
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		intellegence += 15
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		mana += 50
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
while 1:
	print(Fore.YELLOW + 'Выберите класс:' + Style.RESET_ALL)
	q = int(input('1 - Воин\n 2 - Маг\n 3 - Лучник\n 4 - Разбойник\n 5 - Чернокнижник\n'))
	if q==1:
		print(Fore.YELLOW + 'Воин - Характеристики (+)' + Style.RESET_ALL)
		strenght += 10
		print(Fore.RED + 'Сила + 10' + Style.RESET_ALL)
		agility += 5
		print(Fore.GREEN + 'Ловкость + 5' + Style.RESET_ALL)
		intellegence += 0
		print(Fore.BLUE + 'Интеллект + 0' + Style.RESET_ALL)
		mana += 0
		print(Fore.BLUE + 'Мана + 0' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Итоговые характеристики:' + Style.RESET_ALL)
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==2:
		print(Fore.YELLOW + 'Маг - Характеристики (+)' + Style.RESET_ALL)
		strenght += 0
		print(Fore.RED + 'Сила + 0' + Style.RESET_ALL)
		agility += 5
		print(Fore.GREEN + 'Ловкость + 5' + Style.RESET_ALL)
		intellegence += 10
		print(Fore.BLUE + 'Интеллект + 10' + Style.RESET_ALL)
		mana += 50
		print(Fore.BLUE + 'Мана + 50' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Итоговые характеристики' + Style.RESET_ALL)
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==3:
		print(Fore.YELLOW + 'Лучник - Характеристики (+)' + Style.RESET_ALL)
		strenght += 5
		print(Fore.RED + 'Сила + 5' + Style.RESET_ALL)
		agility += 5
		print(Fore.GREEN + 'Ловкость + 5' + Style.RESET_ALL)
		intellegence += 5
		print(Fore.BLUE + 'Интеллект + 5' + Style.RESET_ALL)
		mana += 25
		print(Fore.BLUE + 'Мана + 25' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Итоговые характеристики:' + Style.RESET_ALL)
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==4:
		print(Fore.YELLOW + 'Разбойник - Характеристики (+)' + Style.RESET_ALL)
		strenght += 5
		print(Fore.RED + 'Сила + 5' + Style.RESET_ALL)
		agility += 10
		print(Fore.GREEN + 'Ловкость + 10' + Style.RESET_ALL)
		intellegence += 0
		print(Fore.BLUE + 'Интеллект + 0' + Style.RESET_ALL)
		mana += 0
		print(Fore.BLUE + 'Мана + 0' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Итоговые характеристики:' + Style.RESET_ALL)
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
	if q==5:
		print(Fore.YELLOW + 'Чернокнижник - Характеристики (+)' + Style.RESET_ALL)
		strenght += 5
		print(Fore.RED + 'Сила + 5' + Style.RESET_ALL)
		agility += 0
		print(Fore.GREEN + 'Ловкость + 0' + Style.RESET_ALL)
		intellegence +=10
		print(Fore.BLUE + 'Интеллект + 10' + Style.RESET_ALL)
		mana += 50
		print(Fore.BLUE + 'Мана + 50' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Итоговые характеристики:' + Style.RESET_ALL)
		print(Fore.RED + 'Сила ' + Style.RESET_ALL,strenght)
		print(Fore.GREEN + 'Ловкость' + Style.RESET_ALL,agility)
		print(Fore.BLUE + 'Интеллект ' + Style.RESET_ALL,intellegence)
		print(Fore.BLUE + 'Мана' + Style.RESET_ALL,mana)
		break
print(Fore.YELLOW + 'Приключения начинаются...' + Style.RESET_ALL)
while 1:
	a = randrange(4)
	if a==1:
		print(Fore.YELLOW + 'Вы видите орка.' + Style.RESET_ALL)
		q = int(input('1 - Сразиться\n 2 - Карманная кража\n 3 - Уйти\n 4 - Покинуть мир'))
		if q ==2:
			print(Fore.YELLOW + 'При обыске вы обнаружили '+choice(items1))
		elif q==1:
			while 1:
				orchp -=30
				print(Fore.RED + 'Вы ударили орка, его здоровье снизилось до' + Style.RESET_ALL,orchp)
				hp -=10
				if orchp <= 0:
					exp += 100
					print(Fore.YELLOW + 'Вы одолели орка. При обыске вы обнаружили '+choice(items1))
					print(Fore.YELLOW + 'Вы получили опыт +' + Style.RESET_ALL,exp)
					print(Fore.YELLOW + 'Опыт:' + Style.RESET_ALL,exp)
					orchp = 150
					break
				print(Fore.YELLOW + 'Орк ударил вас, ваше здоровье снизилось до' + Style.RESET_ALL,hp)
				if orchp <= 0:
					exp += 100
					print(Fore.YELLOW + 'Вы одолели орка. При обыске вы обнаружили '+choice(items1))
					print(Fore.YELLOW + 'Вы получили опыт +' + Style.RESET_ALL,exp)
					print(Fore.YELLOW + 'Опыт: + ' + Style.RESET_ALL,exp)
					orchp = 150
					break
				if hp <= 0:
					print(Fore.RED + 'Вы умерли.' + Style.RESET_ALL)
					life = 0
					break
		elif q==4:
			print(Fore.RED + 'Игра окончена.' + Style.RESET_ALL)
			break
	if a==2:
		print(Fore.YELLOW + 'Вы видите каменного голема.' + Style.RESET_ALL)
		q = int(input('1 - Сразиться\n 2 - Уйти\n 3 - Покинуть мир'))
		if q==1:
			while 1:
				sgolemhp -=15
				print(Fore.RED + 'Вы ударили голема, его здоровье снизилось до' + Style.RESET_ALL,sgolemhp)
				hp -=50
				if sgolemhp <= 0:
					exp += 2000
					print(Fore.YELLOW + 'Вы одолели голема. После его обыска вы обнаружили '+choice(items2))
					print(Fore.YELLOW + 'Вы получили опыт +2000' + Style.RESET_ALL)
					print(Fore.YELLOW + 'Опыт:' + Style.RESET_ALL,exp)
					sgolemhp = 300
					break
				print(Fore.RED + 'Голем ударил вас, ваше здоровье снизилось до' + Style.RESET_ALL,hp)
				if sgolemhp <= 0:
					exp += 2000
					print(Fore.YELLOW + 'Вы одолели голема. После его обыска вы обнаружили '+choice(items2))
					print(Fore.YELLOW + 'Вы получили опыт +2000' + Style.RESET_ALL)
					print(Fore.YELLOW + 'Опыт:' + Style.RESET_ALL,exp)
					sgolemhp = 300
					break
				if hp <= 0:
					print(Fore.RED + 'Вы умерли.' + Style.RESET_ALL)
					life = 0
					break
		elif q==3:
			print(Fore.RED + 'Игра окончена.')
			break
	if a==3:
		print(Fore.YELLOW + 'Вы наткнулись на враждебного гоблина.' + Style.RESET_ALL)
		q = int(input('1 - Атаковать\n 2 - Убежать\n 3 - Покинуть мир'))
		if q==1:
			while 1:
				goblinhp -=30
				print(Fore.RED + 'Вы ударили гоблина, его здоровье снизилось до' + Style.RESET_ALL,goblinhp)
				hp -=5
				if goblinhp <= 0:
					exp += 50
					print(Fore.YELLOW + 'Вы одолели гоблина. При обыске вы обнаружили '+choice(items3))
					print(Fore.YELLOW + 'Вы получили опыт +50' + Style.RESET_ALL)
					print(Fore.YELLOW + 'Опыт:' + Style.RESET_ALL,exp)
					goblinhp=50
					break
				print(Fore.RED + 'Гоблин ударил вас, ваше здоровье снизилось до' + Style.RESET_ALL,hp)
				if goblinhp <= 0:
					exp += 50
					print(Fore.YELLOW + 'Вы одолели гоблина. При обыске вы обнаружили '+choice(items3))
					print(Fore.YELLOW + 'Вы получили опыт +50' + Style.RESET_ALL)
					print(Fore.YELLOW + 'Опыт:' + Style.RESET_ALL,exp)
					goblinhp=50
					break
				if hp <= 0:
					print(Fore.RED + 'Вы умерли.' + Style.RESET_ALL)
					life = 0
					break
		if q==2:
			print(Fore.YELLOW + 'Вам удалось оторваться от гоблина.' + Style.RESET_ALL)
		if q==3:
			print(Fore.RED + 'Игра окончена.' + Style.RESET_ALL)
			break			
	if life==0:
		print(Fore.RED + 'Игра окончена.' + Style.RESET_ALL)
		break