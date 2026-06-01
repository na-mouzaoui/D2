import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ButtonGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Grid 47x14")
        
        # Store clicked buttons
        self.clicked_buttons = set()
        
        # Define the button labels
        self._0d1 = "\n d\n \'"
        self._0d2 = "\n d\n \' \'"
        self._1d0 = " \'\n d"
        self._1d1 = " \'\n d\n \'"
        self._1d2 = " \'\n d\n \' \'"
        self._2d0 = " \' \'\n d\n"
        self._2d1 = " \' \'\n d\n \'"
        self._2d2 = " \' \'\n d\n \' \'"
        self._0p1 = "\n p\n \'"
        self._0p2 = "\n p\n \' \'"
        self._1p0 = " \'\n p"
        self._1p1 = " \'\n p\n \'"
        self._1p2 = " \'\n p\n \' \'"
        self._2p0 = " \' \'\n p\n"
        self._2p1 = " \' \'\n p\n \'"
        self._2p2 = " \' \'\n p\n \' \'"

        # Create main container
        self.main_container = ttk.Frame(root)
        self.main_container.pack(expand=True, fill='both', padx=5, pady=5)

        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.main_container)
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create grid container
        self.grid_frame = ttk.Frame(self.scrollable_frame)
        self.grid_frame.pack(expand=True, fill='both', padx=5)

        # Bind mouse wheel
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Create buttons grid
        self.create_button_grid(self.grid_frame)

        # Create validate button and clicked buttons display
        self.create_bottom_panel()

        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_button_grid(self, parent):
        # Create line numbers
        for row in range(14):
            line_label = ttk.Label(parent, text=f"{row+1:02d}")
            line_label.grid(row=row, column=0, padx=(0, 5))

        # Define the pattern for the buttons (47 columns x 14 rows)
        pattern = [
		[self._0d2 , self._0d1,self._2p0,self._2d1,self._2d0,self._0d2,self._0p2,self._1p1,self._1d1,self._0p2,self._2d0,self._0d2,self._2d0,self._2d1,self._1d1,self._1p1,self._2d2,self._0p2,self._0d2,self._1d0,self._0d1,self._2p0,self._1p0,self._0d2,self._1d1,self._2d2,self._0d2,self._1d0,self._1d1,self._2p0,self._2d2,self._1p0,self._0d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0d2,self._1d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0p2,self._0d2,self._0d2,self._2p0],
        [self._2p0 ,self._2d0 ,self._1p0,self._2p0,self._0d2,self._0d1,self._2d2,self._1d1,self._2p0,self._2d2,self._1p0,self._1d2,self._0d2,self._0d2,self._2p0,self._0d2,self._1d0,self._0p2,self._1d1,self._0p2,self._0d2,self._0p1,self._2d0,self._1d1,self._0p2,self._0d1,self._2p0,self._2d1,self._0d2,self._2d0,self._0d1,self._2p0,self._0d2,self._0p2,self._1d1,self._1p1,self._2d0,self._1p0,self._2d0,self._0d2,self._1d1,self._0d2,self._2p0,self._2d0,self._0p2,self._1d1,self._2d0],
        [self._2d2 , self._1d0,self._0d2,self._2d0,self._2p0,self._0p2,self._2d0,self._0p1,self._1d1,self._0p1,self._2p0,self._0p2,self._1d1,self._0d2,self._2p0,self._1d1,self._2p0,self._2d0,self._1p0,self._2d1,self._2d0,self._1p0,self._1d1,self._0p2,self._1d2,self._1d1,self._0p1,self._0d2,self._2p0,self._0p2,self._0d1,self._2d0,self._2d2,self._2d0,self._1p1,self._2d1,self._2d0,self._2p0,self._1d1,self._0p2,self._0d2,self._2d0,self._1d1,self._0d1,self._2d0,self._2p0,self._1d1],
        [self._0d2 , self._0d1,self._2p0,self._2d1,self._2d0,self._0d2,self._0p2,self._1p1,self._1d1,self._0p2,self._2d0,self._0d2,self._2d0,self._2d1,self._1d1,self._1p1,self._2d2,self._0p2,self._0d2,self._1d0,self._0d1,self._2p0,self._1p0,self._0d2,self._1d1,self._2d2,self._0d2,self._1d0,self._1d1,self._2p0,self._2d2,self._1p0,self._0d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0d2,self._1d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0p2,self._0d2,self._0d2,self._2p0],
        [self._2p0 ,self._2d0 ,self._1p0,self._2p0,self._0d2,self._0d1,self._2d2,self._1d1,self._2p0,self._2d2,self._1p0,self._1d2,self._0d2,self._0d2,self._2p0,self._0d2,self._1d0,self._0p2,self._1d1,self._0p2,self._0d2,self._0p1,self._2d0,self._1d1,self._0p2,self._0d1,self._2p0,self._2d1,self._0d2,self._2d0,self._0d1,self._2p0,self._0d2,self._0p2,self._1d1,self._1p1,self._2d0,self._1p0,self._2d0,self._0d2,self._1d1,self._0d2,self._2p0,self._2d0,self._0p2,self._1d1,self._2d0],
        [self._2d2 , self._1d0,self._0d2,self._2d0,self._2p0,self._0p2,self._2d0,self._0p1,self._1d1,self._0p1,self._2p0,self._0p2,self._1d1,self._0d2,self._2p0,self._1d1,self._2p0,self._2d0,self._1p0,self._2d1,self._2d0,self._1p0,self._1d1,self._0p2,self._1d2,self._1d1,self._0p1,self._0d2,self._2p0,self._0p2,self._0d1,self._2d0,self._2d2,self._2d0,self._1p1,self._2d1,self._2d0,self._2p0,self._1d1,self._0p2,self._0d2,self._2d0,self._1d1,self._0d1,self._2d0,self._2p0,self._1d1],
        [self._0d2 , self._0d1,self._2p0,self._2d1,self._2d0,self._0d2,self._0p2,self._1p1,self._1d1,self._0p2,self._2d0,self._0d2,self._2d0,self._2d1,self._1d1,self._1p1,self._2d2,self._0p2,self._0d2,self._1d0,self._0d1,self._2p0,self._1p0,self._0d2,self._1d1,self._2d2,self._0d2,self._1d0,self._1d1,self._2p0,self._2d2,self._1p0,self._0d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0d2,self._1d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0p2,self._0d2,self._0d2,self._2p0],
        [self._2p0 ,self._2d0 ,self._1p0,self._2p0,self._0d2,self._0d1,self._2d2,self._1d1,self._2p0,self._2d2,self._1p0,self._1d2,self._0d2,self._0d2,self._2p0,self._0d2,self._1d0,self._0p2,self._1d1,self._0p2,self._0d2,self._0p1,self._2d0,self._1d1,self._0p2,self._0d1,self._2p0,self._2d1,self._0d2,self._2d0,self._0d1,self._2p0,self._0d2,self._0p2,self._1d1,self._1p1,self._2d0,self._1p0,self._2d0,self._0d2,self._1d1,self._0d2,self._2p0,self._2d0,self._0p2,self._1d1,self._2d0],
        [self._2d2 , self._1d0,self._0d2,self._2d0,self._2p0,self._0p2,self._2d0,self._0p1,self._1d1,self._0p1,self._2p0,self._0p2,self._1d1,self._0d2,self._2p0,self._1d1,self._2p0,self._2d0,self._1p0,self._2d1,self._2d0,self._1p0,self._1d1,self._0p2,self._1d2,self._1d1,self._0p1,self._0d2,self._2p0,self._0p2,self._0d1,self._2d0,self._2d2,self._2d0,self._1p1,self._2d1,self._2d0,self._2p0,self._1d1,self._0p2,self._0d2,self._2d0,self._1d1,self._0d1,self._2d0,self._2p0,self._1d1],
        [self._0d2 , self._0d1,self._2p0,self._2d1,self._2d0,self._0d2,self._0p2,self._1p1,self._1d1,self._0p2,self._2d0,self._0d2,self._2d0,self._2d1,self._1d1,self._1p1,self._2d2,self._0p2,self._0d2,self._1d0,self._0d1,self._2p0,self._1p0,self._0d2,self._1d1,self._2d2,self._0d2,self._1d0,self._1d1,self._2p0,self._2d2,self._1p0,self._0d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0d2,self._1d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0p2,self._0d2,self._0d2,self._2p0],
        [self._2p0 ,self._2d0 ,self._1p0,self._2p0,self._0d2,self._0d1,self._2d2,self._1d1,self._2p0,self._2d2,self._1p0,self._1d2,self._0d2,self._0d2,self._2p0,self._0d2,self._1d0,self._0p2,self._1d1,self._0p2,self._0d2,self._0p1,self._2d0,self._1d1,self._0p2,self._0d1,self._2p0,self._2d1,self._0d2,self._2d0,self._0d1,self._2p0,self._0d2,self._0p2,self._1d1,self._1p1,self._2d0,self._1p0,self._2d0,self._0d2,self._1d1,self._0d2,self._2p0,self._2d0,self._0p2,self._1d1,self._2d0],
        [self._2d2 , self._1d0,self._0d2,self._2d0,self._2p0,self._0p2,self._2d0,self._0p1,self._1d1,self._0p1,self._2p0,self._0p2,self._1d1,self._0d2,self._2p0,self._1d1,self._2p0,self._2d0,self._1p0,self._2d1,self._2d0,self._1p0,self._1d1,self._0p2,self._1d2,self._1d1,self._0p1,self._0d2,self._2p0,self._0p2,self._0d1,self._2d0,self._2d2,self._2d0,self._1p1,self._2d1,self._2d0,self._2p0,self._1d1,self._0p2,self._0d2,self._2d0,self._1d1,self._0d1,self._2d0,self._2p0,self._1d1],
        [self._0d2 , self._0d1,self._2p0,self._2d1,self._2d0,self._0d2,self._0p2,self._1p1,self._1d1,self._0p2,self._2d0,self._0d2,self._2d0,self._2d1,self._1d1,self._1p1,self._2d2,self._0p2,self._0d2,self._1d0,self._0d1,self._2p0,self._1p0,self._0d2,self._1d1,self._2d2,self._0d2,self._1d0,self._1d1,self._2p0,self._2d2,self._1p0,self._0d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0d2,self._1d2,self._2d0,self._2p0,self._0p2,self._1d1,self._0p2,self._0d2,self._0d2,self._2p0],
        [self._2p0 ,self._2d0 ,self._1p0,self._2p0,self._0d2,self._0d1,self._2d2,self._1d1,self._2p0,self._2d2,self._1p0,self._1d2,self._0d2,self._0d2,self._2p0,self._0d2,self._1d0,self._0p2,self._1d1,self._0p2,self._0d2,self._0p1,self._2d0,self._1d1,self._0p2,self._0d1,self._2p0,self._2d1,self._0d2,self._2d0,self._0d1,self._2p0,self._0d2,self._0p2,self._1d1,self._1p1,self._2d0,self._1p0,self._2d0,self._0d2,self._1d1,self._0d2,self._2p0,self._2d0,self._0p2,self._1d1,self._2d0]]
        

        # Create style for clicked buttons
        style = ttk.Style()
        style.configure('Clicked.TButton', background='black', relief='sunken')

        # Create buttons
        for row in range(14):
            for col in range(47):
                button = ttk.Button(
                    parent,
                    text=pattern[row][col],
                    width=3
                )
                button.grid(row=row, column=col+1, padx=1, pady=1, sticky='nsew')
                # Store button coordinates in the button itself
                button.position = (row, col)
                button.bind('<Button-1>', self.on_button_click)

    def create_bottom_panel(self):
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill='x', padx=5, pady=5)

        # Create validate button
        validate_button = ttk.Button(bottom_frame, text="Valider", command=self.validate)
        validate_button.pack(side='left', padx=5)

        # Create clicked buttons display
        self.clicked_display = scrolledtext.ScrolledText(bottom_frame, height=3)
        self.clicked_display.pack(fill='x', padx=5, expand=True)

    def on_button_click(self, event):
        button = event.widget
        pos = f"({button.position[0]}, {button.position[1]})"
        
        if pos in self.clicked_buttons:
            # Unclick button
            button.configure(style='TButton')
            self.clicked_buttons.remove(pos)
        else:
            # Click button
            button.configure(style='Clicked.TButton')
            self.clicked_buttons.add(pos)
        
        # Update display
        self.update_clicked_display()

    def update_clicked_display(self):
        self.clicked_display.delete(1.0, tk.END)
        if self.clicked_buttons:
            self.clicked_display.insert(tk.END, f"Boutons cliqués: {', '.join(sorted(self.clicked_buttons))}")
        else:
            self.clicked_display.insert(tk.END, "Aucun bouton cliqué")

    def validate(self):
        print("Boutons validés:", sorted(self.clicked_buttons))

def main():
    root = tk.Tk()
    app = ButtonGridApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()