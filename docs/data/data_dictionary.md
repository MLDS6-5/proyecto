# Diccionario de datos para la predicción de ACV (Accidente Cerebro Vascular)

La siguiente tabla describe las columnas que posee el conjunto de datos usados para la predicción de un ACV.

| columna | tipo | descripción |
| --- | --- | --- |
| id | INT | Identificador único
| gender | CAT | Género de la persona "Male", "Female" u "Other"
| age | INT | Género de la persona "Male", "Female" u "Other"
| hypertension | INT | 0 si la persona no tiene hipertensión. 1 si tiene hipertensión
| heart_disease | INT | 0 si la persona no tiene enfermedades en el corazón. 1 si tiene enfermedades en el corazón
| ever_married | CAT | "No" si la persona nunca ha estado casada. "Yes" si alguna vez estuvo casada.
| work_type | CAT | Tipo de trabajo. "children" si trabaja con niños. "Govt_job" si trabaja para el gobierno. "Never_worked" si nunca ha trabajado. "Self-employed" si trabaja de manera independiente.
| Residence_type | CAT | "Rural" si la persona vive en zona rural. "Urban" si vive en zona urbana.
| avg_glucose_level | FLOAT | Nivel de glucosa en la sangre
| bmi | FLOAT | Indice de masa corporal
| smoking_status | CAT | "formerly smoked" si la persona furma de manera cotidiana. "never smoked" si no ha fumado nunca. "smokes" si fuma ocasionalmente. "Unknown" significa que no se tiene información sobre la persona sobre si fuma o no.
| stroke | INT | 1 si la persona a tenido un ACV o 0 si no lo ha tenido.

Estos datos fueron obtenidos de Kaggle en el siguiente link: [https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)



