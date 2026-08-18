import os
import sys
from kivy.resources import resource_add_path

resource_add_path(os.path.dirname(os.path.abspath(__file__)))

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp

class BirthdayApp(MDApp):
    def build(self):
        Window.fullscreen = False
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        
        screen = MDScreen()

        self.photo_1 = "images.jpg"
        self.photo_2 = "marta.jpg"

        self.card = MDCard(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(10),
            size_hint=(0.9, 0.88),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[dp(28)],
            style="elevated"
        )

        # 1. Заголовок
        self.title_label = MDLabel(
            text="З Днем Народження!",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0.4, 0.7, 1),
            font_style="H5"
        )

        # 2. Зображення
        self.photo = Image(
            source=self.photo_1 if os.path.exists(self.photo_1) else "",
            size_hint=(1, 3),
            allow_stretch=True,
            keep_ratio=False,
            nocache=True
        )

        # 3. Текст
        self.msg_label = MDLabel(
            text="У мене є сюрпріс натисни на кнопку нижче",
            halign="center",
            font_style="Subtitle1"
        )

        # 4. Кнопка
        self.btn = MDRaisedButton(
            text="Відкрити",
            pos_hint={"center_x": 0.5},
            on_release=self.toggle_wish
        )

        self.card.add_widget(self.title_label)
        self.card.add_widget(self.photo)
        self.card.add_widget(self.msg_label)
        self.card.add_widget(self.btn)
        
        screen.add_widget(self.card)
        return screen

    def toggle_wish(self, instance):
        if self.btn.text == "Відкрити":
            self.photo.size_hint = (1, 3)
            if os.path.exists(self.photo_2):
                self.photo.source = self.photo_2
            self.photo.keep_ratio = True
            
            self.msg_label.font_style = "Subtitle1"
            self.msg_label.text = (
                "Бажаю щоб все тебе всьо було чотінько,\n "
                "міцного здоров'я, здійснення всіх мрій "
                "і все люді пешкі біг боб арешкі\n\n"
                "Від Максіма(Бетмен)\n"
            )
            self.photo.reload()
            self.btn.text = "Сховати"
        else:
            self.photo.size_hint = (1, 3)
            if os.path.exists(self.photo_1):
                self.photo.source = self.photo_1
            self.photo.keep_ratio = False
            
            self.msg_label.font_style = "Subtitle1"
            self.msg_label.text = "Марта у мене є сюрпріс"
            self.photo.reload()
            self.btn.text = "Відкрити"

if __name__ == '__main__':
    BirthdayApp().run()
