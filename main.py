from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyraAIApp(App):
    def build(self):
        self.title = "Myra AI"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.output_label = Label(text="नमस्ते! मैं मायरा एआई हूँ। आपकी क्या मदद कर सकती हूँ?", font_size=18)
        layout.add_widget(self.output_label)
        
        self.user_input = TextInput(hintText="यहाँ अपना सवाल लिखें...", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.user_input)
        
        submit_btn = Button(text="भेजें", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.8, 1))
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)
        
        return layout

    def on_submit(self, instance):
        query = self.user_input.text
        if query:
            self.output_label.text = f"आपने कहा: {query}\n(मायरा एआई जवाब जल्द ही जोड़े जाएंगे)"
            self.user_input.text = ""

if __name__ == '__main__':
    MyraAIApp().run()
