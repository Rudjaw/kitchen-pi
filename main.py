from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.screen_main import ScreenMain
from screens.screen_draw import ScreenDraw
from kivy.uix.screenmanager import FadeTransition



class KitchenApp(App):
    def build_config(self, config):
        pass
        config.setdefaults('buttonNames', {
            '1': 'Abwasch',
        })

    def build(self):
        #load config file
        config = self.config

        #Create Screens and add them to ScreenManager
        self.screenManager = ScreenManager()
        self.screenManager.add_widget(ScreenMain())
        self.screenManager.add_widget(ScreenDraw())
        return self.screenManager




if __name__ == "__main__":
    KitchenApp().run()
