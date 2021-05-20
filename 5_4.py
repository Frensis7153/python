from re import split

digit_w = ['Раз', 'Два', 'Три', 'Четыре']
digit = ['1', '2', '3', '4']
with open('numbers.txt', 'r', encoding='utf-8') as f1, \
        open('wr_to_f.txt', 'w', encoding='utf-8') as f2:
    for i in range(4):
        line = f1.readline()
        line_split = split('[ - |\n]', line)
        if line_split[2] == digit[i]:
            line_split[0] = digit_w[i]
            line_unit = ''.join(line_split)
            f2.write(line_unit)
            f2.write('\n')
