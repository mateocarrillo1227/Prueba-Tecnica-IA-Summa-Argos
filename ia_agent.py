import pandas as pd
import re

class SummaChatbot:
    def __init__(self, file_path):
        try:
            self.df = pd.read_excel(file_path)
            self.df.columns = ['Documento', 'Valor', 'Fecha']
            self.df['Documento'] = self.df['Documento'].astype(str)
            self.df['Valor'] = pd.to_numeric(self.df['Valor'], errors='coerce')
            self.df['Fecha'] = pd.to_datetime(self.df['Fecha'], errors='coerce')
            self.df['Fecha_Formateada'] = self.df['Fecha'].dt.strftime('%d/%m/%Y')
            
            print(f"✅ Base de datos cargada exitosamente.")
        except Exception as e:
            print(f"❌ Error al cargar los datos: {e}")

    def flujo_consulta(self):
        doc_input = input("\n👉 Ingrese el número de documento para consultar: ").strip()
        
        if doc_input.lower() in ['salir', 'atras']: return

        # Buscamos el registro
        resultado = self.df[self.df['Documento'] == doc_input]
        
        if not resultado.empty:
            # Sacamos el primer resultado
            fecha_str = resultado.iloc[0]['Fecha_Formateada']
            valor = resultado.iloc[0]['Valor']
            
            print(f"\n✅ Información encontrada:")
            print(f"   >>> Documento: {doc_input}")
            print(f"   >>> Fecha de Corte: {fecha_str}")
            print(f"   >>> Valor Cesantías: ${valor:,.2f}")
        else:
            print(f"\n❌ Error: El documento {doc_input} no se encuentra en el sistema.")

    def iniciar(self):
        print("\n" + "="*50)
        print("   ASISTENTE DE CONSULTA EXPRÉS - EMPLEADOS SUMMA - ARGOS")
        print("="*50)
        
        while True:
            print("\nOpciones:")
            print("1. Consultar por Documento")
            print("2. Salir")
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == '2' or opcion.lower() == 'salir':
                print("\nAgent: ¡Gracias por usar nuestro servicio, Hasta la próxima.")
                break
            elif opcion == '1':
                self.flujo_consulta()
            else:
                print("⚠️ Opción no válida. Por favor, marque 1 o 2.")

if __name__ == "__main__":
    bot = SummaChatbot('cesancias_causadas.xlsx')
    bot.iniciar()