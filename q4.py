class Car:
    def _init_(self, quilometros):
        self.quilometros=quilometros
        self.gasosa = 0

    def obterGasolina(self):
        print('{:.3f}litros de gasolina disponivel'.format(self.gasosa))
 
    def adicionarGasolina(self, acresGasosa):
        self.gasosa = self.gasosa + acresgasosa

    def andar(self, km):

        if (km/self.quilometros) <= self.gasosa:||
            self.gasosa = self.gasosa - (km/self.quilometros)
        else:
            quilometrosF = self.quilometros * self.gasosa
            self.gasosa = 0
            
            print('A gasolina acabou, você andou {}km e ainda pode andar {:.3f}km'.format(quilometrosF, quilometros - quilometrosF))
