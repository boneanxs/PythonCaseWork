import random
import string
import re

def isNumber(rawStr):
    pat = re.compile('^\d+$')
    if pat.match(rawStr) is None:
        return 0
    else:
        return 1
if __name__ == '__main__':
    num = ''
    while isNumber(num) == 0:
        num = input('Please input the number of codes you need:')
        pass
    digit = ''
    while isNumber(digit) == 0:
        digit = input('Please input your activation code digits:')
        
    for i in range(int(num)):
        result = random.sample(string.ascii_letters + string.digits,int(digit))
        print('the result is ' + ''.join(result))