from kivy.app import App
from App import *


class BudgetBlackJackApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    BudgetBlackJackApp().run()


