def approxName(keyword, actual):
	keyword = keyword.lower()
	actual = actual.lower()

	i = 0
	for j in range(len(actual)): 
		if i >= len(keyword):
			break
		if keyword[i] == actual[j]:
#			print(f'key[{i}]: {keyword[i]}\nact[{j}]:{actual[j]}\n')
			i += 1

	return i == len(keyword)

# def main():
# 	act = "Gaunt's Ghosts"
# 	key = "Charadon"
# 	print(act)
# 	print(key)
# 	print(approxName(key, act))

# if __name__ == main():
# 	main()

