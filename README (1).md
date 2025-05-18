
# 🔎 Predicción de Deserción de Clientes (Churn) en Telecomunicaciones

Este proyecto busca predecir qué clientes de una empresa de telecomunicaciones tienen mayor probabilidad de abandonar el servicio. Utilizamos técnicas de análisis exploratorio y modelos de machine learning para anticipar el churn y ayudar a la toma de decisiones comerciales.

---

## 📁 Contenido del proyecto

- `Pre_Entrega1.ipynb`: Análisis exploratorio, limpieza y codificación de variables
- `Entrega_final.ipynb`: Entrenamiento de modelos, selección de features, optimización y evaluación final
- `requirements.txt`: Librerías necesarias para ejecutar los notebooks
- Visualizaciones y gráficas clave de resultados (Matriz de confusión, Curva ROC)

---

## 🎯 Objetivo del Proyecto

Detectar de manera anticipada qué clientes podrían abandonar la empresa para que el área comercial pueda tomar acciones preventivas de fidelización.

---

## 🧠 Metodología

1. **Carga y análisis exploratorio del dataset**
   - 7043 registros de clientes
   - Variables sobre servicios, contratos, uso y facturación
2. **Tratamiento de datos**
   - Codificación de variables categóricas
   - Imputación de nulos en `TotalCharges`
   - Conversión de booleanos a numéricos
3. **Modelado**
   - Modelos entrenados: `Logistic Regression`, `Random Forest`, `XGBoost`
   - Evaluación con métricas: `Accuracy`, `Recall`, `F1`, `AUC`
4. **Optimización**
   - Selección de las 10 variables más relevantes (`feature importance`)
   - Búsqueda de hiperparámetros con `GridSearchCV` sobre `XGBoost`
   - Ajuste del desbalance de clases con `scale_pos_weight`
5. **Resultados**
   - Modelo final: `XGBoost` optimizado
   - Recall churn: **0.81**
   - AUC-ROC: **0.84**
   - F1 score: **0.63**

---

## 💡 Cómo usar este proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/LautaroPetersen/Proyecto_final_data2.git
cd Proyecto_final_data2
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # en Linux/Mac
venv\Scripts\activate     # en Windows
pip install -r requirements.txt
```

### 3. Ejecutar los notebooks

Podés abrir los notebooks con:

```bash
jupyter notebook
```

O subirlos a [Google Colab](https://colab.research.google.com) para ejecutarlos en la nube.

---

## 📊 Visualizaciones destacadas

- 🔹 Matriz de confusión
- 🔹 Curva ROC
- 🔹 Gráficos de distribución de churn según variables clave
- 🔹 Importancia de features según Random Forest

---

## 📘 Licencia

Este proyecto es de uso académico/personal. Podés usarlo como referencia o punto de partida para tus propios análisis.

---

## 🙌 Autor

**Lautaro Petersen**  
Proyecto Final | Ciencia de Datos II | 2025
