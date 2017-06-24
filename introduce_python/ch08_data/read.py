poem = ''
cont = open('relative', 'rt')
chunk = 100

while True:
    fragment = cont.read(chunk)
    if not fragment:
        break
    poem += fragment

cont.close()
print(len(poem))
