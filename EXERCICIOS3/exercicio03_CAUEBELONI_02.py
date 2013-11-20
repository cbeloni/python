#!/usr/bin/python
#-*- coding: utf-8 -*-
v_user = raw_input("Entre com o nome de usuário: ")
v_pasw = raw_input("Entre com o nome de senha: ")
while v_user == v_pasw:
	print ('\nUsuário não pode ser igual a senha.')
 	v_user = raw_input ("Entre com o nome de usuário: ")
 	v_pasw = raw_input ("digite uma nova senha: ")
