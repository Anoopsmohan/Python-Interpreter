import sys
import opco
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
	print "Magic Number :", hex(magic)[2:-1]
	print "Time Stamp :", hex(time)[2:]
	

	j=0
	while (j< len(b_code)):
		num = b_code[j]
		if num in opco.opcode:
			next_index=opco.opcode[num][1]
			if next_index:
				b2 = b_code[j+1]
				b1 = b_code[j+2]
				b = (b1 << 8) | b2
				print j, opco.opcode[num][0], '      : ',b
			else:
				print j,opco.opcode[num][0]
		if next_index == None:
			next_index=0
		j+=next_index + 1	
			


if __name__=='__main__':
 	main()
