from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
class MyApp(App):
	def build(self):
		win = Widget()
		lbl1 = Label(text='Label',font_size=15, pos=(630,350))
		lbl2 = Label(text='Label',font_size=15, bold=True, pos=(630,300))
		lbl3 = Label(text='Label',font_size=15, italic=True, pos=(630,250))
		lbl4 = Label(text='Label',font_size=25, pos=(650,200))
		lbl5 = Label(text='Label',font_size=25, bold=True, pos=(650,150))
		lbl6 = Label(text='Label',font_size=25, italic=True, pos=(650,100))
		win.add_widget(lbl1)
		win.add_widget(lbl2)
		win.add_widget(lbl3)
		win.add_widget(lbl4)
		win.add_widget(lbl5)
		win.add_widget(lbl6)
		return win
if __name__ == '__main__':
	MyApp().run()
