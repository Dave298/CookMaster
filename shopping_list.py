# shopping_list.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json
import os

DATA_FILE = "shopping_list.json"

class ShoppingListManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        self.input = TextInput(hint_text="Enter item", size_hint_y=None, height=40, multiline=False)
        self.add_widget(self.input)

        add_button = Button(text="Add Item", size_hint_y=None, height=40)
        add_button.bind(on_release=self.add_item)
        self.add_widget(add_button)

        self.list_label = Label(text="", halign='left', valign='top', size_hint_y=None)
        self.list_label.bind(size=self.update_label_height)
        self.add_widget(self.list_label)

        clear_button = Button(text="Clear List", size_hint_y=None, height=40)
        clear_button.bind(on_release=self.clear_list)
        self.add_widget(clear_button)

        self.shopping_list = self.load_list()
        self.update_display()

    def add_item(self, instance):
        item = self.input.text.strip()
        if item:
            self.shopping_list.append(item)
            self.input.text = ""
            self.save_list()
            self.update_display()

    def clear_list(self, instance):
        self.shopping_list.clear()
        self.save_list()
        self.update_display()

    def update_display(self):
        self.list_label.text = "\n".join(f"• {item}" for item in self.shopping_list)

    def update_label_height(self, *args):
        self.list_label.text_size = (self.width, None)
        self.list_label.height = self.list_label.texture_size[1]

    def save_list(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.shopping_list, f)

    def load_list(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return []
