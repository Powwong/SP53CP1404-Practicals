from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ['Jack', 'Gary', 'Jiaqin', 'MingYu', 'Aditya', 'TanAnhNguyen', 'Albert', 'Alvaro']

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates label from entries in the list"""
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.label_box.add_widget(temp_button)


DynamicLabelsApp().run()