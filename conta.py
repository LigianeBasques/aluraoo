

class Conta:

   def __init__(self,numero, titular, saldo, limite):
       print("Construindo objeto...{}".format(self))
       self.__numero = numero
       self.__titular = titular
       self.__saldo = saldo
       self.__limte = limite
   def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

   def deposita(self,valor):
       self.__saldo += valor
   def saca(self,valor):
       self.__saldo -= valor









