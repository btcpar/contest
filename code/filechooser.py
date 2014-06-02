from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooserListView,FileChooserIconView
class MyApp(App):
	def build(self):
		win = Widget()
		fc1 = FileChooserListView(size=(160,150), pos=(670,260))
		fc2 = FileChooserIconView(size=(160,150), pos=(670,120))
		win.add_widget(fc1)
		win.add_widget(fc2)
		return win
if __name__ == '__main__':
	MyApp().run()
