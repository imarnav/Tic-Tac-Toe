# import sys
# sys.stdin=open('input.in','r')
# sys.stdout=open('output.out','w')

pos=['-','-','-',
     '-','-','-',
     '-','-','-']

Name_1=str(input())
Name_2=str(input())

class board():
	def display():
		print(pos[0]+'|'+pos[1]+'|'+pos[2])
		print(pos[3]+'|'+pos[4]+'|'+pos[5])
		print(pos[6]+'|'+pos[7]+'|'+pos[8])	


	def entry_1():
		position_1=int(input())-1
		# position_2=int(input())-1
		if pos[position_1]!="-":
			print("Space not available")
		else:
			pos[position_1]='x'
		# if pos[position_2]!="-":
		# 	print("Space not available")
		# else:
		# 	pos[position_2]='o'		
	


	def entry_2():
		# position_1=int(input())-1
		position_2=int(input())-1
		# if pos[position_1]!="-":
		# 	print("Space not available")
		# else:
		# 	pos[position_1]='x'
		if pos[position_2]!="-":
			print("Space not available")
		else:
			pos[position_2]='o'					

			




	def winner():	
		if pos[0]=='x' and pos[1]=='x' and pos[2]=='x':
			return('x')		
		if pos[3]=='x' and pos[4]=='x' and pos[5]=='x':
			return('x')
		if pos[6]=='x' and pos[7]=='x' and pos[8]=='x':
			return('x')
		if pos[0]=='x' and pos[3]=='x' and pos[6]=='x':
			return('x')  
		if pos[1]=='x' and pos[4]=='x' and pos[7]=='x':
			return('x')
		if pos[2]=='x' and pos[5]=='x' and pos[8]=='x':
			return('x')				
		if pos[0]=='x' and pos[4]=='x' and pos[8]=='x':
			return('x')
		if pos[2]=='x' and pos[4]=='x' and pos[6]=='x':
			return('x')					
		if pos[0]=='o' and pos[1]=='o' and pos[2]=='o':
			return('o')		
		if pos[3]=='o' and pos[4]=='o' and pos[5]=='o':
			return('o')
		if pos[6]=='o' and pos[7]=='o' and pos[8]=='o':
			return('o')
		if pos[0]=='o' and pos[3]=='o' and pos[6]=='o':
			return('o')  
		if pos[1]=='o' and pos[4]=='o' and pos[7]=='o':
			return('o')
		if pos[2]=='o' and pos[5]=='o' and pos[8]=='o':
			return('o')				
		if pos[0]=='o' and pos[4]=='o' and pos[8]=='o':
			return('o')
		if pos[2]=='o' and pos[4]=='o' and pos[6]=='o':
			return('o')
	
						


bord=board
win=bord.winner()
while(win!=True):
	print('')
	print(Name_1,"entry")
	bord.entry_1()
	print('')
	bord.display()
	print('')
	print(Name_2,'entry')
	bord.entry_2()
	print('')
	bord.display()
	winner=bord.winner()			
	if winner=='x':
		print(Name_1 + ' ' + "is Winner")
		break
	elif winner=='o':
		print(Name_2 + ' ' + "is Winner")
		break
	elif pos[0]!='-' and pos[1]!='-' and pos[2]!='-' and pos[3]!='-' and pos[4]!='-' and pos[5]!='-' and pos[6]!='-' and pos[7]!='-' and pos[8]!='-':
		print("Match Drawn")