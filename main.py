from kivy.app import App
from App import *

# Class pro spusteni GUI
class BudgetBlackJackApp(App):
    def build(self):
        """Vytvoření grafického uživatelského rozhraní.
        Vrátí instanci třídy MyLayout, která představuje hlavní rozvržení aplikace.

        """
        return MyLayout()

if __name__ == '__main__':
    BudgetBlackJackApp().run()
