import random
import pandas as pd

forzaFile = 'FH5cars.xlsx'

df = pd.read_excel(forzaFile)

def procesar_respuestas(message) -> str:
    mensaje_nuevo = message.lower()

    if "escoje" in mensaje_nuevo:
        return "salio el " + str(random.randint(1,2)) + " wey" 

    if mensaje_nuevo == "forza":
        return str(df.iloc[random.randint(0,628)].values)
    
    return "escribe !help para ayudarte"

