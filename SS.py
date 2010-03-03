"""
Programa grafiskai atvaizduoja skaicius. Iki 10 skaitmenu.
"""


segcode = { '1' : '     ', '2' : ' ### ', '3' : '#   #', '4' : '#    ',
            '5' : '    #', '6' : '  '}
numbers = { '0' : '23232', '1' : '15151', '2' : '25242', '3' : '25252',
            '4' : '13251', '5' : '24252', '6' : '24232', '7' : '25151',
            '8' : '23232', '9' : '23252'}

def seg(num):
    """Isspausdink pateikta skaiciu dideliais skaitmenim."""
    code = ['','','','','']
    numstr = str(num)
    if len(numstr) > 10:
        print ("Per ilgas skaicius")
    for x in range(len(numstr)):
        tmpstr = numstr[x]
        if tmpstr in numbers:
            for y in range (5):
                code[y] = code[y] + numbers[tmpstr][y] + '6'

    for z in range(5):
        line = ''
        for k in range(len(code[0])-1):
            line = line + segcode[code[z][k]]

        print (line)
        if z in (1,3):
            for i in range(2):
                print (line)    
            
        
