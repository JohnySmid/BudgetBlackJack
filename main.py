from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory


import Hand
import Deck



Window.size = (700, 400)

Builder.load_file('UI.kv')

# pro jednoduche trackovani skore, init pri spusteni aplikace, pak jen davam na puvodni hodnoty
class ScoreTracker:
    def __init__(self):
        self.score = 100

    def deduct_score(self, update):
        self.score -= update

    def addup_score(self, update):
        self.score += update

    def get_score(self):
        return self.score

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playstart()
        self.skore = ScoreTracker()
        self.ids.label_score.text = str(self.skore.get_score())

    # pro debug ucely, jsem si udelal fci na "start", zbytecna ale pouzivam ji
    def playstart(self):
        self.start()

    def start(self):
        # init decku, s kazdym kolem se udela novy deck
        self.deck = Deck.Deck()
        self.deck.shuffle()
        self.hit = False
        self.played = False
        self.bet = False
        self.castkabet = 0

        # kivy
        self.ids.img1karty.source = ''
        self.ids.img2karty.source = ''
        self.ids.img3karty.source = ''
        self.ids.label_bet.text = ''


        # karty
        self.player_hand = Hand.Hand()
        self.dealer_hand = Hand.Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())



        # txt karet
        self.ids.img1karty.source = f'txtkarty/{str(self.player_hand.cards[0])}.png'
        self.ids.img2karty.source = f'txtkarty/{str(self.player_hand.cards[1])}.png'
        self.ids.label1.text = str(
            f"Your hand: {self.player_hand.cards[0]} {self.player_hand.cards[1]}  |  val: {self.player_hand.get_value()}")



    # fce pro pridavani sazek
    def Addup(self):
        # uz jednou vsadil
        if self.bet == True:
            PUzVsazeno = Factory.MyPopup()
            PUzVsazeno.ids.Pmessage.text = 'Uz jste si jednou vsadil, dejte hit nebo stand'
            PUzVsazeno.ids.Pbutton.text = 'zavrit'
            PUzVsazeno.open()
        # prazdny input
        elif self.ids.text_input.text == '' and self.skore.get_score() != 1:
            PChybneZadani = Factory.MyPopup()
            PChybneZadani.ids.Pmessage.text = 'Zadejte sazku'
            PChybneZadani.ids.Pbutton.text = 'zavrit'
            PChybneZadani.open()


        # restart hry, pokud hrac prohraje a ma 1 zeton
        if self.bet == False and self.skore.get_score() == 1:
            PResetHry = Factory.MyPopup()
            PResetHry.ids.Pmessage.text = 'Restart hry'
            PResetHry.ids.Pbutton.text = 'ok'
            PResetHry.open()
            self.skore.addup_score(100-1)
            self.ids.label_score.text = str(self.skore.get_score())
            self.playstart()
        # sazka
        elif self.bet == False and self.ids.text_input.text != '':
            self.bet = True
            if self.skore.get_score() < int(self.ids.text_input.text):
                self.bet = False
                PMocZetonu = Factory.MyPopup()
                PMocZetonu.ids.Pmessage.text = 'Nemate tolik zetonu'
                PMocZetonu.ids.Pbutton.text = 'zavrit'
                PMocZetonu.open()
                self.ids.text_input.text = ''
            else:
                self.skore.deduct_score(int(self.ids.text_input.text))
                self.castkabet = int(self.ids.text_input.text)
                self.ids.label_bet.text = str(self.castkabet)
                if self.skore.get_score() <= 0:
                    self.bet = False
                    self.skore.addup_score(int(self.ids.text_input.text))
                    #self.ids.label_bet.text = ''
                    PZeroZetonu = Factory.MyPopup()
                    PZeroZetonu.ids.Pmessage.text = 'Nemuzete mit 0 zetonu, zadejte mensi castku'
                    PZeroZetonu.ids.Pbutton.text = 'zavrit'
                    PZeroZetonu.open()
                else:
                    self.ids.label_score.text = str(self.skore.get_score())

        self.ids.text_input.text = ''

    # fce pro dalsi kartu
    def Hit(self):
        if self.bet == True:
            if self.player_hand.get_value() == 21:
                PBJ = Factory.MyPopup()
                PBJ.ids.Pmessage.text = 'Mate BlackJack! Nechcete dalsi kartu'
                PBJ.ids.Pbutton.text = 'zavrit'
                PBJ.open()

            elif self.hit == False:
                self.hit = True
                self.player_hand.add_card(self.deck.deal())
                #self.player_hand.DEBUG_LISTCARDS()
                self.ids.label1.text = str(
                    f"Your hand: {' '.join(str(card) for card in self.player_hand.cards)}  |  val: {self.player_hand.get_value()}")
                # print(str(self.player_hand.cards[2]))
                self.ids.img3karty.source = f'txtkarty/{str(self.player_hand.cards[2])}.png'
                if self.player_hand.get_value() > 21:
                    PBust = Factory.MyPopup()
                    PBust.ids.Pmessage.text = 'Bust!'
                    PBust.ids.Pbutton.text = 'zavrit'
                    PBust.open()
                    self.playstart()

            else:
                PHit = Factory.MyPopup()
                PHit.ids.Pmessage.text = 'Uz jste jednou hittoval!'
                PHit.ids.Pbutton.text = 'zavrit'
                PHit.open()


        else:
            PVsad = Factory.MyPopup()
            PVsad.ids.Pmessage.text = 'Nejdrive vsadte castku'
            PVsad.ids.Pbutton.text = 'zavrit'
            PVsad.open()


    # fce pro ukazani vysledku
    def Stand(self):
        if self.bet == True:
            PStand = Factory.MyPopup()
            PStand.ids.Pbutton.text = 'zavrit'

            # check v pripade vyhry
            if self.player_hand.get_value() > self.dealer_hand.get_value() and self.player_hand.get_value() < 21:
                self.skore.addup_score(self.castkabet*2)
                #print(f'U win with {self.player_hand.get_value()} points, delears hand was {self.dealer_hand.get_value()}')
                PStand.ids.Pmessage.text = f'Vyhravate! S hodnotou {self.player_hand.get_value()}'

            # mozny blackjack
            elif self.player_hand.get_value() == 21:
                # pokud jsou jen 2 karty = blackjack
                if len(self.player_hand.cards) == 2:
                    # jestli nema dealer take
                    if self.dealer_hand.get_value() == self.player_hand.get_value():
                        self.skore.addup_score(self.castkabet)
                        PStand.ids.Pmessage.text = 'Mate stejnou value ruky, zetony vam zustanou!'
                        PStand.ids.Pbutton.text = 'zavrit'
                    else:
                        self.castkabet += self.castkabet*2
                        self.skore.addup_score(self.castkabet)
                        PStand.ids.Pmessage.text = 'Mate BlackJack!'
                        PStand.ids.Pbutton.text = 'zavrit'

                # 3 karty, nemuze byt blackjack
                else:
                    # check vyhra
                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        self.skore.addup_score(self.castkabet * 2)
                        PStand.ids.Pmessage.text = f'Vyhravate! S hodnotou {self.player_hand.get_value()}'
                        PStand.ids.Pbutton.text = 'zavrit'
                    # stejna ruka
                    else:
                        self.skore.addup_score(self.castkabet)
                        PStand.ids.Pmessage.text = 'Mate stejnou value ruky, sazka zustava!'
                        PStand.ids.Pbutton.text = 'zavrit'


            # stejna ruka
            elif self.dealer_hand.get_value() == self.player_hand.get_value():
                self.skore.addup_score(self.castkabet)
                PStand.ids.Pmessage.text = 'Mate stejnou value ruky, sazka zustava!'
                PStand.ids.Pbutton.text = 'zavrit'
            # prohra
            else:
                #print(f'U lose with {self.player_hand.get_value()} points, delears hand was {self.dealer_hand.get_value()}')
                PStand.ids.Pmessage.text = f'Prohra! S hodnotou {self.player_hand.get_value()}'


            PStand.open()
            self.ids.label_score.text = str(self.skore.get_score())
            self.playstart()


        else:
            PVsad = Factory.MyPopup()
            PVsad.ids.Pmessage.text = 'Nejdrive vsadte castku'
            PVsad.ids.Pbutton.text = 'zavrit'
            PVsad.open()


# Build
class BudgetBlackJackApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    BudgetBlackJackApp().run()


