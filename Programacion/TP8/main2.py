import pandas as pd

class CopaAmerica:
    def __init__(self):
        self.equipos = pd.DataFrame(columns=[
            'Equipo', 'Puntos', 'PartidosJugados', 'Victorias', 'Empates', 'Derrotas', 
            'GolesAFavor', 'GolesEnContra', 'DiferenciaDeGoles'])
        self.partidos = pd.DataFrame()

    def cargar_fixture(self, archivo_fixture):
        self.partidos = pd.read_csv(archivo_fixture, parse_dates=['Date'], dayfirst=True)
        equipos_local = self.partidos['Home Team'].unique()
        equipos_visitante = self.partidos['Away Team'].unique()
        equipos = set(equipos_local).union(set(equipos_visitante))
        self.equipos = pd.DataFrame(equipos, columns=['Equipo'])
        self.equipos['Puntos'] = 0
        self.equipos['PartidosJugados'] = 0
        self.equipos['Victorias'] = 0
        self.equipos['Empates'] = 0
        self.equipos['Derrotas'] = 0
        self.equipos['GolesAFavor'] = 0
        self.equipos['GolesEnContra'] = 0
        self.equipos['DiferenciaDeGoles'] = 0

    def actualizar_resultados(self, archivo_resultados):
        resultados = pd.read_csv(archivo_resultados)
        for _, row in resultados.iterrows():
            numero_partido = row['Match Number']
            goles_local = row['Home Team Goals']
            goles_visitante = row['Away Team Goals']
            self._actualizar_partido(numero_partido, goles_local, goles_visitante)

    def _actualizar_partido(self, numero_partido, goles_local, goles_visitante):
        partido = self.partidos.loc[self.partidos['Match Number'] == numero_partido].iloc[0]
        equipo_local = partido['Home Team']
        equipo_visitante = partido['Away Team']

        self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'PartidosJugados'] += 1
        self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'PartidosJugados'] += 1

        self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'GolesAFavor'] += goles_local
        self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'GolesEnContra'] += goles_visitante
        self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'GolesAFavor'] += goles_visitante
        self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'GolesEnContra'] += goles_local

        if goles_local > goles_visitante:
            self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'Victorias'] += 1
            self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'Puntos'] += 3
            self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'Derrotas'] += 1
        elif goles_local < goles_visitante:
            self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'Victorias'] += 1
            self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'Puntos'] += 3
            self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'Derrotas'] += 1
        else:
            self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'Empates'] += 1
            self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'Empates'] += 1
            self.equipos.loc[self.equipos['Equipo'] == equipo_local, 'Puntos'] += 1
            self.equipos.loc[self.equipos['Equipo'] == equipo_visitante, 'Puntos'] += 1

        self.equipos['DiferenciaDeGoles'] = self.equipos['GolesAFavor'] - self.equipos['GolesEnContra']

    def calcular_posiciones(self):
        self.equipos = self.equipos.sort_values(by=['Puntos', 'DiferenciaDeGoles', 'GolesAFavor'], ascending=[False, False, False])

    def generar_informe(self, archivo_salida):
        self.calcular_posiciones()
        self.equipos.to_csv(archivo_salida, index=False)

# Ejemplo de uso
copa = CopaAmerica()
copa.cargar_fixture('copa-america-2024-UTC.csv')
copa.actualizar_resultados('resultados.csv')
copa.generar_informe('posiciones_finales.csv')
