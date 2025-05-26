# meal_plans.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class MealPlans(BoxLayout):
    def __init__(self, get_recipe_names_callback, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)
        self.get_recipe_names = get_recipe_names_callback
        self.meal_plans = {}  # Store meal plans as {day: recipe_name}

        self.add_widget(Label(text="Meal Plans", size_hint_y=None, height=30))

        self.plan_list = BoxLayout(orientation='vertical', size_hint_y=None)
        self.plan_list.bind(minimum_height=self.plan_list.setter('height'))
        scroll = ScrollView()
        scroll.add_widget(self.plan_list)
        self.add_widget(scroll)

        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.add_btn = Button(text="Add Meal Plan")
        self.add_btn.bind(on_release=self.add_meal_plan)
        btn_layout.add_widget(self.add_btn)

        self.clear_btn = Button(text="Clear All")
        self.clear_btn.bind(on_release=self.clear_all)
        btn_layout.add_widget(self.clear_btn)

        self.add_widget(btn_layout)

        self.refresh_plan_list()

    def refresh_plan_list(self):
        self.plan_list.clear_widgets()
        for day, recipe in self.meal_plans.items():
            lbl = Label(text=f"{day}: {recipe}", size_hint_y=None, height=30)
            self.plan_list.add_widget(lbl)

    def add_meal_plan(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)

        day_input = TextInput(hint_text="Day (e.g., Monday)", multiline=False, size_hint_y=None, height=40)
        recipe_input = TextInput(hint_text="Recipe Name", multiline=False, size_hint_y=None, height=40)

        content.add_widget(day_input)
        content.add_widget(recipe_input)

        btn_save = Button(text="Save", size_hint_y=None, height=40)
        btn_cancel = Button(text="Cancel", size_hint_y=None, height=40)
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        btn_layout.add_widget(btn_save)
        btn_layout.add_widget(btn_cancel)

        content.add_widget(btn_layout)

        popup = Popup(title="Add Meal Plan", content=content, size_hint=(.7, .5))

        def save_plan(instance):
            day = day_input.text.strip()
            recipe = recipe_input.text.strip()
            if not day or not recipe:
                self.show_popup("Error", "Both day and recipe are required.")
                return
            if recipe not in self.get_recipe_names():
                self.show_popup("Error", "Recipe not found.")
                return
            self.meal_plans[day] = recipe
            self.refresh_plan_list()
            popup.dismiss()

        btn_save.bind(on_release=save_plan)
        btn_cancel.bind(on_release=popup.dismiss)
        popup.open()

    def clear_all(self, instance):
        self.meal_plans.clear()
        self.refresh_plan_list()

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        btn_close = Button(text='Close', size_hint_y=None, height=40)
        content.add_widget(btn_close)
        popup = Popup(title=title, content=content, size_hint=(.6, .4))
        btn_close.bind(on_release=popup.dismiss)
        popup.open()
