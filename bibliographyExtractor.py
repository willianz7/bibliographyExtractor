import PySimpleGUI as sg
import re
class TelaPython:
    def __init__(self):
		#layout
        layout = [
            [sg.Text('Reference:', size=(9,0)),sg.Multiline(size=(51, 4), key='reference')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(60,12))]
        ]
		#janela
        self.janela = sg.Window("Extrator de Bibliografia RE").layout(layout)
		#self.button, self.values = self.janela.Read()
    
    def extraiTrecho(self,pattern,livro):
        p = re.compile(pattern)
        m = p.search(livro)
        return (m.group(0))

    def separaautores(self, trecho1, trecho2):
        autores = re.split("\.,\s",trecho1)
        for autor in autores:
            if autor != "":
                print(autor.lstrip() + ".")
        print(trecho2 + "\n")


    def extraiLivro(self,livro):
        titulo = ''
        print('autores: '+self.extraiTrecho("(\w*,\s[A-Z].((\s[A-Z].)+)?,\s*)+\& (([A-Z]{1}[a-z]+), ([A-Z]{1}\. ?)+)",livro))
        #separaautores(extraitrecho("(\w*,\s[A-Z].((\s[A-Z].)+)?,\s*)+\& (([A-Z]{1}[a-z]+), ([A-Z]{1}\. ?)+)"))
        print(f'ano: ' + self.extraiTrecho("\D\d{4}\D",livro))#ano
        titulo = re.split("\.",self.extraiTrecho("[A-Z]{1}[a-z]+\s+([a-z]+\s*)+. (\w+\s*)+",livro)) #titulo
        print(f'titulo: ' + titulo[0])   
        print(f'editora: '+ titulo[1].lstrip()+'\n')
    
        #SEPARANDO AUTORES
        trecho1 = self.extraiTrecho("(\w*,\s[A-Z].((\s[A-Z].)+)?,\s*)+",livro)
        trecho2 = self.extraiTrecho("\& (([A-Z]{1}[a-z]+), ([A-Z]{1}\. ?)+)",livro)
        print(f'autores separados:')
        self.separaautores(trecho1,trecho2)
#
		
    def iniciar(self):
        while True:
            #extrair dados da tela
            self.button, self.values = self.janela.Read()
            reference = self.values['reference']
            self.extraiLivro(reference)
		
tela = TelaPython()
tela.iniciar()