# user_accounts.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
import os
import hashlib

DATA_FILE = "users.json"

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class UserAccountsManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        self.users = self.load_users()
        self.current_user = None

        # Login UI
        self.lbl_info = Label(text="Please Login or Sign Up", size_hint_y=None, height=30)
        self.add_widget(self.lbl_info)

        self.username_input = TextInput(hint_text="Username", multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.password_input)

        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)

        self.login_btn = Button(text="Login")
        self.login_btn.bind(on_release=self.login)
        btn_layout.add_widget(self.login_btn)

        self.signup_btn = Button(text="Sign Up")
        self.signup_btn.bind(on_release=self.signup)
        btn_layout.add_widget(self.signup_btn)

        self.add_widget(btn_layout)

        self.logout_btn = Button(text="Logout", size_hint_y=None, height=40)
        self.logout_btn.bind(on_release=self.logout)
        self.logout_btn.disabled = True
        self.add_widget(self.logout_btn)

        self.status_label = Label(text="Not logged in", size_hint_y=None, height=30)
        self.add_widget(self.status_label)

    def load_users(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return {}

    def save_users(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.users, f)

    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text

        if username in self.users and self.users[username] == hash_password(password):
            self.current_user = username
            self.status_label.text = f"Logged in as: {username}"
            self.logout_btn.disabled = False
            self.login_btn.disabled = True
            self.signup_btn.disabled = True
            self.username_input.disabled = True
            self.password_input.disabled = True
            self.show_popup("Success", "Login successful!")
        else:
            self.show_popup("Error", "Invalid username or password.")

    def signup(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text

        if not username or not password:
            self.show_popup("Error", "Username and password cannot be empty.")
            return

        if username in self.users:
            self.show_popup("Error", "Username already exists.")
            return

        self.users[username] = hash_password(password)
        self.save_users()
        self.show_popup("Success", "Account created! You can now login.")

    def logout(self, instance):
        self.current_user = None
        self.status_label.text = "Not logged in"
        self.logout_btn.disabled = True
        self.login_btn.disabled = False
        self.signup_btn.disabled = False
        self.username_input.disabled = False
        self.password_input.disabled = False
        self.username_input.text = ""
        self.password_input.text = ""
        self.show_popup("Logged out", "You have been logged out.")

    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_content.add_widget(Label(text=message))
        btn_close = Button(text="Close", size_hint_y=None, height=40)
        popup_content.add_widget(btn_close)

        popup = Popup(title=title, content=popup_content, size_hint=(.75, .4))
        btn_close.bind(on_release=popup.dismiss)
        popup.open()
