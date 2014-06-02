from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
class MyApp(App):
	def build(self):
		win = Widget()
		lbl1 = Label(text='Video Player',font_size=15, bold=True, pos=(700,350))
		vp = VideoPlayer(source='code/softboy.avi',size=(160,200),pos=(670,180))
		btn1 = Button(text='Start Video',font_size=15,bold=True,pos=(670,120))
		win.add_widget(lbl1)
		win.add_widget(vp)
		win.add_widget(btn1)
		return win
if __name__ == '__main__':
	MyApp().run()
