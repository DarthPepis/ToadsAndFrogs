# Toads and Frogs – Python Implementace
Tento projekt obsahuje implementaci hry Toads and Frogs v Pythonu, 
včetně jednoduchého GUI, AI hráče (minimax + alfa-beta pruning), 
programátorské dokumentace, uživatelské dokumentace a ručních testů.

## Spuštění programu
Program se spouští v libovolném IDE, tlačítkem RUN přes soubor: app/main.py
po spuštění programu se otevře setup okno, kde si tlačítky zvolíte rozměry hrací desky,
následně zvolíte režim hráč vs AI nebo AI vs AI, poté se vám zobrazí start tlačítko,
jehož stisknutím zahájíte hru. Hra se ovládá kliknutím na políčko, kterým chcete táhnout(vlastní figurkou)
a následným kliknutím na pole, na které chcete táhnout

## Testování
Ruční testy jsou v souboru: app/testing.py
Spustíte je v IDE spuštěním tohoto filu


## Struktura projektu
- Python aplikace:
    - `složka app`:
        - `main.py` – spuštění programu  
        - `gui.py` – grafické rozhraní  
        - `game_state.py` – logika hry  
        - `ai.py` – minimax + alfa-beta pruning  
        - `testing.py` – ruční testy, nemají vliv na funkčnost aplikace, pouze zkoumají její přesnost

- Doprovodné dokumenty:
    - `programatorskadokumentace.pdf` - programátorská dokumentace k programu
    - `userguide.pdf` - dokument pro spuštění a ovládání programu

- Ostatní:
    - `README.md` - doprovodný file pro GitHub
