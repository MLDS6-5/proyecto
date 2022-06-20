# Análisis de accidentes cardiovasculares

Programa de línea de comandos que permite entrenar un modelo de Regresión logística o una máquina de soporte vectorial para realizar la predicción de accidentes cardiovasculares en pacientes con enfermedades del corazón.

## Requisitos

* Python 3.9
* Poetry

## Instalación

```sh
git clone https://github.com/MLDS6-5/proyecto.git
cd proyecto
poetry install
```

## Entrenamiento

Ejecutar:

```sh
stroke-train --help
```

Para entrenar un modelo de regresión logística usar:

```sh
stroke-train data/stroke-data.csv logistic --help
```

Para entrenar una máquina de soporte vectorial usar:

```sh
stroke-train data/stroke-data.csv svm --help
```

## Predicción

Ejecutar:

```sh
stroke-predict --help
```

Predecir desde un archivo:

```sh
stroke-predict file --help
```

Predecir desde la línea de comandos

```sh
stroke-predict line --help
```