import urllib

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

print (color.END +"Введите число, которое хотите возвести в степень:\n")
Lp = int(input(color.GREEN +"math-$>> "))
print (color.END +"\nВ какую степень хотите возвести?:\n")
Lpl = int(input(color.GREEN +"math-$>> "))
if Lpl == 2:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp )
if Lpl == 3:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp )
if Lpl == 4:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp * Lp )
if Lpl == 5:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp * Lp * Lp )
if Lpl == 6:
	print (color.END +"\nВаш ответ равен:\n")	
	print ( Lp * Lp * Lp * Lp * Lp * Lp )
if Lpl == 7:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp * Lp * Lp * Lp * Lp )
if Lpl == 8:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp * Lp * Lp * Lp * Lp * Lp )
if Lpl == 9:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp* Lp * Lp * Lp * Lp * Lp * Lp * Lp )
if Lpl == 10:
	print (color.END +"\nВаш ответ равен:\n")
	print ( Lp * Lp * Lp * Lp * Lp * Lp * Lp * Lp * Lp * Lp )
