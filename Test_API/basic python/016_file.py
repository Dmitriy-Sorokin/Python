# w - Запись новых данных, но с удалением старых

# var = input('Word please : ')
# fw = open('test_doc/file.txt', 'a') # Запись новых данных и помещение в конец файла
# fw.write(var)
# fw.close()


# fw = open('test_doc/file2.txt', 'a')
# fw.write('privet hello world')
# fw.close()

fr = open('test_doc/file.txt', 'r') # Read file
text = fr.read()
fr.close()
print(text)
