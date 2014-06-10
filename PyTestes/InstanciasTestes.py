#!/usr/bin/env python
# -*- coding: utf-8 -*-
class A:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class A
 
class B(A):
   __c = 3 # atributo privado
 
   def __init__(self):
     print self.a
     print self.__c
a = A()
print isinstance(a, B) # ''Objeto a'' � uma inst�ncia da ''classe B''? Falso.
 
a = B() # Instanc�a o ''objeto a'' na ''classe B'' e imprime os atributos da classe.
print isinstance(a, B) # ''Objeto a'' � uma inst�ncia da ''classe B''?Verdadeiro.
 
b = B() # Instanc�a o ''objeto b'' na ''classe B'' e imprime os atributos da classe.
print isinstance(b, B) # ''Objeto b'' � uma inst�ncia da ''classe B''? Verdadeiro.
 
b = A() # Instanc�a o ''objeto b'' na ''classe A''.
print isinstance(b, A) # ''Objeto b'' � uma inst�ncia da ''classe A''? Verdadeiro.

