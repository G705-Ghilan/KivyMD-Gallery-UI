from app.librarys import (
	re,
	toast,
	Builder,
	Splitter,
	MDCard,
	MDLabel,
	KivyLexer,
	traceback,
	CodeInput,
	MDScreen,
	CodeInput,
	ScrollView,
	get_all_styles,
	MDDropdownMenu,
	
)

class StripSplitter(MDCard):
	pass
	
class SplitterCode(Splitter):
	strip_cls = StripSplitter
	
class SplitterSettings(Splitter):
	strip_cls = StripSplitter
	


class KivyInput(CodeInput):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lexer = KivyLexer()
		self.is_new_line = False
		#['default', 'emacs', 'friendly', 'colorful', 'autumn', 'murphy', 'manni', 'material', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light']
		self.style_name="material"
		self.open_close = {
			"(": ")",
			"{": "}",
			"[": "]",
			'"': '"',
			"'": "'",
		}
		
		
	def insert_text(self, substring: str, from_undo: bool = False):
		_super = super().insert_text
		self.is_new_line = substring == "\n"
		try:
			return self.complete(substring, lambda out: _super(out, from_undo), self.open_close)
		except Exception as e:
			toast(f"ERROR-Complete: ({e.__class__.__name__}): {e}")
			return _super(substring + self.open_close.get(substring, ''), from_undo)
			
		
	def complete(self,substring, sup, open_close):
		""" complete reading """
		text = self.text.split('\n')
		try:
			text = text[self.cursor[1]]
		except IndexError:
			text = text[-1]
		if substring == "\n":
			# complete tap
			try:
				substring += "	"*(
					 len(
					 	re.findall(
					 		r"^([\t]*)",
					 		text.replace('    ', "\t")
					 	)[0]
					 ) + (
					 	1 if text.endswith(":") else 0
					 )
				)
			except IndexError:
				pass
			_super = sup(substring)
			
		elif substring in self.open_close:
			# complete (, ", ...
			substring = "" \
				if self.cursor[0] != len(text) \
				and text[self.cursor[0]] == substring \
				else substring + self.open_close[substring]
			_super = sup(substring)
			self.cursor = (
				self.cursor[0] + (-1 if substring else 1),
				self.cursor[1]
			)
			
		else:
			_super = sup(substring)
		return _super
		

			
class KivymdEditor(MDScreen):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.menu = MDDropdownMenu(
			items= [
				{
					"text": i,
					"viewclass": "OneLineListItem",
					"on_release": self.callback(i)
				} for i in sorted(get_all_styles())
			],
			width_mult=3
		)
	
	def callback(self, style_name):
		def __callback():
			self.ids.code_input.style_name = style_name
		return __callback
	
	
 
	def open_menu(self, caller: object):
		self.menu.caller = caller
		self.menu.open()


	
	def on_text(self, text, ScreenUI, is_new_line):
	
		if not is_new_line:
			return
		try:
			ScreenUI.clear_widgets()
			ScreenUI.add_widget(Builder.load_string(text))
		except Exception:
			scroll = ScrollView()
			scroll.add_widget(
				MDLabel(
					text=(traceback.format_exc()),
					adaptive_height=True,
					theme_text_color="Error",
				)
			)
			ScreenUI.add_widget(
				scroll
			)

	def on_back_click(self):
		toast("BACK")
		return True