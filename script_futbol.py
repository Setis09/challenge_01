# -*- coding: utf-8 -*-

import pandas as pd #importing pandas
resultados_cmff = pd.read_csv("https://raw.githubusercontent.com/edvaicode/challenge_01/main/resultados_cmff.csv") # Creating DataFrame
resultados_cmff # viewing DataFrame

############################################

resultados_cmff_grouper=(resultados_cmff[["anio","equipo","goles"]].groupby(["anio","equipo"]) # Reducing columns and grouping by anio and equipo
.agg({"goles":"sum"}) # adding by group columns
.reset_index() # Eliminating grouping
)

############################################

final_df= pd.DataFrame(columns=["anio","equipo","goles"]) # Creating an empty DataFrame, with just three columns

for i in pd.unique(resultados_cmff_grouper["anio"]): # Iterating over each unique value in anio
  df_anio= resultados_cmff_grouper.query("anio == %i"%i).sort_values("goles",ascending=False) # Creating a DataFrame for each year and sorting it.
  a= df_anio.loc[df_anio.goles == df_anio.goles.max()]  # Selecting the row (containing anio, equipo and goles) with goles max value by year
  
  final_df= final_df.append(a) # Adding the max value to the empty DataFrame created. Remember df.append doesn't occurs in place. 

############################################

final_df # Here is the data frame with the max number of goles, per year.
