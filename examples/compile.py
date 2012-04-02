import sys
import py_compile
def main(argv):
	py_compile.compile(argv[1])
if __name__ == '__main__':
	main(sys.argv)
