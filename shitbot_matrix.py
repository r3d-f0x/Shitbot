import simplematrixbotlib as botlib
from secret import matrix_3054_username
from secret import matrix_3054_password

creds = botlib.Creds('https://matrix.7.62x54r.ru', matrix_3054_username, matrix_3054_password)
bot = botlib.Bot(creds)

def main():
	print('Matrix WKND Bot')
	bot.run()

if __name__ == '__main__':
	main()
