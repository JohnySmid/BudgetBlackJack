# BudgetBlackJack

Budget black jack aplikace sloužící k základnímu předvedení Kivy GUI a práce s ním. </br>
Implementován jednoduchý princip BlackJacku s možností si maximálně líznout 1 další kartu, dealer má k dispozici pouze 2 karty. Aplikace nepracuje s možností sázet na více variant krom výhry, ani s pravidlem hodnoty 17<= pro dealera (pokud je hodnota menší jak 17, líže si další kartu).

# .py soubory
   1. Cards.py
      - zde jsou definovány karty (jejich barva a hodnota)
   2. Deck.py
      - zde je definován balík, který se vytvoří jakožto list z karet
      - dále implementován shuffle a deal funkce
   3. Hand.py
      - zde ruka definována jako list
      - funkce na přidání karty do ruky
      - funkce na získání hodnoty ruky (pracuje i s pravidlem hodnot Es +1/+10)
   4. App.py
      - funkčnost aplikace
   5. main.py
      - pro spuštění GUI
   6. UI.kv
      - kivy soubor


## PIP Installation
```bash
python -m pip install "kivy[base]" kivy_examples --no-binary kivy
```


## PyCharm Kivy file syntax highlighting
   1. stáhnout .jar [soubor](https://github.com/JohnySmid/BudgetBlackJack/blob/main/PyCharm_kv_completion.jar)
   2. V Pycharmu main menu, kliknout "File" -> "Manage IDE Settings" -> "Import Settings".
   3. Vybrat .jar soubor a kliknout OK.
   4. Restart PyCharmu.<br />
   [zdroj](https://stackoverflow.com/questions/38002630/how-to-get-syntax-highlighting-on-kivy-kv-file-in-pycharm-on-osx)
   
   
## TODO:
   - dodělat pravidlo, že pokud hodnota dealera bude 17<=, tak si lízne další kartu
   - využívat pouze 1 Deck dokud to půjde, pak vytvořit nový
   - upravit GUI pro více karet
   - možnost "registrace / login" do / z databáze a ukládání skóre (pro zachování stavu po zavření aplikace)
   - přidat více hráčů