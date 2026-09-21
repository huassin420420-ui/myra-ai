from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyraAIApp(App):
    def build(self):
        self.title = "Myra AI"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.output_label = Label(text="Welcome to Myra AI", font_size=20)
        layout.add_widget(self.output_label)
        
        self.user_input = TextInput(hint_text="Type your message here...", multiline=False)
        layout.add_widget(self.user_input)
        
        submit_btn = Button(text="भेजें", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)
        
        return layout

    def on_submit(self, instance):
        user_text = self.user_input.text
        self.output_label.text = f"You: {user_text}"

if __name__ == '__main__':
    MyraAIApp().run()
