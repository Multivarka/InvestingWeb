while True:
    print('enter text')
    text = input()
    with open('test.txt','a',encoding='utf-8') as file:
        file.write(text+'\n')
    print('All OK')
