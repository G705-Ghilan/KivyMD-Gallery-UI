from app.librarys import (

	md_icons,
	MDScreen,
	Thread,
	StringProperty,
	toast,
	OneLineIconListItem,
)

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class Icons(MDScreen):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_list_md_icons()

	def set_list_md_icons(self, text="", search=False):
		def add_icon_item(name_icon):
			self.ids.rv.data.append(
				{
					"viewclass": "CustomOneLineIconListItem",
					"icon": name_icon,
					"text": name_icon,
					"callback": lambda x: x,
				}
			)
			
		self.ids.rv.data = []
		for name_icon in md_icons.keys():
			if search:
				if text in name_icon:
					add_icon_item(name_icon)
			else:
				add_icon_item(name_icon)

	def on_back_click(self):
		self.ids.search_field.text = ""
		return True
