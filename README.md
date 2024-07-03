# TRABAJO INTEGRADOR - SEMINARIO DE LENGUAJES: PYTHON

## PyTrivia

### Este trabajo consiste en un juego de preguntas en el cual el usuario contestara para competir con otros usuarios en un ranking.

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

### Etapa 2 - Parte 2

En la segunda parte del trabajo integrador completamos las 6 paginas del proyecto, las cuales contienen la siguiente informacion:

1. Inicio: En esta pagina encontraras informacion exclusivamente de juego, asi como tambien instrucciones basicas.

2. Conociendo nuestros datos: En el desarrollo de esta pagina utilizamos pandas, que es una libreria muy eficiente en manejo y procesamiento de datos, para sacar informacion de los datasets y crear graficos.

3. Juego: Aqui podras empezar a jugar. Posteriormente estaran las especificaciones de como es el desarrollo del juego.

4. Formulario: En esta pagina encotraras el sistema de registro de usuario, el cual se almacenara en un archivo ".json" que va a contener la informacion de todos los usuarios.

5. Ranking: A esta pagina se podra acceder de dos maneras diferentes. En un principio desde el menu, donde encontraras la informacion de los primeros 15 usuarios con mejor puntaje. Por otro lado podras acceder gracias a la redireccion de la pagina de juego donde, ademas de la tabla recien mencionada encontraras los detalles de tu juego.

6. Estadisticas: En esta pagina se encontraran mas graficos y detalles de las respuestas historicamente dadas por todos los usuarios.

## Instrucciones para Jugar: 

Para jugar a PyTrivia, sigue estos pasos:
1. Elige un usuario o regístrate si es tu primera vez.
2. Dirigite a el apartado Juego
3. En caso de que tu usuario se encuentre repetido, selecciona tu email tambien.     
4. Selecciona una temática y una dificultad.
5. Responde las preguntas que se te presenten.

### Explicación del parámetro dificultad:

PyTrivia ofrece tres niveles de dificultad:

- Fácil: Se te brindan tres opciones de respuesta y una pista sobre la respuesta correcta.
- Media: Se te indica la cantidad de palabras que tiene la respuesta correcta.
- Alta: No se brindan ayudas, debes responder solo con tus conocimientos.

Elige el nivel que mejor se adapte a ti y desafía tus habilidades.