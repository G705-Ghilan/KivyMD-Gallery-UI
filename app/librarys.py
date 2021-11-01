import re
import traceback
from threading import Thread
from pygments.styles import get_all_styles

from kivy.lang import Builder
from kivy.uix.splitter import Splitter
from kivy.core.window import Window
from kivy.uix.codeinput import CodeInput
from kivy.uix.scrollview import ScrollView
from kivy.extras.highlight import KivyLexer
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from kivymd.toast import toast
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

from app.backend.main import Main
from app.backend.icons import Icons
from app.backend.kivymdeditor import KivymdEditor
from app.backend.Calculator import CalculatorWidget

