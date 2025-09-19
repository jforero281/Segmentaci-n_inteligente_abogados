import pandas as pd

class ETLProcesador:
    def __init__(self, columnas_a_eliminar):
        self.columnas_a_eliminar = columnas_a_eliminar + [
            'MOTIVOS2', 'VALOR PRETENSIONES (EN $)', 'CAUSA'
        ]

    def filtrar_por_anio(self, df, anio_min=2000):
        if not pd.api.types.is_datetime64_any_dtype(df['PRESENTACIÓN DEMANDA']):
            df['PRESENTACIÓN DEMANDA'] = pd.to_datetime(df['PRESENTACIÓN DEMANDA'], errors='coerce')
        df_filtrado = df[(df['AÑO DEMANDA'] >= anio_min) & (df['PRESENTACIÓN DEMANDA'].dt.year >= anio_min)]
        return df_filtrado

    def limpiar_minusculas(self, df):
        # Convierte todos los valores string del DataFrame a minúsculas
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.lower()
        return df

    def eliminar_columnas(self, df):
        return df.drop(columns=self.columnas_a_eliminar, errors='ignore')

    def imputar_nulos_moda(self, df):
        # Imputa nulos con la moda para cada columna
        for col in df.columns:
            if df[col].isnull().any():
                moda = df[col].mode(dropna=True)
                if not moda.empty:
                    df[col] = df[col].fillna(moda[0])
        return df

    def limpiar_tipo_proceso(self, df):
        # Homologación de valores en TIPO DE PROCESO (ya en minúsculas)
        reemplazos = {
            'ordinario': 'Ordinario', 'ordinario ': 'Ordinario', 'odinario': 'Ordinario',
            '0rdinario': 'Ordinario', 'ordinario u.i.': 'Ordinario',
            'especial': 'Especial', 'especial ': 'Especial',
            'ejecutivo': 'Ejecutivo', 'ejecitivo': 'Ejecutivo',
            'unica': 'Unico', 'única instancia': 'Unico', 'fuero ': 'Unico'
        }
        df['TIPO DE PROCESO'] = df['TIPO DE PROCESO'].replace(reemplazos)
        return df
    
    
    def homologar_red(self, df):
        # Homologación de valores en el campo RED
        reemplazos_bancolombia = {
            'colombia ': 'Bancolombia', 'bancolombia ': 'Bancolombia', 'leasing': 'Bancolombia', 'colombia': 'Bancolombia'
        }
        reemplazos_bic = {
            'bic': 'BIC', 'bic': 'BIC', 'bic': 'BIC'
        }
        reemplazos_conavi = {
            'conavi': 'Conavi'
        }
        reemplazos_otros = {
            'sin establecer': 'Otros', 'corfinsura': 'Otros', 'ninguno': 'Otros',
            'banco industrial colombia': 'Otros', 'banco industrial colombiano': 'Otros'
        }
        # Convertir a minúsculas para asegurar la homologación
        df['RED'] = df['RED'].str.lower()
        df['RED'] = df['RED'].replace(reemplazos_bancolombia)
        df['RED'] = df['RED'].replace(reemplazos_bic)
        df['RED'] = df['RED'].replace(reemplazos_conavi)
        df['RED'] = df['RED'].replace(reemplazos_otros)
        # Capitalizar el resultado final
        df['RED'] = df['RED'].str.capitalize()
        return df    

        def homologar_tipo_relacion(self, df):
        # Homologación de valores en el campo TIPO RELACIÓN
        reemplazos_jubilado = {
            'extrabajador': 'Jubilado', 'jubilado ': 'Jubilado'
        }
        reemplazos_empleado = {
            'trabajador': 'Empleado', 'trabajador': 'Empleado'
        }
        reemplazos_otros = {
            'ninguna': 'Otros', 'sobreviviente': 'Otros', 'gestor': 'Otros',
            'corretaje': 'Otros', 'conavi': 'Otros', 'ninguna': 'Otros'
        }
        # Convertir a minúsculas para asegurar la homologación
        df['TIPO RELACIÓN'] = df['TIPO RELACIÓN'].str.lower()
        df['TIPO RELACIÓN'] = df['TIPO RELACIÓN'].replace(reemplazos_jubilado)
        df['TIPO RELACIÓN'] = df['TIPO RELACIÓN'].replace(reemplazos_empleado)
        df['TIPO RELACIÓN'] = df['TIPO RELACIÓN'].replace(reemplazos_otros)
        # Capitalizar el resultado final
        df['TIPO RELACIÓN'] = df['TIPO RELACIÓN'].str.capitalize()
        return df  


   def limpiar_pretension(self, df):
        # Limpieza y homologación del campo PRETENSIÓN
        df['PRETENSIÓN'] = df['PRETENSIÓN'].str.lower()
        patrones = {
            "reintegro": "reintegro",
            "jubilacion": "jubilacion",
            "beneficios": "beneficios",
            "fuero sindical": "fuero sindical",
            "salario": "salario",
            "prestaciones sociales": "prestaciones sociales",
            "indemnizacion": "indemnización",
            "indemnización": "indemnización",
            "contrato": "contrato",
            "pensión": "pensión"
        }
        for patron, valor in patrones.items():
            df.loc[df['PRETENSIÓN'].str.contains(patron, case=False, na=False), 'PRETENSIÓN'] = valor

        # Organizar las clases principales y agrupar el resto en 'otros'
        clases_principales = ['indemnización', 'reintegro', 'jubilacion', 'fuero sindical', 'salario']
        df['PRETENSIÓN'] = df['PRETENSIÓN'].apply(lambda x: x if x in clases_principales else 'otros')
        return df

    def limpiar_clase_posibilidad_perdida(self, df):
        # Homologar el campo CLASE (posibilidad de pérdida) a solo 3 clases
        df['CLASE (posibilidad de pérdida)'] = df['CLASE (posibilidad de pérdida)'].replace({
            'Problable': 'probable',
            'el ersultado es muy inciertoy  por tanto la probailidad de fallo adverso es latente': 'probable'
        })
        # Mantener solo probable, eventual y retoma, el resto agrupar en 'otros'
        clases_validas = ['probable', 'eventual', 'retoma']
        df['CLASE (posibilidad de pérdida)'] = df['CLASE (posibilidad de pérdida)'].apply(
            lambda x: x if x in clases_validas else 'otros'
        )
        return df
    
    

    def limpiar_clase_posibilidad_perdida(self, df):
        # Homologar el campo CLASE (posibilidad de pérdida) a solo 3 clases
        df['CLASE (posibilidad de pérdida)'] = df['CLASE (posibilidad de pérdida)'].replace({
            'Problable': 'probable',
            'el ersultado es muy inciertoy  por tanto la probailidad de fallo adverso es latente': 'probable'
        })
        clases_validas = ['probable', 'eventual', 'retoma']
        df['CLASE (posibilidad de pérdida)'] = df['CLASE (posibilidad de pérdida)'].apply(
            lambda x: x if x in clases_validas else 'otros'
        )
        # Imputar nulos con la moda
        df['CLASE (posibilidad de pérdida)'] = df['CLASE (posibilidad de pérdida)'].fillna(
            df['CLASE (posibilidad de pérdida)'].mode()[0]
        )
        return df

    def limpiar_estado_actual(self, df):
        # Limpieza y homologación del campo ESTADO ACTUAL
        patrones = [
            "conciliado", "favorable", "desfavorable", "contestada", "pendiente", "neutro", "terminado",
            "fallo 2a instancia", "segunda instancia", "radica contestacion", "liquidación",
            "apelación demandante", "resuelto", "fallo 1era instancia", "primera instancia"
        ]
        df['ESTADO ACTUAL'] = df['ESTADO ACTUAL'].str.lower()
        for patron in patrones:
            df.loc[df['ESTADO ACTUAL'].str.contains(patron, case=False, na=False), 'ESTADO ACTUAL'] = patron
        # Agrupar en 'otros' si no está en clases principales
        df['ESTADO ACTUAL'] = df['ESTADO ACTUAL'].apply(
            lambda x: x if x in patrones else 'otros'
        )
        # Imputar nulos con la moda
        df['ESTADO ACTUAL'] = df['ESTADO ACTUAL'].fillna(
            df['ESTADO ACTUAL'].mode()[0]
        )
        return df

    



