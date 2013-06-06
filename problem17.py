# -*- coding: utf-8 -*-

dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
        7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
        13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 
        17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
        30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
        80:'eighty', 90:'ninety'}

num = 0

def count_char(i):
    if i in dic:
        return len(dic[i])
    else:
        return len(dic[int(i / 10) * 10]) + len(dic[i - int(i / 10) * 10])

for i in range(1, 1001):
    print i
    if i < 100:
        num += count_char(i)
    elif i < 1000:
        if i % 100 == 0:
            num += len(dic[i/100]) + len('hundred')
        else:
            num += len(dic[i/100]) + len('hundredand') + count_char(i-int(i/100)*100)
    else:
        num += len('onethousand')



print num


