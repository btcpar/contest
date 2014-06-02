from kivy.app import App
from kivy.uix.widget import Widget
class MyApp(App):
	def build(self):
		win = Widget()
		return win
if __name__ == '__main__':
	MyApp().run()
