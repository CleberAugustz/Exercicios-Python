s = int(input('Digite O valor do seu salário:\n OBS: Faça no seguinte formato! 1000 ou 1280\n'))
if s <= 280:
    s20 = s*1.20
    s20a = s20 - s
    print('Seu salário atual é R${} e teve um aumento de 20%-R${:.2f}, passando a ser R${:.2f}'.format(s,s20a,s20))
elif s > 280 and s <= 700:
    s15 = s*1.15
    s15a = s15 - s
    print('Seu salário atual é R${} e teve um aumento de 15%-R${:.2f}, passando a ser R${:.2f}'.format(s,s15a,s15))
elif s > 700 and s <= 1500:
    s10 = s*1.10
    s10a = s10 - s
    print('Seu salário atual é R${} e teve um aumento de 10%-R${:.2f}, passando a ser R${:.2f}'.format(s,s10a,s10))
elif s > 1500:
    s05 = s*1.05
    s05a = s05 - s
    print('Seu salário atual é R${} e teve um aumento de 5%-R${:.2f}, passando a ser R${:.2f}'.format(s,s05a,s05))