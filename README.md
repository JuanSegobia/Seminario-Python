- Salmeron Emanuel - __Numero de ID 361056__
- Puddu Dante      - __Numero de ID 361837__
- Segobia Juan     - __Numero de ID 359459__
- Zorzoli Tomas    - __Numero de ID 361227__

# Pasos a seguir para iniciar

## Para empezar a trabajar con este projecto se debe clonar el repositorio de gitlab en donde quieras ejecutar el programa.

```
git clone https://gitlab.catedras.linti.unlp.edu.ar/python2024/code/grupo01.git

cd ./grupo01

```

## Ahora instalamos las librerias que utilizamos.
### - Usamos streamlit en la version 1.33.0
### - Usamos jupyter en la version 1.0.0
### - Usamos python en la version 3.11.7

```
pip install -r requirements.txt

```

# Este es el trabajo integrador en grupo de la materia Seminario de Lenguajes: Python
## El trabajo consta de 2 etapas.
### Etapa 1 - Parte 1

La primer etapa esta subdividida en 2 partes.
    
- Por un lado esta la parte de procesamiento de datos. Tenemos distintos datasets los cuales modificamos para luego ser recorridos, tomar datos y poder evaluar distintas condiciones.
- Luego hay un archivo Jupiter Notebook con 12 incisos que recorren los datasets modificados, y dependiendo la consigna se van mostrando en pantalla los datos que se solicitan.

### Para ejecutar el jupyter notebook con los informes debemos utilizar este comando:

Este comando lo que hace es abrir el archivo en el browser y quedaria listo para ser ejecutado.

```
jupyter-notebook.exe ./informes.ipynb

```
### Etapa 1 - Parte 2
- La segunda parte, involucra a streamlit, que es una libreria de Python de código abierto que se utiliza para crear aplicaciones web interactivas y personalizadas para el análisis de datos y la visualización de datos. 
- En esta etapa solo creamos la estructura de la web, y la funcionalidad del formulario, donde permitimos que se ingrese un usuario, y se guarda en un archivo JSON.

### Para ejecutar el streamlit hay que utilizar este comando:

Lo que hace este comando es abrir el archivo en el browser y quedaria listo para ser ejecutado.

```
streamlit run ./pyTrivia.py

```

