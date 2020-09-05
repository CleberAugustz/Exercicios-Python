n1 = float(input('Digite a primeira nota:\n'))
n2 = float(input('Digite a segunda nota:\n'))
n3 = float(input('Digite a terceira nota:\n'))
m = (n1+n2+n3)/3
m1 = m >= 7 and m < 10
m2 = m < 7
m3 = m == 10
if m1 is True:
    print('Você foi \033[0;34;45mAPROVADO!!!\033[m\nSua Média é {:.1f}'.format(m))
elif m2 is True:
    print('Você foi \033[0;33;44mRESPROVADO!!!\033[m.\nSua média é {:.1f}'.format(m))
elif m3 is True:
    print('Você foi \033[0;34;45APROVADO!!!\033[m com Distinção!! Uuaauu.\nSua méida é {:.1f}'.format(m))