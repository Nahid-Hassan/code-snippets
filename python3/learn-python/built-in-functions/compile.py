"""
    The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).

    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

        * source - a normal string, a byte string, or an AST object
        * filename - file from which the code was read. If it wasn't read from a file, you can give a name yourself
        * mode - Either exec or eval or single.
            * eval - accepts only a single expression.
            * exec - It can take a code block that has  Python statements, class and functions, and  so on.
            * single - if it consists of a single   interactive statement
        * flags (optional) and dont_inherit (optional) - controls which future statements affect the compilation of * the source. Default Value: 0
        * optimize (optional) - optimization level of the compiler. Default value -1.


    The code object returned by compile() method can later be called using methods like: exec() and eval() which will execute dynamically generated Python code.
"""

code_in_string = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
code_object = compile(code_in_string, 'sumstring', 'exec')

exec(code_object)


code_in_string = """
int_number = -20
print(abs(int_number))

float_number = -30.33
print(abs(float_number))

complex_number = (3 - 4j)
print(abs(complex_number)) # 5

for i in range(10):
    print(i*i)
"""
code_in_bytearray = bytearray(code_in_string, 'utf-8')
code_object = compile(source=code_in_bytearray, filename='abs', mode='exec')
exec(code_object)

# this is not normally use in python but it show that the python take your source code as a string and then compile it and return object code and file using exec, eval or single we run the object code.