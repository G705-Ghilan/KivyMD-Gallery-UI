from app.librarys import (
	MDCard,
	MDScreen,
	Window,toast,
	StringProperty,
	ObjectProperty,
)

class NumItem(MDCard):
	text: str = StringProperty("")
	result: object = ObjectProperty()
	caltext: object = ObjectProperty()
	tex_color: str = StringProperty("#FFFFFF")

	def refresh_number(self):
		if self.text == "C":
			self.caltext.text = ""
			self.result.text = ""
		elif self.text == "=":
			if self.result.text:
				self.caltext.text = self.result.text
				self.result.text = ""
		elif self.text in "+-×÷.":
			if not self.caltext.text:
				return
			elif self.caltext.text[-1] not in  "+-×÷.":
				if self.text == '.':
					if '.' not in self.caltext.text.split('+')[-1].split('-')[-1].split('×')[-1].split('÷')[-1]:
						self.caltext.text += self.text
				else:
					self.caltext.text += self.text
		else:
			self.caltext.text += self.text
			try:
				result = str(eval(self.caltext.text.replace("×", "*").replace("÷", "/")))
				if result != self.caltext.text:
					try:
						self.result.text = result.split('.')[0] if int(result.split('.')[-1]) == 0 else result
					except ValueError:
						self.result.text = result
				else:
					self.result.text = ""
			except Exception as e:
				self.result.text = str(e)
		


class CalculatorWidget(MDScreen):
	""" this class is all widgets of page calculator """
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		_item = NumItem
		_item.caltext = self.ids.caltext
		_item.result = self.ids.result
		for i in list(range(1, 10)) + [0, '.', "="]:
			self.ids["grid"].add_widget(_item(text=str(i)))
			
	def on_back_click(self):
		self.ids.caltext.text = ""
		self.ids.result.text = ""
		return True

