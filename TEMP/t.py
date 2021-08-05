with open('list.txt','r') as f:
    content = f.read()
    content = content[content.find('\n'):]
    print(content)
    成都市