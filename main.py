from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.settings import SettingsWithSidebar

# Define the KV string
Builder.load_string('''
<CanvasButton>:
    icon: ''
    text: ''
    size_hint: None, None
    size: 200, 200
    canvas.before:
        Color:
            rgba: 0.3, 0.3, 0.3, 0.5  # Darker gray background color
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        size: root.size
        pos: root.pos
        spacing: 10
        Image:
            source: root.icon
            size_hint: None, None
            size: 100, 100  # Adjust size of the icon as needed
            pos_hint: {'center_x': 0.5}
        Label:
            text: root.text
            color: 0, 1, 0, 1  # Green text color

<ScreenOne>:
    orientation: 'vertical'
    
    BoxLayout:
        id: layout_one
        orientation: 'vertical'
        size_hint: None, None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        canvas.before:
            Color:
                rgba: 0.2, 0.2, 0.2, 0  # Set alpha to 0 for transparency
            Rectangle:
                size: self.size
                pos: self.pos

        Label:
            text: "Welcome to Section One"
            font_size: 30
            color: 0, 1, 0, 1
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'middle'
            halign: 'center'

        Button:
            text: 'Go to Section Two'
            size_hint: None, None
            size: 200, 50
            pos_hint: {'center_x': 0.5}
            on_press: root.change_screen()

<ScreenTwo>:
    orientation: 'vertical'
    AnchorLayout:
        BoxLayout:
            orientation: 'horizontal'
            spacing: 20
            size_hint: None, None
            size: 800, 200
            pos_hint: {'center_x': 0.5}

            CanvasButton:
                text: 'facebook'
                on_press: root.go_to_section('section1')
                icon: 'icon1.png'

            CanvasButton:
                text: 'Section 2'
                on_press: root.go_to_section('section2')
                icon: 'icon2.png'

            CanvasButton:
                text: 'Section 3'
                on_press: root.go_to_section('section3')
                icon: 'icon3.png'

            CanvasButton:
                text: 'Section 4'
                on_press: root.go_to_section('section4')
                icon: 'icon4.png'

<FacebookSection>:
    orientation: 'vertical'
    Label:
        text: 'Section 1'
        font_size: 30
        color: 0, 1, 0, 1
        size_hint_y: None
        height: self.texture_size[1]
        valign: 'middle'
        halign: 'center'
    
    Button:
        text: 'Back to Section Two'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5}
        on_press: root.change_screen()

<SectionTwo>:
    orientation: 'vertical'
    Label:
        text: 'Section 2'
        font_size: 30
        color: 0, 1, 0, 1
        size_hint_y: None
        height: self.texture_size[1]
        valign: 'middle'
        halign: 'center'
    
    Button:
        text: 'Back to Section Two'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5}
        on_press: root.change_screen()

<SectionThree>:
    orientation: 'vertical'
    Label:
        text: 'Section 3'
        font_size: 30
        color: 0, 1, 0, 1
        size_hint_y: None
        height: self.texture_size[1]
        valign: 'middle'
        halign: 'center'
    
    Button:
        text: 'Back to Section Two'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5}
        on_press: root.change_screen()

<SectionFour>:
    orientation: 'vertical'
    Label:
        text: 'Section 4'
        font_size: 30
        color: 0, 1, 0, 1
        size_hint_y: None
        height: self.texture_size[1]
        valign: 'middle'
        halign: 'center'
    
    Button:
        text: 'Back to Section Two'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5}
        on_press: root.change_screen()
''')

class CanvasButton(ButtonBehavior, Widget):
    icon = StringProperty('')
    text = StringProperty('')

class ScreenOne(Screen):
    def change_screen(self):
        app.root.current = 'screen_two'

class ScreenTwo(Screen):
    def go_to_section(self, section):
        app.root.current = section

class FacebookSection(Screen):
    def change_screen(self):
        app.root.current = 'screen_two'

class SectionTwo(Screen):
    def change_screen(self):
        app.root.current = 'screen_two'

class SectionThree(Screen):
    def change_screen(self):
        app.root.current = 'screen_two'

class SectionFour(Screen):
    def change_screen(self):
        app.root.current = 'screen_two'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='screen_one'))
        sm.add_widget(ScreenTwo(name='screen_two'))
        sm.add_widget(FacebookSection(name='facebook_section'))
        sm.add_widget(SectionTwo(name='section2'))
        sm.add_widget(SectionThree(name='section3'))
        sm.add_widget(SectionFour(name='section4'))
        return sm

if __name__ == '__main__':
    app = MyApp()
    app.run()
