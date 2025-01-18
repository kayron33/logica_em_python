# importar o APP, importar o Builder (gui-interface)
#criar o aplicativo
#criar a função build do aplicativo
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text = tarefa))
class Tarefa(BoxLayout):
    def __init__(self,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
class Teste(App):
    def build(self):
        return Tarefas(["Fazer compras", "Buscar filho","Molhar a calçada","12321313","12312312","123123"] )
   
Teste().run()