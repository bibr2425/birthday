from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText
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

        self.photo_1 = "images.jfif"  # Перша картинка (котик)
        self.photo_2 = "marta.jpg"     # Друга картинка (фото Марти)

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
            font_style="Headline",
            role="medium"
        )

        # 2. Зображення
        self.photo = Image(
            source=self.photo_1,
            size_hint=(1, 3),
            allow_stretch=True,
            keep_ratio=False,
            nocache=True
        )

        # 3. Збільшений текст привітання (Title / Headline)
        self.msg_label = MDLabel(
            text="У мене є сюрпріс натисни на кнопку нижче",
            halign="center",
            font_style="Title",
            role="large"
        )

        # 4. Кнопка
        self.btn = MDButton(
            MDButtonText(text="Відкрити"),
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
        btn_text = self.btn.children[0]
        
        if btn_text.text == "Відкрити":
            self.photo.size_hint = (1, 3)
            self.photo.source = self.photo_2
            self.photo.keep_ratio = True
            
            # Збільшений текст привітання
            self.msg_label.font_style = "Title"
            self.msg_label.role = "large"
            self.msg_label.text = (
                "Бажаю щоб все тебе всьо було чотінько,\n "
                "міцного здоров'я, здійснення всіх мрій "
                "і все люді пешкі біг боб арешкі\n\n"
                    "Від Максіма(Бетмен)\n"
            )
            self.photo.reload()
            btn_text.text = "Сховати"
        else:
            self.photo.size_hint = (1, 3)
            self.photo.source = self.photo_1
            self.photo.keep_ratio = False
            
            self.msg_label.font_style = "Title"
            self.msg_label.role = "large"
            self.msg_label.text = "Марта у мене є сюрпріс"
            self.photo.reload()
            btn_text.text = "Відкрити"

if __name__ == '__main__':
    BirthdayApp().run()
