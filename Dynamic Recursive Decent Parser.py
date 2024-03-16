from types import FunctionType
def onlyterminalrule(term):
	global rdp
	rdp=rdp+"\t\tif ("+nonterm+"()):\n\t\t\treturn\n"


def nonterminalrule(nonterm):
	global rdp
	rdp=rdp+"\t\t\t"+nonterm+"()\n"
	
def firstterminalrule(term):
	global rdp
	rdp=rdp+"\t\tif string[lookahead]=='"+term+"':\n\t\t\tmatch('"+term+"')\n"

def terminalrule(term):
	global rdp
	rdp=rdp+"\t\t\tmatch('"+term+"')\n"

def firstnonterminalrule(nonterm):
	global rdp
	rdp=rdp+"\t\tif ("+nonterm+"()):\n"

def epsilonrule(epsilon):
	global rdp
	rdp=rdp+"\t\telse:\n\t\t\treturn\n"

def create(f):
	global rdp
	f = open(f, "r")
	co=f.read()
	col=co.split("\n")
	col.pop()
	col.reverse()
	
	for i in range(0,len(col)):
		V=col[i][0]
		pipearr=[2]
		currentrule=col[i]
		rdp=rdp+"\tdef "+V+"():\n\t\tglobal lookahead\n\t\tglobal string\n"
		for chi in range(0,len(col[i])):
			if col[i][chi]=='|':
				pipearr.append(chi)
		pipearr.append(len(col[i]))
		for pipenumber in range (0,len(pipearr)-1):
			leftofindexrule=pipearr[pipenumber]+1
			rightofindextrule=pipearr[pipenumber+1]
			if currentrule[leftofindexrule]<='Z' and currentrule[leftofindexrule]>='A':
				if rightofindextrule==leftofindexrule+2: #
					onlyterminalrule(currentrule[j])	#
				else:
					firstnonterminalrule(currentrule[leftofindexrule])
					for j in range (leftofindexrule+1,rightofindextrule):
						if currentrule[j]<='Z' and currentrule[j]>='A':
							nonterminalrule(currentrule[j])
						else:
							terminalrule(currentrule[j])
			elif currentrule[leftofindexrule]=='#':
				epsilonrule(currentrule[0])
			else:
				firstterminalrule(currentrule[leftofindexrule])
				for j in range (leftofindexrule+1,rightofindextrule):
					if currentrule[j]<='Z' and currentrule[j]>='A':
						nonterminalrule(currentrule[j])
					else:
						terminalrule(currentrule[j])

print("Welcome to the recursive decent parser")
lookahead=0
rdp="def recursivedecentparser(string):\n"  #recursive decent parser code
rdp=rdp+"\tdef match(ch):\n\t\tglobal lookahead\n\t\tglobal string\n\t\tif string[lookahead] == ch:\n\t\t\tlookahead= lookahead+ 1\n\t\telse:\n\t\t\tprint('ERRROR')\n"    #including match function
#rdp=rdp+"\tdef match(ch):\n\t\tprint('match')\n\t\tglobal lookahead\n\t\tglobal string\n\t\tif string[lookahead] == ch:\n\t\t\tlookahead= lookahead+ 1\n\t\t\tprint(lookahead)\n\t\telse:\n\t\t\tprint('ERRROR')\n"    #including match function
f=input("Enter file name storing the CFG: ")
create(f)
#rdp=rdp+"\tprint(string)\n\tS()\n\tif lookahead==len(string):\n\t\tprint('Success')\n\telse:\n\t\tprint('Failure')"
ss=input("Enter the starting symbol: ")
rdp=rdp+"\t"+ss+"()\n\tif lookahead==len(string):\n\t\tprint('Success, the string is valid')\n\telse:\n\t\tprint('Failure, this string is invalid')\n"
string=input("Enter the string to be checked: ")
file1 = open("myfile.txt", "w")
file1.write(rdp)
rdpcode=compile(rdp, "<int>", "exec")
output=FunctionType(rdpcode.co_consts[0],globals(),"recursivedecentparser")
output(string)

	
