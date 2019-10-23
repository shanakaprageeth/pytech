import dis #disassember of python byte code into mnemonics
import marshal, sys, os
import py_compile

command = 'print("Hello World")' # your test command

# simple test function
def testfunc():
	print("Hello World")
	a = 10
	return a

print("---------- print Hello World mnemonics ------")
dis.dis(command)  # mnemonics interpretation of bytecode ex: .pyc bytecode

# get bytecode instructions list
bytecode = dis.Bytecode(testfunc)
# pointer of the function
print("---------- pointer of test function ------")
print(bytecode)
# print instruction opcode list
print("---------- operation names of test function ------")
for instr in bytecode:
    print(instr.opname)
print("---------- mnemonics of test function ------")
# print opcode details of the function
dis.dis(testfunc)
print("---------- compiling python script ------")
# compile python code to generate compiled bytecode .pyc
python_script_name = 'dis_exe.py'
py_compile.compile(python_script_name)

# get initial metadata size
metadata_size = 12 if sys.version_info >= (3, 3) else 8
print("---------- printing mnemonics of the compiled bytecode .pyc ------")
# open the .pyc bytecode
with open(os.path.join('__pycache__',python_script_name.split('py')[0]+'cpython-36.pyc'), "rb") as f:
	# remove initial meta data
    initial_metadata = f.read(metadata_size)
    # capture opcodes
    code = marshal.load(f)

# print opcodes mneonics
dis.dis(code)