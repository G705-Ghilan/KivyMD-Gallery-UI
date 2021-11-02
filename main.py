from kivymd.app import MDApp

from app.librarys import (
	Main,
	toast,
	Icons,
	Builder,
	Window,
	traceback,
	KivymdEditor,
	FadeTransition,
	ScreenManager,
	CalculatorWidget
)

Builder.load_string("""
#:import toast kivymd.toast.toast
#:import hex kivy.utils.get_color_from_hex
#:import images_path kivymd.images_path
#:import Clipboard kivy.core.clipboard.Clipboard
#:import md_icons kivymd.icon_definitions.md_icons
#:import ButtonBehavior kivy.uix.behaviors.button.ButtonBehavior

#:include app/frontend/Calculator.kv
#:include app/frontend/Main.kv
#:include app/frontend/Icons.kv
#:include app/frontend/kivymdeditor.kv
""")


from kivy.base import ExceptionHandler, ExceptionManager

class ExceptionApp(ExceptionHandler):
	""" for handle exception of app """
	
	def handle_exception(self, ins):
		""" catch any exception at runTouchApp and show to user """
		app = MDApp.get_running_app()
		if app.screen_manager.current == "KivymdEditor":
			obj = app.screen_manager.get_screen("KivymdEditor")
			if not obj.error:
				obj.add_error(traceback.format_exc())
		else:
			toast(f"ERRORAtrunTouchApp: {ins}")
			
		return ExceptionManager.PASS
		
ExceptionManager.add_handler(ExceptionApp())

class GalleryKivymd(MDApp):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Screens ...
		self.screen_manager = ScreenManager(transition=FadeTransition())
		self.screen_manager.add_widget(Main(name="Main"))
		self.screen_manager.add_widget(CalculatorWidget(name="Calculator"))
		self.screen_manager.add_widget(Icons(name="Icons"))
		self.screen_manager.add_widget(KivymdEditor(name="KivymdEditor"))
		# Controler Android ...
		Window.bind(on_keyboard=self.android_back_click)
		
	Themes = {
		"default": {
			"box": '#78909C',
			"screen": '#455A64'
		},
		"green_dark": {
			"box": "#26A69A",
			"screen": "#00695C"
		}
	}
	

	Theme_name = "green_dark"
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return self.screen_manager

	@property
	def theme(self):
		return self.Themes[self.Theme_name]

	def android_back_click(self, window: object, key: int, *lasts):
		''' if user clicked on back click will run this function '''
		if key == 27:
			obj = self.screen_manager.get_screen(self.screen_manager.current)
			self.screen_manager.current = "Main"
			return obj.on_back_click()

GalleryKivymd().run()
