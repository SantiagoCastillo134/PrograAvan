# Aplicación de Monitoreo de Gastos para Familias

## 1. Descripción del Proyecto: Propósito, Objetivo Principal y Contexto

**Propósito:** Proporcionar una herramienta accesible, intuitiva y robusta para que individuos y familias puedan llevar un control financiero riguroso de sus ingresos y gastos diarios, sin depender de hojas de cálculo propensas a errores.  
**Objetivo Principal:** Ayudar a los usuarios a visualizar el flujo de su dinero, detectar fugas de capital en tiempo real y fomentar una cultura de ahorro mediante recomendaciones automáticas y reportes sobre sus hábitos de consumo.  
**Contexto:** Llevar las finanzas en papel o Excel suele resultar tedioso. Esta aplicación centraliza todos estos procesos en una interfaz gráfica (GUI) construida en Python que automatiza cálculos, filtra información al instante con tecnología de Pandas y crea análisis visuales integrados en la misma ventana, eliminando barreras técnicas.

---

## 2. Funcionalidades Principales

El sistema ofrece una experiencia de usuario dividida en cuatro pestañas principales:

1. **Pestaña de Registro (Ingreso de Datos):**  
   - Permite agregar transacciones como "Gasto" o "Ingreso".
   - Al seleccionar el tipo de transacción, las opciones del menú de "Categorías" se actualizan automáticamente para mostrar únicamente opciones relevantes (ej. Alimentos, Transporte, o Salario, Rentas).
   - Validaciones internas aseguran que los montos sean números válidos antes de guardarlos de forma permanente en un archivo CSV local.

2. **Pestaña de Búsqueda y Filtrado:**  
   - Muestra el historial completo de transacciones en una tabla (Treeview) fácil de leer.
   - Permite aplicar filtros dinámicos con simples menús desplegables. El usuario puede filtrar por "Tipo" (Solo Gastos, Solo Ingresos, o Todos) y "Categoría" (ej. solo ver los gastos de "Alimentos y Despensa").

3. **Pestaña de Reportes y Recomendaciones:**  
   - Genera un **balance general** calculando el total de ingresos, gastos y el dinero neto restante (ahorro).
   - El sistema emite **alertas proactivas** si alguna categoría de gasto excede un umbral límite predefinido (ej. gastos mayores a $1,000 en una sola categoría).
   - El motor de recomendaciones detecta matemáticamente la categoría donde más dinero se está gastando y emite consejos personalizados para sugerir recortes de presupuesto específicos.

4. **Pestaña de Análisis Visual:**  
   - Despliega gráficos que se actualizan automáticamente con los datos actuales:
   - **Gráfico Circular (Pastel):** Muestra de forma porcentual la distribución del gasto total entre las distintas categorías.
   - **Gráfico de Tendencias:** Un gráfico de líneas que traza la evolución de los gastos a lo largo del tiempo agrupados por meses.

## 3. Mercado Objetivo / Público al que se Dirige

- **Familias y Hogares:** Personas responsables del presupuesto familiar que buscan un método sencillo para asegurarse de que los ingresos cubran todos los gastos mensuales.
- **Jóvenes Profesionales e Independientes:** Que desean evitar gastos innecesarios (gastos hormiga) y requieren una herramienta de escritorio gratuita y privada para controlar su propio dinero.
- **Usuarios no técnicos:** Aquellos que desean algo más estructurado que una libreta, pero mucho más fácil de usar y directo que configuraciones complejas en Excel o software empresarial.

---

## 4. Ventajas Competitivas

- **Privacidad Local y Segura:** A diferencia de apps móviles que alojan tu información financiera en sus servidores, este proyecto guarda todo el historial en un archivo local `datos_gastos.csv` en tu propia computadora.
- **Tecnología Analítica Integrada:** Gracias a la integración de `pandas` y `matplotlib` dentro de `tkinter`, el usuario obtiene la capacidad analítica de la ciencia de datos en una aplicación de escritorio que corre en milisegundos.
- **Sin Curva de Aprendizaje:** Interfaz enfocada en la simplicidad. Al abrir la app, no se requiere registrar correos, crear contraseñas o configurar bases de datos. Todo funciona al primer clic.
- **Bajo Consumo de Recursos:** Al estar desarrollada en Python con Tkinter, la aplicación utiliza una cantidad mínima de memoria RAM y no satura el equipo.

---

## 5. Arquitectura del Código

El software ha sido desarrollado con un enfoque modular, separando las responsabilidades de programación para mantener el código limpio y escalable:

- `backend.py`: Maneja el modelo de datos. Utiliza la librería Pandas para el procesamiento de transacciones, filtrado avanzado, algoritmos de recomendación y generación de Figuras de Matplotlib.
- `frontend.py`: Maneja la vista. Utiliza Tkinter (ttk) para dibujar las pestañas, botones y la interfaz en general. Invoca funciones del backend en respuesta a las acciones del usuario.
- `main.py`: Punto de entrada del programa. Inicializa tanto el backend como el frontend, orquestando la comunicación inicial.
