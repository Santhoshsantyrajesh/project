from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
import pyrebase

s = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    LoginScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
    MDRectangleFlatButton:
        text: 'backlogin'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'login'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu' 
<UploadScreen>:
    name: 'upload'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Entered'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5

        MDLabel:
            text: 'hello world'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: root.manager.current = 'menu' 
<LoginScreen>:
    name:"login"
    MDFloatLayout:

        MDTextField:
            id:email
            hint_text: "Enter username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:300
            
        MDTextField:
            id:password
            hint_text: "Enter password"
            helper_text: "or click on forgot password"
            helper_text_mode: "on_focus"
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.58}
            size_hint_x:None
            width:300
        MDRaisedButton:
            text:"LOGIN"
            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
            md_bg_color: 1, 0, 1, 1
            on_press: root.manager.current = 'menu'
        """
LO = '''
MDScreen:
     '''

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
class LoginScreen(MDScreen):
    pass



class Accont:
    def __init__(self):
        firebaseConfig = {
            "apiKey": "AIzaSyBniiXUdMN3CfbsvEMnF3HRpuLNB-YpVZY",
            "authDomain": "amigo-virtual-6960b.firebaseapp.com",
            "projectId": "amigo-virtual-6960b",
            "databaseURL": "https://amigo-virtual-6960b.firebaseio.com",
            "storageBucket": "amigo-virtual-6960b.appspot.com",
            "messagingSenderId": "924780726622",
            "appId": "1:924780726622:web:38694cd80c1024d3a6a7cf",
            "measurementId": "G-T0PYHDD2RB"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()
    def sing_up(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            return True

        except:
            return False
class MainApp(MDApp):

    def build(self):
        global scr
        scr = ScreenManager()
        Builder.load_string(s)
        #Builder.load_string(a)
        self.theme_cls.primary_palette = "Orange"
        scr.add_widget((Builder.load_file("Main.kv")))

        scr.add_widget((Builder.load_string(LO)))
        scr.add_widget(MenuScreen(name='menu'))
        scr.add_widget(ProfileScreen(name='profile'))
        scr.add_widget(UploadScreen(name='upload'))
        scr.add_widget(LoginScreen(name='login'))
        return scr

    def navigation_draw(self):
        pass
    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        scr.current = "login"



if __name__ == "__main__":
    accont = Accont()
    MainApp().run()
