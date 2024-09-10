operations = {"read": "r", "write": "w", "execute": "x"}


def get_files():
	n = int(input()) # количество файлов
	files = {} 
	for _ in range(n):
		file, *rights = str(input()).split(" ")
		files[file] = rights
	return files


def get_input(files):
	m = int(input())
	for _ in range(m):
		operation, file = str(input()).split(" ")
		if operation not in operations:
			print("Error operation")
			continue
		if file not in files:
			print("File not found")
			continue
		if operations[operation] not in files[file]:
			print("ACESS DENIED")
			continue
		print("OK")


files = get_files()
get_input(files)
