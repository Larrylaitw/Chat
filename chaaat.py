import os #operation system
# 讀取檔案
def read_file(filename):
        products = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip()
                products.append(data)
            return products
#印出使用者內容
def print_result(products):
    print('以下為chat內容:')
    for p in products:
        print(p)
#寫入檔案
def write_file(filename, products):
    with open('chats02.txt', 'w', encoding='utf-8') as f:
        f.write('聊天內容如下->\n')
        print('-----------')
        print('格式修改後:')
        for p in products:
            if '林志龍' in p:
                f.write(p + ': ')
                print(p, ':')
            elif '你傳送了' in p:
                f.write('我: ')
                print('我:')
            else:
                f.write(p + '\n')
                print(p)
        return products

filename = 'chat01.txt'
if os.path.isfile(filename):
    print('Yeah~keep going!')
    products = read_file(filename)
else:
    print('File is not exist')
print_result(products)
write_file('chats02.txt', products)
