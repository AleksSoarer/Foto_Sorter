import os

path = r'Z:\Fotoset'
#total_size = 0
#path, dirs, files = next(os.walk(path))
#for f in files:
#    fp = os.path.join(path, f)
#    total_size += os.path.getsize(fp)
#    print('1', fp)
fotos = []

for address, dirs, files in os.walk('Z:\Fotoset'):
    for name in files:
        print(os.path.join(address, name))

        if address == 'Z:\Fotoset\Khakassia_big':
            fotos.append(name)

print(fotos)
#print('Размер каталога (в Кб): ', total_size / 1024)
#print('Количество подкаталогов: ', len(dirs))
#print('Количество файлов: ', len(files))