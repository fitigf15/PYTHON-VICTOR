def parser(filepath):
	#NO TIENE SENTIDO AÑADIR DE 5000 EN 5000, porque el fichero solo contiene 5000 items
	#CADA VEZ QUE AÑADIMOS, EN VEZ DE AÑADIR HACEMOS UNA NUEVA LISTA
	userList=ABB()
	with open(filepath,'r') as usersFile:
	    lines=usersFile.readlines()
	    for line in lines:
		disks_played = []
		user_first = line.split("||")
		user_second = map(lambda x: x.split("&&"), user_first)
		user_disks = map(lambda x: x.split("::"), user_second[4])
		bestArtist=Artist("",0)
		for disk in user_disks:
		    artist=Artist(name=disk[0],playedSongs=disk[1])
		    disks_played.append(artist)
		user=User(name=user_second[0][0],gender=user_second[1][0],age=user_second[2][0],country=user_second[3][0],songs_played=disks_played,most_played=Artist(user_second[5][0],user_second[5][1]))
		userList.insert(user,int(float(user.relevance)*1000))	
	return userList
#EJECUCION DE CODIGO
#a=parser("LastFM_small.dat")
#inorderPrint(a)
#preorderPrint(a)
