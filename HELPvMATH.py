#!/usr/bin/python
#cli.py
# -*- coding: utf-8 -*-

import os
import sys
import time as t
import subprocess
import click
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

def clearx():
	if sys.platform == 'linux':
		a = os.system('clear')
		del a
	elif sys.platform == 'win32':
		a = os.system('cls')
		del a
		
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

@click.command()
def main():
	print(color.BLUE +"#  #  #####  #      #####")
	print("#  #  #      #      #    #")
	print("####  ####   #      #####")
	print("#  #  #      #      #")
	print("#  #  #####  #####  #\n")
	print(color.YELLOW +"### ###  #####  #######  #   #")
	print("# # # #  #   #     #     #   #")
	print("#  #  #  #####     #     #####")
	print("#     #  #   #     #     #   #")
	print("#     #  #   #     #     #   #")
	t.sleep(1)
	print (color.GREEN +"\nHelpMath v.0.1 BETA\n")
	print (color.END +"\t [1] Возвести в степень")
	print ("\t [2] Вывести из корня")
	print ("\t [3] FAQ")
	print ("\t [4] Выход\t")
	a = input (color.GREEN +"math-$>> ")	
	if a == "1":
		clearx()
		t.sleep(3)
		subprocess.Popen(['python3', 'l.py', 'argzzz1', 'argzzz2'])
		t.sleep(15)
		clearx()
		main()
	if a == "2":
		clearx()
		t.sleep(2)
		subprocess.Popen(['python3', 'n.py', 'argzzz3', 'argzzz4'])
		t.sleep(10)
		clearx()
		main()
	if a == "3":
		clearx()
		with open('README.md','r') as f:
			print(f.read())
		t.sleep(10)
		clearx()
		main()
	if a == "4" or a == "e" or a == "exit":
		clearx()
		print ("До скорой встречи!")
		t.sleep(1)
		exit()	
	else:
		print (color.FAIL +"НЕВЕРНАЯ КОМАНДА!")
		t.sleep(1)
		clearx()
		main()
if __name__	== "__main__":
	main()
