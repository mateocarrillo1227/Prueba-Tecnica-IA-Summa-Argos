# Solución Prueba Técnica IA - SUMMA (Grupo Argos) 🚀

Este repositorio contiene una solución integral que combina Machine Learning, Series de Tiempo y un Agente de IA con arquitectura MCP.

## 📂 Estructura del Proyecto
- `main.py`: API Backend desarrollada en FastAPI para la clasificación de gestores.
- `ia_agent.py`: Agente de IA para consulta de cesantías (Simulación MCP).
- `entrenamiento_modelo.ipynb`: Pipeline de entrenamiento y análisis de demanda.
- `resultados_predicciones.csv`: Predicciones finales para los nuevos registros.
- `teoria_mateo_carrillo.pdf`: Documentación técnica y diagramas.

## 🚀 Instrucciones de Ejecución

### 1. Instalación de dependencias
```bash
pip install -r requirements.txt

```
### 2. Iniciar la API de Clasificación

```bash
python main.py

```
Acceda a http://localhost:8005/docs para probar el endpoint /predict.

```
### 3. Ejecutar el Agente de Consulta

```bash
python ia_agent.py
