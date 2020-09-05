a = int(input('Digite o tamanho do arquivo KB:\n'))
v = int(input('Digite a velocidade da internet em KB/s:\n OBS: 1mb = 1000kb\n'))
print('O arquivo tem {}KB/s e a velocidade da sua internet é {}'.format(a,v))
print('O tempo para fazer o download é {:.0f}Segundos'.format(a/v))
