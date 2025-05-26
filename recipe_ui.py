# recipe_ui.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class RecipeUI(BoxLayout):
    def __init__(self, recipes_manager, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)
        self.recipes_manager = recipes_manager

        # Recipe list label
        self.add_widget(Label(text="Recipes", size_hint_y=None, height=30))

        # Recipe list
        self.recipe_list = BoxLayout(orientation='vertical', size_hint_y=None)
        self.recipe_list.bind(minimum_height=self.recipe_list.setter('height'))
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.recipe_list)
        self.add_widget(self.scroll_view)

        # Buttons
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.add_btn = Button(text="Add Recipe")
        self.add_btn.bind(on_release=self.add_recipe)
        btn_layout.add_widget(self.add_btn)

        self.edit_btn = Button(text="Edit Recipe")
        self.edit_btn.bind(on_release=self.edit_recipe)
        btn_layout.add_widget(self.edit_btn)

        self.delete_btn = Button(text="Delete Recipe")
        self.delete_btn.bind(on_release=self.delete_recipe)
        btn_layout.add_widget(self.delete_btn)

        self.add_widget(btn_layout)

        self.selected_recipe = None

        self.refresh_recipe_list()

    def refresh_recipe_list(self):
        self.recipe_list.clear_widgets()
        for recipe in self.recipes_manager.get_all_recipes():
            btn = Button(text=recipe['name'], size_hint_y=None, height=40)
            btn.bind(on_release=self.select_recipe)
            self.recipe_list.add_widget(btn)

    def select_recipe(self, instance):
        self.selected_recipe = instance.text
        self.show_recipe_details(self.selected_recipe)

    def show_recipe_details(self, recipe_name):
        recipe = self.recipes_manager.get_recipe(recipe_name)
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=f"Name: {recipe['name']}"))
        content.add_widget(Label(text=f"Ingredients:\n{recipe['ingredients']}"))
        content.add_widget(Label(text=f"Instructions:\n{recipe['instructions']}"))

        btn_close = Button(text='Close', size_hint_y=None, height=40)
        content.add_widget(btn_close)

        popup = Popup(title="Recipe Details", content=content, size_hint=(.7, .7))
        btn_close.bind(on_release=popup.dismiss)
        popup.open()

    def add_recipe(self, instance):
        self.recipe_editor_popup("Add New Recipe")

    def edit_recipe(self, instance):
        if not self.selected_recipe:
            self.show_popup("Error", "No recipe selected.")
            return
        self.recipe_editor_popup("Edit Recipe", self.recipes_manager.get_recipe(self.selected_recipe))

    def delete_recipe(self, instance):
        if not self.selected_recipe:
            self.show_popup("Error", "No recipe selected.")
            return
        self.recipes_manager.delete_recipe(self.selected_recipe)
        self.refresh_recipe_list()
        self.show_popup("Deleted", f"Deleted recipe: {self.selected_recipe}")
        self.selected_recipe = None

    def recipe_editor_popup(self, title, recipe=None):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        name_input = TextInput(text=recipe['name'] if recipe else '', hint_text='Recipe Name', multiline=False)
        ingredients_input = TextInput(text=recipe['ingredients'] if recipe else '', hint_text='Ingredients')
        instructions_input = TextInput(text=recipe['instructions'] if recipe else '', hint_text='Instructions')

        content.add_widget(name_input)
        content.add_widget(ingredients_input)
        content.add_widget(instructions_input)

        btn_save = Button(text='Save', size_hint_y=None, height=40)
        btn_cancel = Button(text='Cancel', size_hint_y=None, height=40)
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        btn_layout.add_widget(btn_save)
        btn_layout.add_widget(btn_cancel)
        content.add_widget(btn_layout)

        popup = Popup(title=title, content=content, size_hint=(.8, .8))

        def save_recipe(instance):
            name = name_input.text.strip()
            ingredients = ingredients_input.text.strip()
            instructions = instructions_input.text.strip()
            if not name:
                self.show_popup("Error", "Recipe name is required.")
                return
            self.recipes_manager.save_recipe(name, ingredients, instructions)
            self.refresh_recipe_list()
            popup.dismiss()

        btn_save.bind(on_release=save_recipe)
        btn_cancel.bind(on_release=popup.dismiss)
        popup.open()

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        btn_close = Button(text='Close', size_hint_y=None, height=40)
        content.add_widget(btn_close)
        popup = Popup(title=title, content=content, size_hint=(.6, .4))
        btn_close.bind(on_release=popup.dismiss)
        popup.open()