def cargar_base_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    return df

def proceso_etl(df, columnas_a_eliminar, anio_min=2000):
    etl = ETLProcesador(columnas_a_eliminar)
    df = etl.filtrar_por_anio(df, anio_min)
    df = etl.limpiar_minusculas(df)
    df = etl.eliminar_columnas(df)
    df = etl.imputar_nulos_moda(df)
    df = etl.limpiar_tipo_proceso(df)
    df = etl.homologar_red(df)
    df = etl.homologar_tipo_relacion(df)
    df = etl.limpiar_pretension(df)
    df = etl.limpiar_clase_posibilidad_perdida(df)
    df = etl.limpiar_estado_actual(df)
    
    return df

if __name__ == "__main__":
    columnas_a_eliminar = [
        'JGO.', 'RADICADO', 'RADICADO CONSULTA', 'MOTIVOS', 'PRIMERA INSTANCIA',
        'Fecha Fallo 1a. instancia', 'SEGUNDA INSTANCIA', 'Fecha Fallo 2a. instancia',
        'CASACIÓN', 'Fecha Casación', 'MONTO DE LA PROVISION (EN MILLONES) Años anteriores',
        'MONTO DE LA PROVISION (EN MILLONES) 2017', 'MONTO TOTAL DE LA PROVISIÓN',
        'FECHA ESTIMADA DE PAGO', 'EMPRESA APODERADO BANCO', '% PROVISIÓN Años anteriores',
        '% PROVISIÓN\n2015', 'TOTAL % PROVISIÓN', 'HONORARIOS', 'APODERADO ACTOR',
        'OBSERVACIONES', 'FOGAFIN', 'INSTANCIA', 'DESCRPICIÓN HECHOS','MOTIVOS2', 'VALOR PRETENSIONES (EN $)',
        'CAUSA'
    ]
    ruta_excel = "C:/Users/jdfr1/Segmentaci-n_inteligente_abogados/Base_Datos.xlsx"
    df_original = cargar_base_excel(ruta_excel)
    df_transformado = proceso_etl(df_original, columnas_a_eliminar, anio_min=2000)
    df_transformado.to_csv("base_transformada.csv", index=False)