#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Pessoa(object):
    def __init__(self, nome, sexo):
        super(Pessoa, self).__init__()
        self.nome = nome
        self.sexo = sexo

    @classmethod   
    def valores(self,valor_male):        
        self.FEMALE = valor_male
        self.MALE = 1
        return self.FEMALE

    @staticmethod
    def valoresEstaticos(self,valor_male):        
        self.FEMALE = valor_male
        self.MALE = 11
        return self.FEMALE    

p = Pessoa('Beloni', 'Masc')
p.valoresEstaticos('valor inserido estático','teste')

print (Pessoa.valores('valor inserido classmethod'))
print (p.valores('valor inserido2 classmethod'))


