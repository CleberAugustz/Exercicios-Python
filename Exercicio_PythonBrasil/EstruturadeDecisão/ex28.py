import time
import winsound
print('Seja bem-vindo ao SuperMercado Tabajara\nLista de carnes disponíveis\nFilé-Duplo\nAlcatra\nPicanha\nPara atender todos os clientes, \nestamos vendendo um tipo de carne por cliente sem limite de quantidade!')
c = str(input('Digite o nome da carne deseja:\n')).lower().rstrip()
q = int(input('Quantos Kg?\n'))
p = str(input('Cartão-Tabajara (5% de desconto) ou Dinheiro?\n')).lower().rstrip()
if c in 'filé-duplo':
    if q < 5:
        r = q*4.9
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
    elif q >= 5:
        r = q* 5.8
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
if c in 'alcatra':
    if q < 5:
        r = q*5.90
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
    elif q >= 5:
        r = q*6.80
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
if c in 'picanha':
    if q < 5:
        r = q*6.9
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
    elif q >= 5:
        r = q*7.8
        if p in 'cartão-tabajara':
            r1 = r*0.95
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r1,p))
        elif p in 'dinheiro':
            print('Você comprou\n{} {}kg\nR${:.2f}\nCom {}'.format(c,q,r,p))
time.sleep(1)
print('O Super-Mercado Tabajara Agradece!!\nVolte SEMPRE!!')
winsound.Beep(1000, 500)
winsound.PlaySound('', winsound.SND_FILENAME)


