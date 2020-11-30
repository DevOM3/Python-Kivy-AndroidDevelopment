from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader


class PianoButtons(GridLayout):

    def __init__(self, **kwargs):
        super(PianoButtons, self).__init__(**kwargs)

        self.cols = 1
        self.rows = 8

        def sa(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def re(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def ga(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def ma(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def pa(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def dha(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def ni(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        def saa(self):
            sound = SoundLoader.load("01 Patola (feat Bohemia) (SongsMp3.Com) (SongsMp3.Com).mp3")

        self.btn1 = Button(background_color=[0, 0, 0, 1])
        self.add_widget(self.btn1)
        self.btn1.bind(on_press=sa)

        self.btn2 = Button(background_color=[255, 255, 255, 1])
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=re)

        self.btn3 = Button(background_color=[0, 0, 0, 1])
        self.add_widget(self.btn3)
        self.btn3.bind(on_press=ga)

        self.btn4 = Button(background_color=[255, 255, 255, 1])
        self.add_widget(self.btn4)
        self.btn4.bind(on_press=ma)

        self.btn5 = Button(background_color=[0, 0, 0, 1])
        self.add_widget(self.btn5)
        self.btn5.bind(on_press=pa)

        self.btn6 = Button(background_color=[255, 255, 255, 1])
        self.add_widget(self.btn6)
        self.btn6.bind(on_press=dha)

        self.btn7 = Button(background_color=[0, 0, 0, 1])
        self.add_widget(self.btn7)
        self.btn7.bind(on_press=ni)

        self.btn8 = Button(background_color=[255, 255, 255, 1])
        self.add_widget(self.btn8)
        self.btn8.bind(on_press=saa)


class Piano(App):
    def build(self):
        return PianoButtons()


Piano().run()
