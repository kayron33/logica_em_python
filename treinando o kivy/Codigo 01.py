# importar o APP, importar o Builder (gui-interface)
#criar o aplicativo
#criar a função build do aplicativo
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text = tarefa, font_size = 30))
        
class Teste(App):
    def build(self):
        return Tarefas(["Fazer compras", "Buscar filho","Molhar a calçada"] , orientation = 'horizontal')
   
Teste().run()