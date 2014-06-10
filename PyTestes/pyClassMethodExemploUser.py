#!/usr/bin/env python
#-*- coding: utf-8 -*-
#https://gist.github.com/fabiocerqueira/1b05352a26892dea6813

class User(object): # Definição da classe User que herda de object(ler sobre new-stye class)
	# seq é um atributo da classe para contar quantas instâncias de User já foram salvas(chamaram o método save)
	seq = 0
	# objects é a lista de instâncias de User que foram salvas(que chamaram o método save).
	# O atributo poderia ter qualquer nome.
	objects = []
	 
	# inicializador, nele são definido os valores iniciais da instânca, no momento da chamada do construtor
	def __init__(self, name, password):
	# inicializando os atributos, id começa com None, pois a instância foi criada ainda não foi salva
		self.id = None
		self.name = name
		self.password = password
	 
	# método save incrementa o atributo de classe que conta quantas instâncias
	# foram salvas e adiciona a instância na lista de objects
	def save(self):
	# self.__class__ acessa a class que criou a instância, assim é possível i
	# acessar o atributo dela seq. Poderia ser usado aqui User.seq, porém caso
	# User fosse herdado, o seq seria o de User e não da classe filha.
		self.__class__.seq += 1
		self.id = self.__class__.seq
	# Da mesma forma que acessamos seq, acessamos objects e é feito um append com a instância.
		self.__class__.objects.append(self)
	 
	# retorna uma representação do objecto como str, usado em conversões para str.
	# Exemplo str(my_user), print my_user
	def __str__(self):
		return self.name
	 
	# retorna uma representação do objeto usada por outros objetos,
	# Exemplo: quando é convertida uma lista de user para string
	def __repr__(self):
		# O self.__class__.__name__ é a forma de acessar o
		# nome da classe que gerou a instância
		return '<{}: {} - {}>'.format(self.__class__.__name__, self.id, self.name)
	 
	# Class method usado para acessar todas as instâncias salvas(chamaram o método save).
	# Aqui usamos um @classmethod, pois faz mais sentindo ser um método de classe do que
	# de instância, pois estamos retornando informações da classe e não de uma instância
	# isolada.
	@classmethod
	def all(cls):
		return cls.objects
 
# Demonstração do uso da nossa classe
if __name__ == '__main__':
	u1 = User('fabio', '12345')
	u2 = User('regis', 'qwerty')
	# Note que nesse print a lista está vazia
	print User.all()
	u1.save()
	u2.save()
	# Após chamar o save para as duas instâncias elas são guardas
	# E o método User.all() retorna essa lista
	print User.all()