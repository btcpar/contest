from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.switch import Switch
class MyApp(App):
	def build(self):
		win = Widget()
		lbl = Label(text='Label',font_size=15, pos=(630,350))
		btn = Button(text='Button',font_size=15, bold=True, pos=(690,320))
		txti = TextInput(font_size=15, width=100, height=25, pos=(690,290))
		chkb = CheckBox(group='',pos=(680,350))
		spn = Spinner(text='home',values=('home','file','edit'),size=(100,25),pos=(690,260))
		sl = Slider(width=0,height=100,max=100,value=25,orientation='vertical',pos=(670,180))
		pb = ProgressBar(width=100,max=100,value=75,pos=(720,180))
		img = Image(source='code/dna.jpeg',size=(100,100),pos=(670,80))
		win.add_widget(lbl)
		win.add_widget(btn)
		win.add_widget(txti)
		win.add_widget(chkb)
		win.add_widget(spn)
		win.add_widget(sl)
		win.add_widget(pb)
		win.add_widget(img)
		return win
if __name__ == '__main__':
	MyApp().run()
