from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
class MyApp(App):
	def build(self):
		win = Widget()
		lbl1 = Label(text='Images',font_size=15, bold=True, pos=(700,350))
		img1 = Image(source='code/dna.jpeg',size=(50,50),pos=(670,320))
		img2 = Image(source='code/dna.jpeg',size=(100,100),pos=(720,220))
		img3 = Image(source='code/dna.jpeg',size=(160,160),pos=(670,50))
		win.add_widget(img1)
		win.add_widget(img2)
		win.add_widget(img3)
		return win
if __name__ == '__main__':
	MyApp().run()
