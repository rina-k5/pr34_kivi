from kivy.config import Config
Config.set('graphics', 'width', '500')  # Устанавливаем ширину окна в 500 пикселей

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class RainbowApp(App):
    def build(self): #метод
        self.layout = BoxLayout(orientation='vertical')

       #создаём верхнее текстовое поле
        self.label = Label(text="Выберите цвет", size_hint=(1, 0.2), font_size='24sp')
        with self.label.canvas.before:#цвет фона поля (чёрный)
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.label.size, pos=self.label.pos)
        self.label.bind(size=self.update_rect, pos=self.update_rect)

        self.layout.add_widget(self.label)

        colors = [
            ("Красный", (1, 0, 0, 1)),#значение цвета в формате RGBA
            ("Оранжевый", (1, 0.5, 0, 1)),
            ("Желтый", (1, 1, 0, 1)),
            ("Зеленый", (0, 1, 0, 1)),
            ("Голубой", (0, 1, 1, 1)),
            ("Синий", (0, 0, 1, 1)),
            ("Фиолетовый", (0.5, 0, 0.5, 1))
        ]

        for color_name, color_value in colors:#цикл для кнопок
            btn = Button(text=color_name, background_normal='', background_color=color_value, on_press=self.on_button_press)
            self.layout.add_widget(btn)#вызов метода

        return self.layout

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def on_button_press(self, instance):#меняет текст вверху на шестнадцатиричное значение цвета
        color_value = instance.background_color #получает значение цвета фона нажатой кнопки
        color_hex = f"{int(color_value[0] * 255):02X}{int(color_value[1] * 255):02X}{int(color_value[2] * 255):02X}"

        self.label.text = color_hex #устанавливает в верхнее поле шестн.значение цвета
        with self.label.canvas.before:
            self.label.canvas.before.clear()
            Color(*color_value)
            self.rect = Rectangle(size=self.label.size, pos=self.label.pos)
        self.label.color = (1, 1, 1, 1) if sum(color_value[:3]) / 3 < 0.5 else (0, 0, 0, 1)

if __name__ == "__main__":
    RainbowApp().run()
