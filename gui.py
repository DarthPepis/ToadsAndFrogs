import tkinter as tk
from tkinter import Toplevel
from game_state import GameState, Move
from ai import find_best_move

class ToadsAndFrogsGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Toads and Frogs")

        self.mode = None #nemame nastaveny mod
        # otevřít dialog pro nastavení
        self.show_setup_dialog()

    def set_mode(self, mode):
        self.mode = mode

        self.start_button.config(state = "normal", bg = "white")

    # -----------------------------
    # DIALOG PRO NASTAVENÍ HRY
    # -----------------------------
    def show_setup_dialog(self):
        # pokud existuje staré GUI, smažeme ho
        for widget in self.root.winfo_children():  #winfo_children vraci seznam všech widgetu
            widget.destroy()

        self.setup = Toplevel(self.root) #udělame nove okno nad hlavnim oknem Tk()
        self.setup.title("Nastavení hry")
        self.setup.geometry("260x220")
        self.setup.grab_set() #dokud nesmažu okno z rodiče, user nemuže kliknout na root
 
        # výchozí hodnoty
        self.toads = 2
        self.frogs = 2
        self.empty = 3

        # pomocná funkce na vytvoření CELÉHO řádku
        def add_row(label, get, set):
            frame = tk.Frame(self.setup)
            frame.pack(pady=5)

            #nazev řadku
            label = tk.Label(frame, text = label, width = 15)
            label.pack(side = tk.LEFT) #cely řadek zarovnavame doleva

            def minus_click():
                current_value = get() #vraci aktualni hodnotu, je to podfunkce add_row, každy řadek ma svoje get, set
                new_value = max(0, current_value - 1)
                set(new_value) #nastavi hodnotu na novou

            minus_button = tk.Button(frame, text = "-", width = 3, command = minus_click) #pouze reference na funkci, jinak by se spustila hned při vytvořeni btn
            minus_button.pack(side = tk.LEFT)

            #aktualni hodnota na řadku
            value_label = tk.Label(frame, text=str(get()), width=4)
            value_label.pack(side=tk.LEFT)


            def plus_click():
                current_value = get() #vraci aktualni hodnotu
                new_value = current_value + 1
                set(new_value) #nastavi hodnotu na novou

            plus_button = tk.Button(frame, text = "+", width = 3, command = plus_click)
            plus_button.pack(side = tk.LEFT)

            return value_label

        def get_toads():
            return self.toads
        
        def set_toads(value):
            self.update_value("toads", value)

        def get_frogs():
            return self.frogs

        def set_frogs(value):
            self.update_value("frogs", value)

        # Toads řadek
        self.toads_label = add_row(
            "Počet Toads:",
            get_toads,        #opět chceme jen referenci
            set_toads
        )

        # Frogs řadek
        self.frogs_label = add_row(
            "Počet Frogs:",
            get_frogs,
            set_frogs
        )
        #prazdna mista radku
        def get_empty():
            return self.empty
        def set_empty(value):
            self.update_value("empty", value)

        self.empty_label = add_row(
            "Prázdná místa:",
            get_empty,
            set_empty
        )


        tk.Label(self.setup, text="Režim hry:").pack(pady=5)

        tk.Button(self.setup, text="Hráč vs AI",
          command=lambda: self.set_mode("HUMAN_VS_AI")).pack(pady=2)

        tk.Button(self.setup, text="AI vs AI",
          command=lambda: self.set_mode("AI_VS_AI")).pack(pady=2)

        self.start_button = tk.Button(self.setup, text="Start", state = "disabled", bg="#cccccc", command=self.start_game)
        self.start_button.pack(pady=10)

    def update_value(self, name, value):
        setattr(self, name, value) #konkretni přiklad setattr(self, "toads", 5), pak self.toads = 5, měnime self.name
        if name == "toads":
            self.toads_label.config(text=str(value)) #konfigurujeme hodnotu labelu, měnime hodnotu v labelu
        elif name == "frogs":
            self.frogs_label.config(text=str(value))
        elif name == "empty":
            self.empty_label.config(text=str(value))

    # -----------------------------
    # START HRY
    # -----------------------------

    ###
    ###
    
    def start_game(self):
        if self.mode is None:
            return
        #pojistka


        # vytvořit pole podle nastavení
        board = ['T'] * self.toads + ['.'] * self.empty + ['F'] * self.frogs

        self.state = GameState(board, 1)
        self.setup.destroy() #mažu setup okno - TopLevel
        
        # GUI prvky
        self.selected_index = None #default
        self.ai_enabled = True
        self.ai_depth = 4 #hloubka minmax

        self.info_label = tk.Label(self.root, text="")#zde bude kdo je na tahu a info
        self.info_label.pack(pady=10)

        self.board_frame = tk.Frame(self.root)#zde budou board btns
        self.board_frame.pack()

        self.new_game_button = tk.Button(self.root, text="Nová hra", command=self.show_setup_dialog)
        self.new_game_button.pack(pady=10)

        self.update_board()

        

    # VYKRESLENÍ DESK

    
    def update_board(self):
        for w in self.board_frame.winfo_children(): #vykresluju board pokažde znova 
            w.destroy()

        for i, cell in enumerate(self.state.board): #self.state.board - přistup k board v GameState, aktualni board
            #enumerate vyhazuje index pole i a daný prvek na pozici i, 
            # self.state je Gamestate, z definice třidy je self.state.board = board
            if cell == 'T':
                text = 'T'
            elif cell == 'F':
                text = 'F'
            else:
                text = '.'
            
            #lambda zavola funkci ktera položi idx rovno indexu na ktery klikam
            btn = tk.Button(self.board_frame, text=text, width=4, height=2, command=lambda idx=i: self.on_click(idx) 
            )
            #tvořime tlačitko pro každy frame v 1xn poli
            btn.grid(row=0, column=i, padx=2, pady=2)

        if self.state.current_player == 1:
            self.info_label.config(text="Na tahu: hráč 1 (Toads)")
        else:
            self.info_label.config(text="Na tahu: hráč 2 (Frogs)")

        if self.state.is_terminal():
            if self.state.current_player == 1:
                self.info_label.config(text="Konec hry – hráč 1 nemá tah, prohrává.")
            else:
                self.info_label.config(text="Konec hry – hráč 2 nemá tah, prohrává.")
            return
        

        #hlavni if kde tahne AI
        if not self.state.is_terminal():
            if self.mode == "AI_VS_AI":
            # AI táhne za oba hráče
                self.root.after(500, self.ai_move)

            elif self.mode == "HUMAN_VS_AI" and self.state.current_player == 2:
            # AI táhne jen za Frogs
                self.root.after(500, self.ai_move)


    # -----------------------------
    # KLIKÁNÍ NA POLE
    # -----------------------------
    def on_click(self, idx: int):
        if self.mode == "AI_VS_AI":
            return   # hráč nehraje¨
        #opět hrač nehraje :`)
        if self.ai_enabled and self.state.current_player == 2:
            return
        
        #prvni kliknuti na pole kterym chceme tahnout
        if self.selected_index is None: 
            if self.state.current_player == 1 and self.state.board[idx] == 'T':
                self.selected_index = idx
            elif self.state.current_player == 2 and self.state.board[idx] == 'F':
                self.selected_index = idx
            return
        else:
            move = Move(self.selected_index, idx)
        if self.is_legal_move(move):
            self.state = self.state.apply_move(move)
        else:
            self.show_illegal_move()
            self.selected_index = None
            return  # DŮLEŽITÉ – zastaví funkci dřive než dojde k update_board, aby nesmazal hlášku v info_label

        self.selected_index = None #po tahu
        self.update_board()


    def is_legal_move(self, move: Move) -> bool:
        return any(m.from_idx == move.from_idx and m.to_idx == move.to_idx
                   for m in self.state.generate_moves())
    #jestliže alespoň 1 položka je true vraci true, m je tah z konkretniho stavu, jestliže vybrana dvojice nebude
    #ve všech možnych tazich pak to neni legal

    def show_illegal_move(self):
        self.info_label.config(text="Tento tah nelze provést.")
        self.root.after(1200, lambda: self.info_label.config(text=""))



    # AI tah
    def ai_move(self):
        best = find_best_move(self.state, self.ai_depth)
        if best:
            self.state = self.state.apply_move(best)

        #pokud nenajdeme best move tak game is terminal, loop v update_board
        self.update_board()
