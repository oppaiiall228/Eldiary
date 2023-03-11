from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle

Config.set("graphics", "width", "400")
Config.set("graphics", "height", "700")

from kivy.uix.floatlayout import FloatLayout


class RootWidget(BoxLayout):
    pass


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
          # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainApp(App):
    def build(self):
        root = RootWidget()
        fl = CustomLayout(size=(300, 300), size_hint=(.5, .50))
        root.add_widget(fl)
        fl.add_widget(
            AsyncImage(
                source="./don2.jpg",
                size_hint=(0.5, 0.5),
                pos_hint={'center_x': 0.5, 'center_y': 1}))
        fl.add_widget(Button(text="Ученик",
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal="",
                             size_hint=(.6, .3),
                             pos=(150 / 2 - 0.3, 300 / 2)))
        fl.add_widget(Button(text="Родитель",
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal="",
                             size_hint=(.6, .3),
                             pos=(150 / 2, 600 / 2)))
        fl.add_widget(Button(text="Учитель",
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal="",
                             size_hint=(.6, .3),
                             pos=(150 / 2, 900 / 2)))

        return root

    def btn_press(self, instance):
        print("ryj")
        instance.text = "zsf"


if __name__ == "__main__":
    MainApp().run()
