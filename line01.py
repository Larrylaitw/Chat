import os #operation system

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding= 'utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    Vincert_word_count = 0
    Me_word_count = 0
    Vincert_sticker_count = 0
    Me_sticker_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Vincent':
            if s[2] == '貼圖':
                Vincert_sticker_count += 1
            else:
                for m in s[2:]:
                    Vincert_word_count += len(m)
        elif name == '維力':
            if s[2] == '貼圖':
                Me_sticker_count += 1
            else:
                for m in s[2:]:
                    Me_word_count += len(m)
    print('Vincent 共說了', Vincert_word_count, '字')
    print('Vincent 用了', Vincert_sticker_count, '個貼圖')
    print('維力 共說了', Me_word_count, '字')
    print('維力 用了', Me_sticker_count, '個貼圖')

def write_file(filename, lines):
    with open(filename, 'w', encoding= 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    filename = 'line.txt'
    if os.path.isfile(filename):
        print('Yeah~file exist and count words!')
        lines = read_file(filename)
    else:
        print('File is not exist')
    lines = convert(lines)
    #write_file('count.txt', lines)

main()