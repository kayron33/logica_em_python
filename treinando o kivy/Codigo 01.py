# importar o APP, importar o Builder (gui-interface)
#criar o aplicativo
#criar a função build do aplicativo
from kivy.app import App
from kivy.lang import Builder


GUI = Builder.load_file("front-end.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI
    
MeuAplicativo().run()
    