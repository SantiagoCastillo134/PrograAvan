import pandas as pd
import os
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
from datetime import datetime

class FinanceBackend:
    def __init__(self, data_file="datos_gastos.csv"):
        self.data_file = data_file
        self.columns = ["ID", "Tipo", "Fecha", "Categoria", "Monto"]
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            self.df = pd.read_csv(self.data_file)
            self.df['Fecha'] = pd.to_datetime(self.df['Fecha'])
        else:
            self.df = pd.DataFrame(columns=self.columns)
            self.save_data()

    def save_data(self):
        self.df.to_csv(self.data_file, index=False)

    def add_record(self, tipo, fecha, categoria, monto):
        new_id = self.df["ID"].max() + 1 if not self.df.empty else 1
        # Asegurar formato de fecha correcto
        fecha_dt = pd.to_datetime(fecha)
        new_row = {
            "ID": new_id,
            "Tipo": tipo,
            "Fecha": fecha_dt,
            "Categoria": categoria,
            "Monto": float(monto)
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.save_data()

    def get_records(self, tipo=None, categoria=None, fecha_inicio=None, fecha_fin=None, monto_min=None, monto_max=None):
        filtered = self.df.copy()
        
        if tipo and tipo != "Todos":
            filtered = filtered[filtered["Tipo"] == tipo]
            
        if categoria and categoria != "Todas":
            filtered = filtered[filtered["Categoria"].str.contains(categoria, case=False, na=False)]
        
        if fecha_inicio:
            try:
                dt_inicio = pd.to_datetime(fecha_inicio)
                filtered = filtered[filtered["Fecha"] >= dt_inicio]
            except:
                pass
                
        if fecha_fin:
            try:
                dt_fin = pd.to_datetime(fecha_fin)
                filtered = filtered[filtered["Fecha"] <= dt_fin]
            except:
                pass

        if monto_min is not None:
            filtered = filtered[filtered["Monto"] >= float(monto_min)]
        
        if monto_max is not None:
            filtered = filtered[filtered["Monto"] <= float(monto_max)]

        # Devolver ordenado por fecha
        return filtered.sort_values(by="Fecha", ascending=False)

    def get_summary(self):
        ingresos = self.df[self.df["Tipo"] == "Ingreso"]["Monto"].sum()
        gastos = self.df[self.df["Tipo"] == "Gasto"]["Monto"].sum()
        return ingresos, gastos

    def get_expenses_by_category(self):
        gastos_df = self.df[self.df["Tipo"] == "Gasto"]
        if gastos_df.empty:
            return pd.Series(dtype=float)
        return gastos_df.groupby("Categoria")["Monto"].sum()

    def get_alerts(self, threshold=1000):
        alerts = []
        gastos_por_cat = self.get_expenses_by_category()
        for cat, amount in gastos_por_cat.items():
            if amount > threshold:
                alerts.append(f"¡Alerta! Los gastos en '{cat}' (${amount:.2f}) superan el umbral de ${threshold:.2f}.")
        return alerts

    def get_recommendations(self):
        gastos_por_cat = self.get_expenses_by_category()
        if gastos_por_cat.empty:
            return "No hay suficientes datos para generar recomendaciones."
            
        max_cat = gastos_por_cat.idxmax()
        max_amount = gastos_por_cat.max()
        ingresos, gastos = self.get_summary()
        
        recs = [f"Tu mayor área de gasto es '{max_cat}' con ${max_amount:.2f}."]
        
        if gastos > ingresos:
            recs.append("¡Atención! Tus gastos superan tus ingresos. Necesitas recortar presupuestos urgentemente.")
        else:
            ahorro = ingresos - gastos
            recs.append(f"Actualmente ahorras ${ahorro:.2f}. Buen trabajo.")
            
        recs.append(f"Sugerencia: Intenta reducir tus gastos en '{max_cat}' buscando alternativas más económicas o limitando el consumo.")
        return "\n".join(recs)

    def get_distribution_chart(self):
        gastos_por_cat = self.get_expenses_by_category()
        fig, ax = plt.subplots(figsize=(5, 4))
        
        if gastos_por_cat.empty:
            ax.text(0.5, 0.5, 'No hay datos de gastos', ha='center', va='center')
            ax.axis('off')
        else:
            ax.pie(gastos_por_cat, labels=gastos_por_cat.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title("Distribución de Gastos")
            
        return fig

    def get_trend_chart(self):
        gastos_df = self.df[self.df["Tipo"] == "Gasto"].copy()
        fig, ax = plt.subplots(figsize=(6, 4))
        
        if gastos_df.empty:
            ax.text(0.5, 0.5, 'No hay datos de gastos', ha='center', va='center')
            ax.axis('off')
        else:
            # Agrupar por mes y año
            gastos_df['Mes_Año'] = gastos_df['Fecha'].dt.to_period('M')
            tendencia = gastos_df.groupby('Mes_Año')["Monto"].sum()
            
            # Convertir el índice Period a string para graficar fácilmente
            tendencia.index = tendencia.index.astype(str)
            
            ax.plot(tendencia.index, tendencia.values, marker='o', linestyle='-', color='r')
            ax.set_title("Tendencia de Gastos a lo Largo del Tiempo")
            ax.set_xlabel("Mes")
            ax.set_ylabel("Monto ($)")
            ax.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            fig.tight_layout()
            
        return fig
