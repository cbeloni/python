#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cherrypy
import sqlite3

#Importar valores da base SQLite
def obterValores():
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    sql =  ''' SELECT * FROM orcamento '''
    resultado = cursor.execute(sql)
    return resultado

class Node(object):
    exposed = True

    def __call__(self):
        return "The node content"


class Root(object):

    def __init__(self):
        self.node = Node()

    @cherrypy.expose
    def index(self):
        dados = list(obterValores())
        return "The index of the root objeto: " + str(dados)

    def page(self):
        return 'This is the "page" content'
    page.exposed = True


if __name__ == '__main__':
    cherrypy.quickstart(Root())