from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout

# Import your module UIs (make sure these files are in the same folder)
from recipe_ui import RecipeUI
from shopping_list import ShoppingListUI
from user_accounts import UserAccountsUI
from timer import TimerUI
from meal_plans import MealPlansUI

class CookMasterTabs(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False  # Disable default tab
        
        # Add Recipe tab
        self.recipe_tab = self.create_tab("Recipes", RecipeUI())
        self.add_widget(self.recipe_tab)

        # Add Shopping List tab
        self.shopping_tab = self.create_tab("Shopping List", ShoppingListUI())
        self.add_widget(self.shopping_tab)

        # Add User Accounts tab
        self.accounts_tab = self.create_tab("User Accounts", UserAccountsUI())
        self.add_widget(self.accounts_tab)

        # Add Timers tab
        self.timer_tab = self.create_tab("Timers", TimerUI())
        self.add_widget(self.timer_tab)

        # Add Meal Plans tab
        self.mealplans_tab = self.create_tab("Meal Plans", MealPlansUI())
        self.add_widget(self.mealplans_tab)

    def create_tab(self, title, content):
        from kivy.uix.tabbedpanel import TabbedPanelItem
        tab = TabbedPanelItem(text=title)
        tab.add_widget(content)
        return tab

class CookMasterApp(App):
    def build(self):
        return CookMasterTabs()

if __name__ == "__main__":
    CookMasterApp().run()
