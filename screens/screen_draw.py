from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.uix.widget import Widget

Builder.load_string("""
<ScreenDraw>:
    name: 'draw'
    FloatLayout:
		Draw
		Button:
			color: 0,1,0,1
			font_size: 25
			size_hint: 0.3,0.2
			text: "Back Home"
			on_release: app.root.current = "main"
			pos_hint: {"right":1, "top":1}
""")

class ScreenDraw(Screen):
    pass

class Draw(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]
