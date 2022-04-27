import os

print ("*****CARANGO VELHO*****")
val = float(input("Digite o valor a ser pago: R$"))
ano = int(input("Digite o ano do veiculo: "))

os.system('clear')

if(ano <= 2010):
  desc1 = val*(35/100)
  desc2 = val - desc1
  print  ("Valor do desconto: R$",desc1)
  print  ("Valor a ser pago: R$",desc2)
elif(ano >= 2011 and ano <= 2015):
  desc3 = val*(25/100)
  desc4 = val - desc3
  print  ("Valor do desconto: R$",desc3)
  print  ("Valor a ser pago: R$",desc4)
elif(ano >= 2016 and ano <= 2020):
  desc5 = val*(15/100)
  desc6 = val - desc5
  print  ("Valor do desconto: R$",desc5)
  print  ("Valor a ser pago: R$",desc6)



