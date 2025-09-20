import pandas as pd
import numpy as np


class FeatureEngineer:
    def __init__(self, df, top_10_ciudades, clases_pretension, clases_principales):
        self.df = df.copy()
        self.top_10_ciudades = top_10_ciudades
        self.clases_pretension = clases_pretension
        self.clases_principales = clases_principales


        # Listas de clasificación para la decisión
        self.exito = [
            'favorable', 'contestada', 'liquidación',
            'terminado', 'conciliado', 'resuelto',
            'primera instancia', 'radica contestacion'
        ]
        self.fracaso = [
            'pendiente', 'fallo 2a instancia',
            'segunda instancia', 'neutro'
        ]

    def add_ciudad_principal(self):
        """Crea la feature ES_CIUDAD_PRINCIPAL"""
        self.df['ES_CIUDAD_PRINCIPAL'] = self.df['CIUDAD'].isin(self.top_10_ciudades).astype(int)

    def add_pretension_principal(self):
        """Crea la feature PRETENSION_PRINCIPAL"""
        self.df['PRETENSION_PRINCIPAL'] = self.df['PRETENSIÓN'].isin(self.clases_pretension).astype(int)

    def add_estado_actual_principal(self):
        """Crea la feature ESTADO_ACTUAL_PRINCIPAL"""
        self.df['ESTADO_ACTUAL_PRINCIPAL'] = self.df['ESTADO_ACTUAL'].isin(self.clases_principales).astype(int)

    def add_es_jubilado(self):
        """Crea la feature ES_JUBILADO"""
        self.df['ES_JUBILADO'] = (self.df['TIPO_RELACION'] == 'Jubilado').astype(int)

    def clasificar_decision(self, estado):
        """Clasifica una decisión en éxito, fracaso u otros"""
        if estado in self.exito:
            return 'exito'
        elif estado in self.fracaso:
            return 'fracaso'
        else:
            return 'otros'

    def add_decision(self):
        """Crea la feature DECISION"""
        self.df['DECISION'] = self.df['ESTADO_ACTUAL'].apply(self.clasificar_decision)

    def transform(self):
        """Aplica todas las transformaciones al DataFrame"""
        self.add_ciudad_principal()
        self.add_pretension_principal()
        self.add_estado_actual_principal()
        self.add_es_jubilado()
        self.add_decision()
        return self.df


