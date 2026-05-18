import tkinter as tk
from backend import FinanceBackend
from frontend import ExpenseAppFrontend

def main():
    # Instanciar el backend que maneja Pandas
    backend = FinanceBackend()

    # Configurar la ventana principal de Tkinter
    root = tk.Tk()
    
    # Instanciar el frontend pasándole el backend
    app = ExpenseAppFrontend(root, backend)
    
    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
