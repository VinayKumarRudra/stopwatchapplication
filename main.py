from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import kivy.uix.button as kb
from kivy.clock import Clock
from time import  strftime
from kivy.properties import NumericProperty
from datetime import datetime
from datetime import timedelta





class Input(GridLayout):

    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.time=0
        self.count=0
        self.sec=0
        self.seconds=0
        self.cols = 2
        self.size= self.width * 0.8, self.height * 0.8

        self.row_default_height= 30
        self.row_force_default= True

        self.add_widget(Label(text='Number of Exercise'))
        self.numberofexercise = TextInput(multiline=False)
        self.add_widget(self.numberofexercise)
        self.add_widget(Label(text='Number of Reps'))
        self.noofrep = TextInput(multiline=False)
        self.add_widget(self.noofrep)
        self.add_widget(Label(text='Time gap between the Reps(in secs)'))
        self.betweenrep = TextInput(multiline=False)
        self.add_widget(self.betweenrep)
        self.add_widget(Label(text='Time gap between the exercises(in secs)'))
        self.betweenexercise = TextInput(multiline=False)
        self.add_widget(self.betweenexercise)
        btn1 = kb.Button(text='start', pos=(200, 200), size_hint_x=None, width=100)
        btn1.bind(on_press=self.callback)

        self.add_widget(btn1)
        self.add_widget(Label(text="Time"))

    def callback(self, instance):

        for i in range(int(self.numberofexercise.text)):
            self.add_widget(Label(text='exercise'))
            self.btn2=kb.Button(text='click to start timer')
            self.add_widget(self.btn2)
            self.btn2.bind(on_press=self.start_increment)
            self.btn2.bind(on_press=self.start_incr)
            for i in range(int(self.noofrep.text)):

                self.add_widget(Label(text="rep"))
                self.label=Label(text='0')
                self.add_widget(self.label)

    def start_incr(self,*args):
        Clock.schedule_interval(self.timer_call, 0)


    def start_increment(self,*args):
        Clock.schedule_interval(self.btn2, 0)

    def timer_call(self,*args):
        self.sec+=1
        self.btn2.text=str(self.sec)
        if self.sec == int(self.betweenexercise.text):
            self.btn2.text = 'Time Over!'
            self.sec=0
            return False


    def timer(self, *args):
        self.seconds += 1
        self.label.text = str(self.seconds)
        if self.seconds == int(self.betweenrep.text):
            self.label.text = 'Time Over!'
            self.seconds=0
            return False



class ClockApp(App):
    def build(self):
        return Input()


if __name__ == '__main__':
    ClockApp().run()