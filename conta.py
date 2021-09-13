

class Conta:

   def __init__(self,numero, titular, saldo, limite):
       print("Construindo objeto...{}".format(self))
       self.numero = numero
       self.titular = titular
       self.saldo = saldo
       self.limte = limite
   def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo,self.titular))






