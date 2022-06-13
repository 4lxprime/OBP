# [+] imports
import random
from colorama import Fore

# [+] var
cr = Fore.RED
cb = Fore.BLUE
cw = Fore.WHITE
cy = Fore.YELLOW
cg = Fore.GREEN
logo = """
    ,o888888o.     8 888888888o   8 888888888o
 . 8888     `88.   8 8888    `88. 8 8888    `88.
,8 8888       `8b  8 8888     `88 8 8888     `88
88 8888        `8b 8 8888     ,88 8 8888     ,88
88 8888         88 8 8888.   ,88' 8 8888.   ,88'
88 8888         88 8 8888888888   8 888888888P'   Par 4lxprime
88 8888        ,8P 8 8888    `88. 8 8888
`8 8888       ,8P  8 8888      88 8 8888
 ` 8888     ,88'   8 8888    ,88' 8 8888
    `8888888P'     8 888888888P   8 8888
"""
# [-] var

# [+] main code
class OBP():
    def __init__(self):
        self.main()
    
    def main(self):
        cmd = input (f"{cw}automatique ou manuel (a/m)> ")
        if cmd == 'a':
            gen_lvl = input(f"{cw}nombre d'identités remarquables dans une meme operation (1->6)> ")
            try: int(gen_lvl)
            except: 
                print(f'{cr}[!] erreur (entrez un nombre) !{cw}')
                self.main()
            try: 
                if int(gen_lvl) == 1:
                    try:
                        if bool(random.getrandbits(1)):
                            if bool(random.getrandbits(1)):
                                print(f' > {self.idr2(etat = False)}')
                            else:
                                print(f' > {self.idr1(etat = False)}')
                        else: 
                            print(f' > {self.idr3(etat = False)}')
                    except: print(f'{cr}[!] erreur 1 !{cw}')
                    
                elif int(gen_lvl) == 2:
                    try:
                        result_i = []
                        for i in range(2):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr3(etat = False))
                            else: 
                                result_i.append(self.idr1(etat = False))
                        calc = f'({result_i[0]})*({result_i[1]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 2 !{cw}')
                    
                elif int(gen_lvl) == 3:
                    try:
                        result_i = []
                        for i in range(3):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr1(etat = False))
                            else: 
                                result_i.append(self.idr3(etat = False))
                        if bool(random.getrandbits(1)): symbole = '+'
                        else: symbole = '-'
                        calc = f'({result_i[0]})*({result_i[1]}){symbole}({result_i[2]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 3 !{cw}')
                
                elif int(gen_lvl) == 4:
                    try: 
                        result_i = []
                        for i in range(4):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr1(etat = False))
                            else: 
                                result_i.append(self.idr3(etat = False))
                        if bool(random.getrandbits(1)): symbole = '+'
                        else: symbole = '-'
                        calc = f'({result_i[0]})*({result_i[1]}){symbole}({result_i[2]})*({result_i[3]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 4 !{cw}')
                
                elif int(gen_lvl) == 5:
                    try:
                        result_i = []
                        for i in range(5):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr1(etat = False))
                            else: 
                                result_i.append(self.idr3(etat = False))
                        if bool(random.getrandbits(1)): symbole = '+'
                        else: symbole = '-'
                        if bool(random.getrandbits(1)): symbole_2 = '+'
                        else: symbole_2 = '-'
                        calc = f'({result_i[0]})*({result_i[1]}){symbole}({result_i[2]})*({result_i[3]}){symbole_2}({result_i[4]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 5 !{cw}')
                
                elif int(gen_lvl) == 6:
                    try:
                        result_i = []
                        for i in range(6):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr1(etat = False))
                            else: 
                                result_i.append(self.idr3(etat = False))
                        if bool(random.getrandbits(1)): symbole = '+'
                        else: symbole = '-'
                        if bool(random.getrandbits(1)): symbole_2 = '+'
                        else: symbole_2 = '-'
                        calc = f'({result_i[0]})*({result_i[1]}){symbole}({result_i[2]})*({result_i[3]}){symbole_2}({result_i[4]})*({result_i[5]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 6 !{cw}')
                
                elif int(gen_lvl) == 18:
                    try:
                        result_i = []
                        for i in range(18):
                            if bool(random.getrandbits(1)):
                                if bool(random.getrandbits(1)):
                                    result_i.append(self.idr2(etat = False))
                                else:
                                    result_i.append(self.idr1(etat = False))
                            else: 
                                result_i.append(self.idr3(etat = False))
                        if bool(random.getrandbits(1)): symbole = '+'
                        else: symbole = '-'
                        if bool(random.getrandbits(1)): symbole_2 = '+'
                        else: symbole_2 = '-'
                        if bool(random.getrandbits(1)): symbole_3 = '+'
                        else: symbole_3 = '-'
                        if bool(random.getrandbits(1)): symbole_4 = '+'
                        else: symbole_4 = '-'
                        if bool(random.getrandbits(1)): symbole_5 = '+'
                        else: symbole_5 = '-'
                        if bool(random.getrandbits(1)): symbole_6 = '+'
                        else: symbole_6 = '-'
                        if bool(random.getrandbits(1)): symbole_7 = '+'
                        else: symbole_7 = '-'
                        if bool(random.getrandbits(1)): symbole_8 = '+'
                        else: symbole_8 = '-'
                        calc = f'({result_i[0]})*({result_i[1]}){symbole}({result_i[2]})*({result_i[3]}){symbole_2}({result_i[4]})*({result_i[5]}){symbole_3}({result_i[6]})*({result_i[7]}){symbole_4}({result_i[8]})*({result_i[9]}){symbole_5}({result_i[10]})*({result_i[11]}){symbole_6}({result_i[12]})*({result_i[13]}){symbole_7}({result_i[14]})*({result_i[15]}){symbole_8}({result_i[16]})*({result_i[17]})'
                        print(f' > {calc}')
                    except: print(f'{cr}[!] erreur 18 !{cw}')
                else: 
                    print(f'{cr}[!] erreur (entrez un nombre valide) !{cw}')
                    self.main()
            except: print(f'{cr}[!] erreur global !{cw}')
        else: 
            print(' - IR1 = (a+b)² = a² + 2ab + b²')
            print(' - IR2 = (a-b)² = a² - 2ab + b² ')
            print(' - IR3 = a² - b² = (a+b)(a-b)')
            idr = input(f'entrez une identité remarquable (1/2/3)> ')
            if idr == '1':
                print(self.idr1(etat = True))
            elif idr == '2':
                print(self.idr2(etat = True))
            elif idr == '3':
                print(self.idr3(etat = True))
            else:
                print(f'{cr}[!] erreur (choisissez une option valide) !{cw}')
                
    # [+] remarquable identity main code
    def idr1(self, etat):
        # (a+b)² = a² + 2ab + b²
        if etat:
            if bool(random.getrandbits(1)): s = '-'
            else: s = ''
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            return f' > ({s}{a}x+{b})²  =>  ({s}{a}x)² + {s}{2*a*b}x + {b}²'
        else:
            if bool(random.getrandbits(1)): s = '-'
            else: s = ''
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            return f'({s}{a}x+{b})²'

    def idr2(self, etat):
        # (a-b)² = a² - 2ab + b² 
        if etat:
            if bool(random.getrandbits(1)): s = '-'
            else: s = ''
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            return f' > ({s}{a}x-{b})²  =>  ({s}{a}x)² - {s}{2*a*b}x + {b}²'
        else:
            if bool(random.getrandbits(1)): s = '-'
            else: s = ''
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            return f'({s}{a}x-{b})²'

    def idr3(self, etat):
        # a² - b² = (a+b)(a-b)
        # (a+b)(a-b) = a² - b²
        if etat:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            if bool(random.getrandbits(1)): 
                return f' > ({a}x)²-{b}²  =>  ({a}x+{b})({a}x-{b})'
            else: 
                return f' > ({a}x+{b})*({a}x-{b})  =>  ({a}x)²-{b}²'
        else:
            a = random.randint(1, 9)*random.randint(1, 9)
            b = random.randint(1, 9)
            if bool(random.getrandbits(1)): 
                return f'({a}x)²-{b}²'
            else: 
                return f'({a}x+{b})*({a}x-{b})'
        
    # [-] remarquable identity main code
    
print(cb + logo + cw)

while True: 
    OBP()

# [+] main code
