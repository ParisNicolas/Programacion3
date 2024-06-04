import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('copa-america-2024-UTC.csv')

def createOutput(results_df, teams_df):
    planilla_df = pd.DataFrame(columns=["Grupo","Equipo","Puntos","PartidosJugados","Victorias","Empates","Derrotas","GolesAFavor","GolesEnContra","DiferenciaDeGoles"])
    
    teams_df["Grupo", "Equipo"]
    for index, row in results_df.iterrows():
        teams_df
    planilla_df["Grupo"] = teams_df[]
    pass


#Menu interactivo
while True:
    print("1) Rellenar plantilla de goles")
    print("2) Previsualizar")
    print("3) Generar informe y salir")
    print("4) Salir")

    option = input("Ingresa una opcion: ")

    if option == "1":
        if input("Relleno de la BD (M/A): ") == "M":
            result_columns = ["Match Number","Home Team Goals","Away Team Goals"]
            results_list = []
            print("\nMatch,Team1_Goals,Team2_Goals (Ex: 1,2,1)")
            while True:
                data = input().split(",")
                if not data: break
                results_list.append(data)
        else:
            results_list = np.random.randint(0, 6, size=(5, 3))
        
        results_df = pd.dataframe(results_list, columns=result_columns)
    
    
    elif option == "2":
        print(results_df)
    elif option == "3":
        pass
    else:
        break