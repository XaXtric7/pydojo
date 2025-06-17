poem = open(
    "D:\Sarthak\VScode workshop\Python(py) Files\CWH\CH.9 (File I-O)\poems.txt")
x = poem.read()

if 'Twinkle' in x or 'twinkle' in x:
    print("Twinkle is found")
else:
    print("Twinkle is not found")

poem.close()
