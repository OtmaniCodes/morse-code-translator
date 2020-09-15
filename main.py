from kivy.app import App
from kivy.lang.builder import Builder 
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from morse_code import morse_code
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


class MainApp(App):
    def build(self):
        Window.size= 360, 614
        return Builder.load_file('main.kv')

    def change(self, target):
        self.m= self.root.ids.morse_txt
        self.e= self.root.ids.normal_txt
        self.m.text = 'morse code'.title()
        
        try:
            #if: target.isnumeric() or target.isalpha() or target.isspace():   
            res = morse_code(str(target))
            self.m.text = res
        except:
            self.m.text = 'invalid inputs...'

 
if __name__ == "__main__":
    app= MainApp()
    app.run()