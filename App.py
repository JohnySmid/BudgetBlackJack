from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory


import Hand
import Deck



Window.size = (700, 400)

# vyuziti kivy.lang knihovny pro pouziti .kv souboru
Builder.load_file('UI.kv')

# pro jednoduche trackovani skore, init pri spusteni aplikace, pak jen davam na puvodni hodnoty
class ScoreTracker:
    def __init__(self):
        self.score = 100

    # odecita skore
    def deduct_score(self, update):
        self.score -= update

    #prida skore
    def addup_score(self, update):
        self.score += update

    #vrati skore
    def get_score(self):
        return self.score

# Layout
class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playstart()
        # inicializace ScoreTrackeru()
        self.skore = ScoreTracker()
        # nastavi text labelu na nase urcene skore
        self.ids.label_score.text = str(self.skore.get_score())

    # pro debug ucely, jsem si udelal fci na "start", zbytecna ale pouzivam ji
    def playstart(self):
        self.start()

    # funkce na hru
    def start(self):
        # init decku, s kazdym kolem se udela novy deck
        self.deck = Deck.Deck()
        # zamicha deck
        self.deck.shuffle()

        # promene slouzici ke hre
        self.hit = False
        self.played = False
        self.bet = False
        self.castkabet = 0

        # kivy widgety
        self.ids.img1karty.source = ''
        self.ids.img2karty.source = ''
        self.ids.img3karty.source = ''
        self.ids.label_bet.text = ''


        # inicializace ruky hrace a dealera
        self.player_hand = Hand.Hand()
        self.dealer_hand = Hand.Hand()

        # prida karty do ruky hrace a dealera
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())



        # txt karet
        self.ids.img1karty.source = f'txtkarty/{str(self.player_hand.cards[0])}.png'
        self.ids.img2karty.source = f'txtkarty/{str(self.player_hand.cards[1])}.png'

        # label pod texturami karet
        self.ids.label1.text = str(
            f"Your hand: {self.player_hand.cards[0]} {self.player_hand.cards[1]}  |  val: {self.player_hand.get_value()}")



    # f-ce pro pridavani sazek
    def Addup(self):
        # uz jednou vsadil
        if self.bet == True:
            # PopUp - definovan na zacatku .kv souboru
            # widgety to jiz obsahuje, menime pouze jejich hodnoty
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
            # pokud zadame vice nez mame zetonu
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

                # pokud mame 0 a min zetonu
                if self.skore.get_score() <= 0:
                    self.bet = False
                    # musime pridat skore, jelikoz uz jsme odecetli
                    self.skore.addup_score(int(self.ids.text_input.text))
                    PZeroZetonu = Factory.MyPopup()
                    PZeroZetonu.ids.Pmessage.text = 'Nemuzete mit 0 zetonu, zadejte mensi castku'
                    PZeroZetonu.ids.Pbutton.text = 'zavrit'
                    PZeroZetonu.open()
                else:
                    self.ids.label_score.text = str(self.skore.get_score())

        self.ids.text_input.text = ''

    # f-ce pro dalsi kartu
    def Hit(self):
        # pokud vsazeno
        if self.bet == True:
            # pokud chceme dalsi kartu s BlackJackem v ruce
            if self.player_hand.get_value() == 21:
                PBJ = Factory.MyPopup()
                PBJ.ids.Pmessage.text = 'Mate BlackJack! Nechcete dalsi kartu'
                PBJ.ids.Pbutton.text = 'zavrit'
                PBJ.open()

            elif self.hit == False:
                self.hit = True
                # prida kartu
                self.player_hand.add_card(self.deck.deal())
                # self.player_hand.DEBUG_LISTCARDS()
                # vypis listu s mezerou
                self.ids.label1.text = str(
                    f"Your hand: {' '.join(str(card) for card in self.player_hand.cards)}  |  val: {self.player_hand.get_value()}")

                self.ids.img3karty.source = f'txtkarty/{str(self.player_hand.cards[2])}.png'

                # Bust
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


    # f-ce pro ukazani vysledku
    def Stand(self):
        if self.bet == True:
            # pop up
            PStand = Factory.MyPopup()
            PStand.ids.Pbutton.text = 'zavrit'

            # check v pripade vyhry
            if self.player_hand.get_value() > self.dealer_hand.get_value() and self.player_hand.get_value() < 21:
                self.skore.addup_score(self.castkabet*2)
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
                PStand.ids.Pmessage.text = f'Prohra! S hodnotou {self.player_hand.get_value()}'


            PStand.open()
            self.ids.label_score.text = str(self.skore.get_score())

            # spusti se nova hra
            self.playstart()


        else:
            PVsad = Factory.MyPopup()
            PVsad.ids.Pmessage.text = 'Nejdrive vsadte castku'
            PVsad.ids.Pbutton.text = 'zavrit'
            PVsad.open()
