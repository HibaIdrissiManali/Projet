import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



folder = './transactions-ser'


# Fonction qui lit et fusionne les fichiers csv dans le dossier "folder"
def read_and_merge(folder) :
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    df = pd.read_csv(os.path.join(folder, csv_files[0]),delimiter=';')
    common_columns = list(df.columns)

    for file in csv_files[1:]:
        df_temp = pd.read_csv(os.path.join(folder, file), delimiter=';')
        df_temp = df_temp[common_columns]
        df = pd.concat([df, df_temp], ignore_index=False)
    return df


# Fonction qui nettoie le dataFrame, la fonction est plus détaillée dans le notebook VisualisionEtAnalyse
def data_cleaning(df) :
    df = df.replace({'None': None, 'nan': float('nan')})
    df.dropna(subset = ["valeur_fonciere"], inplace = True)
    df.dropna(subset = ["surface_reelle_bati"], inplace = True)
    df['surface_terrain'] = df['surface_terrain'].fillna(0)

    df = df.loc[(df['type_local'] == 'Maison') | (df['type_local'] == 'Appartement')]
    df['code_type_local'] = pd.to_numeric(df['code_type_local'], errors='coerce', downcast='integer')

    df = df.drop(df.loc[df["nombre_lots"]> 1].index)
    df.groupby("nombre_lots")[['valeur_fonciere']].count().sort_values("nombre_lots")
    df = df.drop(df.loc[df["lot1_surface_carrez"] > df["surface_reelle_bati"]].index)

    df['surface'] = np.where(df["code_type_local"] == 1, df["surface_reelle_bati"],df["lot1_surface_carrez"])
    df.dropna(subset = ["surface"], inplace = True)

    df = df.dropna(thresh=len(df) * 0.10, axis=1)

    df = df.drop(['id_mutation','nature_mutation' , 'adresse_numero','adresse_nom_voie' ,'adresse_code_voie','code_postal', 'nom_commune','code_departement', 'id_parcelle', 'date_mutation','numero_disposition','code_nature_culture','nature_culture','code_commune'], axis=1)

    # OUTLIERS :

    largest_st = df['surface_terrain'].nlargest(len(df[df['surface_terrain'] > 1000]))
    df = df.drop(largest_st.index)
    largest_vf = df['valeur_fonciere'].nlargest(len(df[df['valeur_fonciere'] > 300000]))
    df = df.drop(largest_vf.index)
    largest_vf = df['surface'].nlargest(len(df[df['surface'] > 150]))
    df = df.drop(largest_vf.index)
    largest_vf = df['surface_reelle_bati'].nlargest(len(df[df['surface_reelle_bati'] > 150]))
    df = df.drop(largest_vf.index) 

    return df


# Fonction qui entraine le modele de la régression linéaire
def train(df) :
    df_train = df.sample(n=3000, random_state=7,replace=True)

    X = pd.DataFrame(np.c_[df_train["surface"],df_train['code_type_local'],df_train['surface_terrain'],df_train["nombre_pieces_principales"]], columns= ["surface",'code_type_local',"surface_terrain","nombre_pieces_principales"])
    y = df_train["valeur_fonciere"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)
    X_train = X_train.values

    lmodellineaire = LinearRegression()
    lmodellineaire.fit(X_train, y_train)

    y_pred = lmodellineaire.predict(X_test)

    return lmodellineaire

# Fonction qui retourne les coefficients de la régression liéaire
def get_coef() :
    df = read_and_merge(folder)
    df = data_cleaning(df)
    lmodellineaire = train(df)
    coefficient = lmodellineaire.coef_
    return np.append(coefficient ,lmodellineaire.intercept_)

# Fonction qui retourne l'estimation des prix, les paramètres sont la sufrace, le type, la surface du terrain et le nombre de pièces
def predict(surface, code_type, surface_terrain, np_piece) :
    df = read_and_merge(folder)
    df = data_cleaning(df)
    lmodellineaire = train(df)
    df_estim = [[surface, code_type, surface_terrain, np_piece]]
    estimation = round(lmodellineaire.predict(df_estim)[0],2)
    return estimation

