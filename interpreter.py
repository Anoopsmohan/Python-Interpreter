import sys
import opco
Code=[]
Pc=0
NSTACK=100
NUM=100
stack=[0] * NSTACK
sp=0
NULL=0
const=[]
sim_tab=[0] * NUM
loop_end=0
loop_start=0
class classitem:
	pass

def initcode(b_code):
	length=len(b_code)
	global Code
	for i in range(0, length):
		t = classitem()
	
		Code.append(t)
	
def LOAD_CONST():
	global stack, sp, Pc,Code,const
	index=Code[Pc].operand
	stack[sp]=const[index]
	sp+=1
	Pc+=2


def PRINT_ITEM():
	global stack, sp
	sp-=1
	print stack[sp]
	sp+=1
	
def PRINT_NEWLINE():
	return
 	
def push(num_br):
	global stack, sp
	stack[sp]=num_br
	sp+=1
	
def pop():
	global stack, sp
	sp -=1
	result=stack[sp]
	return result

def STORE_NAME():
	global Pc,Code,sim_tab
	op=Code[Pc].operand
	sim_tab[op]=pop()
	Pc+=2
	
def LOAD_NAME():
	global Code, Pc, sim_tab
	op=Code[Pc].operand
	push(sim_tab[op])
	Pc+=2

def SETUP_LOOP():
	global stack, sp, Pc,Code,sim_tab
	count= Code[Pc].operand
	Pc+=2
	loop_end=Pc+count;
	loop_start=Pc	

def get_val():
	global stack, sp
	sp-=1
	value=stack[sp]
	sp+=1
	return value

 
def JUMP_IF_FALSE():
	global stack, sp, Pc,Code,sim_tab
	if (get_val() == 0):
		loc=Code[Pc].operand
		Pc+=2
		Pc=Pc+loc
	else:
		Pc+=2
	return

def BINARY_ADD():
	push(pop() + pop())

def BINARY_MULTIPLY():
	push(pop() * pop())

def BINARY_SUBTRACT():
	op1=pop()
	op2=pop()
	push(op2 - op1)

def BINARY_DIVIDE():
	op1=pop()
	op2=pop()
	if op1 !=0:
		push ( op2 / op1)
	else:
		print 'Error!! Zero divisor'

def BINARY_MODULO():
	op1=pop()
	op2=pop()
	push(op2 % op1)

def POP_TOP():
	pop()
	return
def JUMP_ABSOLUTE():
	global Code, Pc
	Pc=22 + Code[Pc].operand
	return

def JUMP_FORWARD():
	global Code,Pc
	Pc=Pc+Code[Pc].operand
	return

def POP_BLOCK():
	return

def evaluate(b_code):
	j=22
	i=22
	index=[]
	ip=0
	cp=0
	global Code, const
	while (i< len(b_code)):
		num=b_code[i]
		if num in opco.opcode:
			next=opco.opcode[num][1]
			ins=opco.opcode[num][0]
			if ins == 'LOAD_ATTR':
				b2 = b_code[i+1]
				b1 = b_code[i+2]
				b = (b1 << 8) | b2
				const.append(b)
		i+=1
	const.append(0)

	while (j< len(b_code)):
		
		num = b_code[j]
		if num in opco.opcode:
			next_index=opco.opcode[num][1]
			instr=opco.opcode[num][0]
			if instr != 'RETURN_VALUE':
				Code[j].op=instr
				j+=1
				if next_index:
					b2 = b_code[j]
					b1 = b_code[j+1]
					b = (b1 << 8) | b2
					Code[j].operand=b
					j+=2
							
									
			else:
				return j				


def eval(b_code):
	global Code, Pc,stack,sp
	Pc=evaluate(b_code)
	Code[Pc].op=NULL
	Pc=22
	while Code[Pc].op != NULL:
		tmp = Pc
		Pc = Pc + 1
		exec(Code[tmp].op +'()')
	return stack[0]

def main():
	bcode=sys.argv[1]
	f=open(bcode,'r')
	text=f.read()
	b=text[:4]
	c=text[4:8]
	text=text[8:]
	b_code=[]
	for i in text:
		b_code.append(ord(i))

	magic = (ord(b[0])<<24)|(ord(b[1]) << 16)|(ord(b[2])<<8) | ord(b[3])
	time= (ord(c[0])<<24) | (ord(c[1]) <<16 ) | (ord(c[2]) <<8) | ord(c[3])
	#print "Magic Number :", hex(magic)[2:-1]
	#print "Time Stamp :", hex(time)[2:]

	initcode(b_code)
	eval(b_code)	
	

if __name__=='__main__':
 	main()
