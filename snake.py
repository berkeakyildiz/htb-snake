#
# Created by Berke Akyıldız on 21/June/2019
#

import random
lr = '\x64'
print('''
___________.__               _________              __           
\__    ___/|  |__   ____    /   _____/ ____ _____  |  | __ ____  
  |    |   |  |  \_/ __ \   \_____  \ /    \\__  \ |  |/ // __ \ 
  |    |   |   Y  \  ___/   /        \   |  \/ __ \|    <\  ___/ 
  |____|   |___|  /\___  > /_______  /___|  (____  /__|_ \\___  >
                \/     \/          \/     \/     \/     \/    \/ 

''')
chains = [0x74, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x74, 0x72, 0x6f, 0x6c, 0x6c]
db = '\x6e'
ef = '\x63'
chars = []
keys = [0x70, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x21, 0x21]
#length of keys: 10
nn = '\x61'
lock_pick = random.randint(0, 0x3e8)
lock = lock_pick * 2
password = [0x69, 0x74, 0x73, 0x20, 0x6e, 0x6f, 0x74, 0x20, 0x74, 0x68, 0x61, 0x74, 0x20, 0x65, 0x61, 0x73, 0x79]
#password: ITS NOT THAT EASY
lock = lock + 10
ty = '\x61'
lock = lock / 2
auth = [0x6b, 0x65, 0x65, 0x70, 0x20, 0x74, 0x72, 0x79, 0x69, 0x6e, 0x67]
lock = lock - lock_pick
gh = '\x6e'
print('The Snake Created by 3XPL017')
print('Your number is ' + str(lock_pick))
print('Lock is : ' + str(lock))
print('keys are: ' + '\x70' + '\x61' + '\x73' + '\x73' + '\x77' + '\x6f' + '\x72' + '\x64' + '\x21' + '\x21')
print('chains are: ' + '\x74' + '\x68' + '\x69' + '\x73'+'\x20'+'\x69'+'\x73'+'\x20'+'\x61'+'\x20'+'\x74'+'\x72'+'\x6f'+'\x6c'+'\x6c')

for key in keys:
    keys_encrypt = lock ^ key
    chars.append(keys_encrypt)
for chain in chains:
    chains_encrypt = chain + 0xA #65
    chars.append(chains_encrypt)
#chars: udvvrjwa$$^rs]*s)*k*^\yvv
#keys_encrypted = udvvrjwa$$
#chains_encrypted = ^rs]*s)*k*^\yvv
for i in range(10):
    keys_decrypt = 5 ^ chars[i]
    print('keys decrypt ' + str(chr(keys_decrypt%128)))
for i in range(15):
    chains_decrypt = chars[10+i] - 0xA
    print('chains decrypt ' + str(chr(chains_decrypt)))
aa = '\x61'
rr = '\x6f'
slither = aa + db + nn + ef + rr + gh + lr + ty
print('Authentication required')
print('')
user_input = input('Enter your username\n')
if user_input == slither:
    pass

else:
    print ('Wrong username try harder')
    exit()
pass_input = input('Enter your password\n')
for passes in pass_input:
    for char in chars:
        if passes == str(chr(char)):
            print('Good Job')
            break
        else:
            print('Wrong password try harder')
            exit(0)
    break