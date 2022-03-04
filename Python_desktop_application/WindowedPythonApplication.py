import random

from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Label

class ClearApp(App):

    numberOfGuesses = 0
    number = random.randint(1, 20)


    def build(self):

        self.label = Label(text="I am thinking of a number between 1 and 20.", font_size='30')

        self.box = BoxLayout(orientation='horizontal', spacing=20)

        self.txt = TextInput(hint_text='Write here', size_hint=(.5,.1))

        self.btn = Button(text='Venture a guess', on_press=self.clearText, size_hint=(.1,.1))

        self.box.add_widget(self.txt)

        self.box.add_widget(self.btn)

        self.box.add_widget(self.label)
        return self.box

    def clearText(self, instance):

        self.txt.text = ''

ClearApp().run()