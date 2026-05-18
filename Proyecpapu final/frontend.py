import tkinter as tk
from tkinter import ttk, messagebox
# pyrefly: ignore [missing-import]
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import pandas as pd


class ExpenseAppFrontend:
    def __init__(self, root, backend):
        self.root = root
        self.backend = backend
        self.root.title("Monitoreo de Gastos para Familias")
        self.root.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Crear contenedor de pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear Pestañas
        self.tab_registro = ttk.Frame(self.notebook)
        self.tab_busqueda = ttk.Frame(self.notebook)
        self.tab_reportes = ttk.Frame(self.notebook)
        self.tab_analisis = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_registro, text="Registro")
        self.notebook.add(self.tab_busqueda, text="Búsqueda")
        self.notebook.add(self.tab_reportes, text="Reportes")
        self.notebook.add(self.tab_analisis, text="Análisis")

        # Rellenar cada pestaña
        self.build_registro_tab()
        self.build_busqueda_tab()
        self.build_reportes_tab()
        self.build_analisis_tab()

        # Actualizar datos al cambiar de pestaña
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def build_registro_tab(self):
        frame = ttk.LabelFrame(self.tab_registro, text="Nuevo Registro", padding=20)
        frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        # Tipo
        ttk.Label(frame, text="Tipo:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.tipo_var = tk.StringVar(value="Gasto")
        self.tipo_combo = ttk.Combobox(frame, textvariable=self.tipo_var, values=["Ingreso", "Gasto"], state="readonly")
        self.tipo_combo.grid(row=0, column=1, pady=10, sticky=tk.EW)
        self.tipo_combo.bind("<<ComboboxSelected>>", self.actualizar_categorias)

        # Fecha
        ttk.Label(frame, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.fecha_var = tk.StringVar(value=datetime.today().strftime('%Y-%m-%d'))
        ttk.Entry(frame, textvariable=self.fecha_var).grid(row=1, column=1, pady=10, sticky=tk.EW)

        # Categoria
        ttk.Label(frame, text="Categoría:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.cat_var = tk.StringVar()
        self.cat_combo = ttk.Combobox(frame, textvariable=self.cat_var, state="readonly")
        self.cat_combo.grid(row=2, column=1, pady=10, sticky=tk.EW)

        # Monto
        ttk.Label(frame, text="Monto:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.monto_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.monto_var).grid(row=3, column=1, pady=10, sticky=tk.EW)

        # Boton Guardar
        ttk.Button(frame, text="Guardar Registro", command=self.guardar_registro).grid(row=4, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)
        
        # Inicializar categorías
        self.actualizar_categorias()

    def actualizar_categorias(self, event=None):
        tipo = self.tipo_var.get()
        if tipo == "Gasto":
            categorias = [
                "Alimentos y Despensa", "Transporte Público", "Combustible y Peajes",
                "Educación (Colegiaturas, Útiles)", "Servicios (Agua, Luz, Gas)", 
                "Internet y Telefonía", "Salud y Medicamentos", "Renta / Hipoteca", 
                "Entretenimiento y Ocio", "Ropa y Calzado", "Mascotas", 
                "Cuidado Personal", "Mantenimiento del Hogar", "Suscripciones", "Otros Gastos"
            ]
        else:
            categorias = [
                "Salario Principal", "Bonos y Aguinaldo", "Negocios e Inversiones",
                "Trabajos Freelance", "Venta de Artículos", "Rentas de Propiedades",
                "Subsidios / Ayudas", "Regalos", "Otros Ingresos"
            ]
        self.cat_combo['values'] = categorias
        if categorias:
            self.cat_combo.current(0)

    def guardar_registro(self):
        tipo = self.tipo_var.get()
        fecha = self.fecha_var.get()
        categoria = self.cat_var.get()
        monto = self.monto_var.get()

        if not categoria or not monto:
            messagebox.showwarning("Error", "Categoría y Monto son obligatorios")
            return

        try:
            float(monto)
        except ValueError:
            messagebox.showwarning("Error", "El monto debe ser un número válido")
            return

        self.backend.add_record(tipo, fecha, categoria, monto)
        messagebox.showinfo("Éxito", "Registro guardado correctamente")
        
        # Limpiar
        self.monto_var.set("")
        self.cat_var.set("")

    def build_busqueda_tab(self):
        # Filtros
        filtro_frame = ttk.LabelFrame(self.tab_busqueda, text="Filtros de Búsqueda")
        filtro_frame.pack(fill=tk.X, padx=10, pady=10)

        # Tipo
        ttk.Label(filtro_frame, text="Tipo:").grid(row=0, column=0, padx=5, pady=5)
        self.search_tipo = tk.StringVar(value="Todos")
        ttk.Combobox(filtro_frame, textvariable=self.search_tipo, values=["Todos", "Ingreso", "Gasto"], state="readonly", width=10).grid(row=0, column=1, padx=5, pady=5)

        # Categoria
        ttk.Label(filtro_frame, text="Categoría:").grid(row=0, column=2, padx=5, pady=5)
        self.search_cat = tk.StringVar(value="Todas")
        
        todas_categorias = ["Todas"] + [
            "Alimentos y Despensa", "Transporte Público", "Combustible y Peajes",
            "Educación (Colegiaturas, Útiles)", "Servicios (Agua, Luz, Gas)", 
            "Internet y Telefonía", "Salud y Medicamentos", "Renta / Hipoteca", 
            "Entretenimiento y Ocio", "Ropa y Calzado", "Mascotas", 
            "Cuidado Personal", "Mantenimiento del Hogar", "Suscripciones", "Otros Gastos",
            "Salario Principal", "Bonos y Aguinaldo", "Negocios e Inversiones",
            "Trabajos Freelance", "Venta de Artículos", "Rentas de Propiedades",
            "Subsidios / Ayudas", "Regalos", "Otros Ingresos"
        ]
        ttk.Combobox(filtro_frame, textvariable=self.search_cat, values=todas_categorias, state="readonly", width=30).grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(filtro_frame, text="Buscar", command=self.realizar_busqueda).grid(row=0, column=4, padx=10, pady=5)

        # Resultados
        res_frame = ttk.Frame(self.tab_busqueda)
        res_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columnas = ("Fecha", "Tipo", "Categoría", "Monto")
        self.tree = ttk.Treeview(res_frame, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=100, width=150)
            
        scrollbar = ttk.Scrollbar(res_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def realizar_busqueda(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        tipo = getattr(self, 'search_tipo', tk.StringVar(value="Todos")).get()
        cat = getattr(self, 'search_cat', tk.StringVar(value="Todas")).get()

        df = self.backend.get_records(tipo=tipo, categoria=cat)
        
        for _, row in df.iterrows():
            fecha_str = row['Fecha'].strftime('%Y-%m-%d') if pd.notnull(row['Fecha']) else ''
            self.tree.insert("", tk.END, values=(fecha_str, row['Tipo'], row['Categoria'], f"${row['Monto']:.2f}"))

    def build_reportes_tab(self):
        frame = ttk.Frame(self.tab_reportes)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.report_text = tk.Text(frame, wrap=tk.WORD, font=("Helvetica", 12))
        self.report_text.pack(fill=tk.BOTH, expand=True)

    def actualizar_reportes(self):
        self.report_text.delete(1.0, tk.END)
        
        ingresos, gastos = self.backend.get_summary()
        balance = ingresos - gastos
        
        texto = "=== RESUMEN FINANCIERO ===\n\n"
        texto += f"Total Ingresos: ${ingresos:.2f}\n"
        texto += f"Total Gastos: ${gastos:.2f}\n"
        texto += f"Balance Actual: ${balance:.2f}\n\n"
        
        texto += "=== ALERTAS DE GASTOS ===\n\n"
        alertas = self.backend.get_alerts()
        if alertas:
            for alerta in alertas:
                texto += f"- {alerta}\n"
        else:
            texto += "No hay alertas de gastos excesivos.\n"
            
        texto += "\n=== RECOMENDACIONES ===\n\n"
        texto += self.backend.get_recommendations()
        
        self.report_text.insert(tk.END, texto)

    def build_analisis_tab(self):
        # Frame izquierdo para el gráfico de torta
        self.frame_pie = ttk.Frame(self.tab_analisis)
        self.frame_pie.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame derecho para el gráfico de línea
        self.frame_line = ttk.Frame(self.tab_analisis)
        self.frame_line.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.canvas_pie = None
        self.canvas_line = None

    def actualizar_analisis(self):
        # Actualizar Torta
        fig_pie = self.backend.get_distribution_chart()
        if self.canvas_pie:
            self.canvas_pie.get_tk_widget().destroy()
        self.canvas_pie = FigureCanvasTkAgg(fig_pie, master=self.frame_pie)
        self.canvas_pie.draw()
        self.canvas_pie.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Actualizar Línea
        fig_line = self.backend.get_trend_chart()
        if self.canvas_line:
            self.canvas_line.get_tk_widget().destroy()
        self.canvas_line = FigureCanvasTkAgg(fig_line, master=self.frame_line)
        self.canvas_line.draw()
        self.canvas_line.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def on_tab_changed(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        
        if tab_text == "Búsqueda":
            self.realizar_busqueda()
        elif tab_text == "Reportes":
            self.actualizar_reportes()
        elif tab_text == "Análisis":
            self.actualizar_analisis()
