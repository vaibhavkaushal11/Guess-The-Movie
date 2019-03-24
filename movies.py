import random
movies = ["iron man","hulk","thor","bumblebee","transformers","inception","deadpool","xmen","captain marvel","endgame"]


def create_question(movie):
	n=len(movie)
	letters = list(movie)
	temp=[]
	for i in range(n):
		if letters[i]==" ":
			temp.append(" ")
		else:
			temp.append("*")
	qn = "".join(str(x) for x in temp)
	return qn


def is_present(letter,movie):
	c=movie.count(letter)
	if c==0:
		return False
	else:
		return True


def unlock(qn,movie,letter):
	ref=list(movie)
	qn_list=list(qn)
	temp=[]
	n=len(movie)
	for i in range(n):
		if ref[i]==" " or ref[i]==letter:
			temp.append(ref[i])
		else:
			if qn_list[i]=="*":
				temp.append("*")
			else:
				temp.append(ref[i])
	qn_new = "".join(str(x) for x in temp)
	return qn_new


def play():
	p1=input("Enter Player name 1 = ")
	p2=input("Enter player name 2 = ")
	pp1=0
	pp2=0
	turn = 0
	willing = True
	while willing:
		if turn%2==0:
			print(p1,"Your Turn!")
			picked_movie=random.choice(movies)
			qn = create_question(picked_movie) 
			print(qn)
			modified_qn=qn
			not_said = True
			while not_said:
				letter = input("Your Letter = ")
				if is_present(letter,picked_movie):
					modified_qn=unlock(modified_qn,picked_movie,letter)
					print(modified_qn)
					d=int(input("Press 1 to guess or 2 to unlock more!\n"))
					if d==1:
						ans = input("Answer = ")
						if ans == picked_movie:
							print("Right!")
							pp1=pp1+1
							not_said=False
							print(p1,"Score = ",pp1)
							turn = turn+1

						else:
							print("Wrong!")
							not_said=False
				else:
					print(letter,"not found!")
			c=int(input("Press 1 to continue or 0 to Quit\n"))
			if c==0:
				print(p1,"Score = ",pp1)
				print(p2,"Score = ",pp2)
				willing=False

		else:
			print(p2,"Your Turn!")
			picked_movie=random.choice(movies)
			qn = create_question(picked_movie) 
			print(qn)
			modified_qn=qn
			not_said = True
			while not_said:
				letter = input("Your Letter = ")
				if is_present(letter,picked_movie):
					modified_qn=unlock(modified_qn,picked_movie,letter)
					print(modified_qn)
					d=int(input("Press 1 to guess or 2 to unlock more!\n"))
					if d==1:
						ans = input("Answer = ")
						if ans == picked_movie:
							print("Right!")
							pp2=pp2+1
							not_said=False
							print(p2,"Score = ",pp2)
							turn = turn + 1
						else:
							print("Wrong!")
							not_said=False
				else:
					print(letter,"not found!")
			c=int(input("Press 1 to continue or 0 to Quit\n"))
			if c==0:
				print(p1,"Score = ",pp1)
				print(p2,"Score = ",pp2)
				willing=False

play()