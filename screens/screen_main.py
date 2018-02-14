from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.uix.widget import Widget

Builder.load_string("""
<ScreenMain>:
    name: 'main'
    Button:
		on_release: app.root.current = "draw"
		text: "to draw"
		font_size: 50
""")

class ScreenMain(Screen):

    pass

class Buttons(Widget):
    def build(self):
        mainLayout = BoxLayout(orientation='vertical', spacing=20)
        upperRow = BoxLayout(orientation='horizontal', spacing=20)
        lowerRow = BoxLayout(orientation='horizontal', spacing=20)

        mainLayout.add_widget(upperRow)
        mainLayout.add_widget(lowerRow)


        btn11 = Button(text='11', background_color=(0, 0, 1, 1),font_size=20)
        btn12 = Button(text='12', background_color=(0, 0, 1, 1),font_size=20)

        btn21 = Button(text='21', background_color=(0, 0, 1, 1),font_size=20)
        btn22 = Button(text='22', background_color=(0, 0, 1, 1),font_size=20)
        upperRow.add_widget(btn11)
        upperRow.add_widget(btn12)

        lowerRow.add_widget(btn21)
        lowerRow.add_widget(btn22)

        #btn1 = Button(text='%d' % int((config.get('section', 'test')),), background_color=(0, 0, 1, 1),font_size=150)
        self.parent.parent.add_Widget(mainLayout)
        self.parent.update()
