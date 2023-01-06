import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


folder = './transactions-ser'

def read_and_merge(folder) :
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    df = pd.read_csv(os.path.join(folder, csv_files[0]),delimiter=';')
    common_columns = list(df.columns)

    for file in csv_files[1:]:
        df_temp = pd.read_csv(os.path.join(folder, file), delimiter=';')
        # Keep only the columns that are present in the first CSV file
        df_temp = df_temp[common_columns]
        #df = df.append(df_temp, ignore_index=False)
        df = pd.concat([df, df_temp], ignore_index=False)
    return df


#df = read_and_merge(folder)
#print(df.info())

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

#df = data_cleaning(df)
#print(df)

def train(df) :
    df_train = df.sample(n=3000, random_state=7,replace=True)

    X = pd.DataFrame(np.c_[df_train["surface"],df_train['code_type_local'],df_train['surface_terrain'],df_train["nombre_pieces_principales"]], columns= ["surface",'code_type_local',"surface_terrain","nombre_pieces_principales"])
    y = df_train["valeur_fonciere"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)
    X_train = X_train.values

    lmodellineaire = LinearRegression()
    lmodellineaire.fit(X_train, y_train)

    y_pred = lmodellineaire.predict(X_test)
    #rmse = round(np.sqrt(mean_squared_error(y_test, y_pred)),2)
    #r2 = round(r2_score(y_test, y_pred),4)

    #print(f"L'erreur quadratique moyenne est {rmse}€")
    #print(f"Taux de bonne classification {np.ceil(r2*100)}%")

    return lmodellineaire

#lmodellineaire = train(df)

def predict(surface, code_type, surface_terrain, np_piece) :
    df = read_and_merge(folder)
    df = data_cleaning(df)
    lmodellineaire = train(df)
    df_estim = [[surface, code_type, surface_terrain, np_piece]]
    #print(df_estim)
    estimation = round(lmodellineaire.predict(df_estim)[0],2)
    #print (f'Estimation du bien : {estimation} euros.')
    coefficient = lmodellineaire.coef_
    print(coefficient)

    return estimation

def get_coef() :
    df = read_and_merge(folder)
    df = data_cleaning(df)
    lmodellineaire = train(df)
    #df_estim = [[surface, code_type, surface_terrain, np_piece]]
    coefficient = lmodellineaire.coef_
    return coefficient


#print(predict(70, 2, 150, 3))
#get_coef()
