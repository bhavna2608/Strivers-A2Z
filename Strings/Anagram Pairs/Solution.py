def isAnagram(str1, str2) :
	# write your code here.
	dict_1 = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
	dict_2 = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

	if len(str1) != len(str2):
		return 0
	else:
		for i in range(len(str1)):
			dict_1[str1[i]] += 1
			dict_2[str2[i]] += 1
	
	if dict_1 == dict_2:
		return 1
	else:
		return 0
