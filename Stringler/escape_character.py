# \'	Single Quote
txt = 'It\'s alright.'
print(txt) 

# \\	Backslash	
txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line
# txt = "Hello\nWorld!"
print(txt)

# \r	Carriage Return	
txt = "Hello\rWorld!"
print(txt) 

# \t	Tab	
txt = "Hello\tWorld!"
print(txt) 

# \b	Backspace	
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

# \ooo	Octal value	
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


# \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
