from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class MyApp(App):
	def build(self):
		win = Widget()
		lbl1 = Label(text='Text Editor',font_size=15, bold=True, pos=(700,350))
		txti = TextInput(width=160, height=200,pos=(670,180))
		btn1 = Button(text='Open',font_size=15,bold=True,pos=(670,140))
		btn2 = Button(text='Save',font_size=15,bold=True,pos=(670,110))
		btn3 = Button(text='exit',font_size=15,bold=True,pos=(670,80))
		win.add_widget(lbl1)
		win.add_widget(txti)
		win.add_widget(btn1)
		win.add_widget(btn2)
		win.add_widget(btn3)
		return win
if __name__ == '__main__':
	MyApp().run()
