# Number
# Data Type - Integer
a = 1
# Data Type - Floating-point
a = 1.1
# Data Type - Octal: 0o(or O)
a = 0o1
# Data Type - Hexadecimal: 0x(or X)
a = 0x1

# Operator
a + a
a - a
a * a
a / a
a ** a
a % a # 나머지
a // a # 몫

# String
a = "a"
a = 'a'
a = """a"""
a = '''a'''
# cf. """" """ or ''' ''' Multiline input, Comment

# Escape code
a = "\n"
a = "\t"
a = "\\"
a = "\'"
a = "\""

# String Operator
a + a
a * a

# String Indexing: [] in number, -n ~ 0 ~ n
a = "abcd efgh ijkl"
a[1]

# String Slising
a = "abcd efgh ijkl"
b = a[0] + a[1] + a[2] + a[3]
b = a[0:4]
# cf. a[n1, n2] >> n1 <= a < n2

# String Formatting: s - String, c - character, d - integer, f - floating-point
# Stirng Formatting: o - octa, x - hexa, % - Literal
print("asdasd %d adasd %d%%" %(a, 80))













def A(a,b):
    return a+b
