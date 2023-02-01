# BudgetBlackJack

Budget black jack aplikace sloužící k základnímu předvedení Kivy GUI a práce s ním. Implementován jednoduchý princip BlackJacku s možností maximálně líznout si 1 další kartu, dealer má k dispozici pouze 2 karty. Aplikace nepracuje s možností sázet na více variant krom výhry.



## Kivy file syntax highlighting
   1. stáhnout .jar [soubor](https://github.com/JohnySmid/BudgetBlackJack/blob/main/PyCharm_kv_completion.jar)
   2. V Pycharmu main menu, kliknout "File" -> "Manage IDE Settings" -> "Import Settings".
   3. Vybrat .jar soubor a kliknout OK.
   4. Restart PyCharmu.<br />
   [zdroj](https://stackoverflow.com/questions/38002630/how-to-get-syntax-highlighting-on-kivy-kv-file-in-pycharm-on-osx)

## PIP Installation
```bash
python -m pip install "kivy[base]" kivy_examples --no-binary kivy
```
## TODO:
   - ošetřit pouze čísla v textfile
   - dodělat pravidlo, že pokud hodnota dealera bude 17<=, tak si lízne další kartu
   - využívat pouze 1 Deck dokud to půjde, pak vytvořit nový
   - upravit GUI pro více karet se ScreenManagerem (v kivy problém s listem IDS při využití více screen)
   - možnost "registrace / login" do / z databáze a ukládání skóre
