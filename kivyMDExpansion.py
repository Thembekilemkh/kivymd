from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class expand(MDBoxLayout):
	def __init__(self, **kwargs):
		super(expand, self).__init__(**kwargs)
		#self.adaptive_height=True
		#self.orientation = "vertical"
		#self.height = self.minimum_height
		#self.size_hint = (1, None)
		
		for btn_num in range(10):
			btn = TwoLineIconListItem(text="Text: "+ str(btn_num), secondary_text="It actually works")
			self.add_widget(btn)

class content(GridLayout):
	pass


class box(BoxLayout):
	def __init__(self):
		super(box,self).__init__()
		self.orientation = "vertical"
		scrollview = ScrollView()
		grid = MDGridLayout(cols=1, size_hint_y=None)
		print("grid height: ", grid.minimum_height)
		grid.height=grid.minimum_height
		#grid
		
		names =["option1", "option2","option3"]

		for name in names:
			boat = expand(orientation="vertical",size_hint = (1, None), adaptive_height=True)
	
			panel = MDExpansionPanel(content=boat, icon="Add.png", panel_cls=MDExpansionPanelOneLine(text=name))
			grid.add_widget(panel)

		scrollview.add_widget(grid)
		self.add_widget(scrollview)

class MainApp(MDApp):

	def build(self):
		return box()


MainApp().run()
