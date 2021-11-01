from app.librarys import MDScreen, toast

class Main(MDScreen):
	def on_back_click(self):
		toast("are you sure!")
		#return True
