import pdfplumber # Package pour extraire des textes et des tables
import pandas as pd #Permet de traiter les librairies
import os

def transform(input, output, name, mdp=''):
    with pdfplumber.open(input, password=mdp) as pdf:
        for page in pdf.pages[0:]:
            table = page.extract_table() # Retourne une liste des listes, où une liste représente une ligne de la table
            
            # Colonnes de départ
            if page == pdf.pages[0]:
                columns = table[0]
                df = pd.DataFrame(table[1:], columns=columns)
            else:
                df = pd.concat([df, pd.DataFrame(table[1:], columns = columns)])

        df.to_excel(f"{output}/{name}.xlsx", index=False)
        os.system(f"start EXCEL.EXE {output}{name}.xlsx")