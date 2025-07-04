phones = []

# phones.append('8(495)430-23-97')
# phones.append('+7-4-9-5-43-023-97')
# phones.append('4-3-0-2-3-9-7')
# phones.append('8-495-430')

# phones.append('86406361642')
# phones.append('83341994118')
# phones.append('86406361642')
# phones.append('83341994118')

phones.append(input())
phones.append(input())
phones.append(input())
phones.append(input())

alph = ['0','1','2','3','4','5','6','7','8','9']

phones_normal = []

number = []
for phone in phones:
    for n in reversed(phone):
        if n in alph:
            number.append(n)
    number_normal = ''.join(reversed(number))
    if len(number_normal) == 7 and number_normal[0:4] != '8495':
            number_normal = '8495' + number_normal
    if number_normal[0] == '7':
        number_normal = '8' + number_normal[1::]
    phones_normal.append(number_normal)
    number = []

phone_one = phones_normal[0]
for i in range(1,len(phones_normal)):
    if phone_one == phones_normal[i]:
        print('YES')
    else:
        print('NO')