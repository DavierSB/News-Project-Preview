# News Project Preview

## Autores:

Davier Sánchez Bello

Maykol Luis Martínez

## Descripción del problema:
El problema se basa en construir un sistema para extraer información estructurada de noticias en línea. Permitir, a través de la dirección url proporcionada, conocer título, autores, fecha, resumen del contenido, entidades involucradas así como proporcionar 3 noticias similares. 

## Consideraciones tomadas a la hora de realizar la solución:
Se utilizó RealTimeData/bbc_news_alltime localizada en la librería datasets como base de datos para buscar noticias similares a las proporcionadas por el usuario.

Se optó por usar el modelo de indexación de semántica latente (diferente al modelo usado en el proyecto anterior) para construir un motor de búsqueda que proporcione las tres noticias similares. 

Los resúmenes contendrán las 5 oraciones más relevantes del texto.

## Explicación de como ejecutar el proyecto. Posibles entradas de parámetros:

Para correr el proyecto se usa el comando:
streamlit run src/code/web_app.py

No se introducen parámetros de entrada al correr el proyecto. Solo posteriormente se introducen las direcciones url de las noticias a analizar, algunas de las que se podrían utilizar son: 
https://www.granma.cu/cultura/2024-02-15/escribo-para-que-nazca-un-hombre-mejor-15-02-2024-23-02-42

https://www.washingtonpost.com/politics/2024/02/16/judge-engoron-ruling-trump-ny-civil-fraud-trial/

https://www.washingtonpost.com/politics/2024/02/15/nebraska-biden-electoral-college/

https://www.latimes.com/california/story/2024-02-17/how-forecasters-got-predictions-so-right-with-big-l-a-storm

## Explicación de la solución desarrollada:

Para la realización de este proyecto se dependió principalmente de la biblioteca newspaper de python, especializada en el scraping de artículos de periódico. 

En primer lugar se utiliza dicha biblioteca para descargar el artículo de noticias  través de su url. Luego se analiza el HTML del artículo para extraer el título, el autor, la fecha de publicación y el cuerpo del artículo, para esto se depende del método parse de newspaper que a su vez hace uso del código parsing de python, python-goose, el cual es conocido por su capacidad de extraer contenido de manera eficiente de páginas web. Este proceso implica identificar elementos HTML específicos que contienen la información deseada, es decir, el elemento title o en su ausencia h1 para encontrar el título; elementos time, o atributos datetime en etiquetas meta para la fecha, etc.

Newspaper intenta extraer el nombre del autor de varias etiquetas predefinidas en el código fuente de la página web, las cuales incluyen a author, byline, by1 y doc.creator en la sección de metadatos de la página web, además si el sitio web utiliza JSON-LD(JavaScript Object Noation for Linked Data) para almacenar información sobre el autor, se puede extraer el nombre de esta sección.  

Para elaborar el resumen utilizamos sumy.parsers.plaintext.Plaintextparser.from_string junto con sumy.nlp.tokenizers.tokenixer para tokenizar el cuerpo de la noticia, y prepararlo para ejecutar el algoritmo. Luego utilizamos el algoritmo LSA(Latent Semantic Analysis) para extraer las partes más importantes del documento, este enfoque se basa en la idea de que las palabras que aparecen en contextos similares tienden a tener significados similares(hipótesis distributiva) lo que permite identificar temas y conceptos subyacentes en el texto. Después de eliminar las palabras irrelevantes se utiliza la técnica de Descomposición en Valores Singulares(SVD) para reducir la dimensionalidad del  espacio de palabras manteniendo la información importante. SVD descompone la matriz de de término-documento en tres matrices: una matriz de términos, una matriz diagonal de valores singulares y una matriz de documentos, y luego reconstruir la matriz inicial manteniendo la estructura de similitud entre las columnas, que en este caso representan documentos. Luego se identifican los temas y relaciones semánticas entre las palabras y las oraciones mediante la asignación de vectores semánticos a estos permitiendo identificar los temas clave. Finalmente, comprobamos la similitud entre las oraciones y los temas clave identificados, y las oraciones con vectores semánticos más cercanos a los temas clave conformarán el resumen.

### SVD:
$$ M = ULV$$

Para la extracción y clasificación de entidades presentes en el texto se hace uso de spacy, esta utiliza  un diccionario de palabras y hace uso de una red neuronal convolucional para codificarlas en una matriz de oraciones a fin de tener en cuenta el contexto, para la clasificación también se utiliza una red neuronal de múltiples capas.

Para proporcionar noticias similares se ha utilizado un motor de búsqueda que hace uso del modelo indexación de semántica latente(LSI),como anteriormente se realizó un proyecto sobre motores de búsqueda, no se implementó ninguna forma de expansión de consulta o realimentación para mejorar el modelo sino que se usó en su forma básica. LSI es básicamente una aplicación de LSA que usamos anteriormente para confeccionar los resúmenes, luego de procesar los datos eliminando las palabras irrelevantes y realizando lematización para contruir el corpus, se utilizan las técnicas antes mencionadas para extraer 200 temas del corpus y confeccionar el modelo LSI, luego, una vez obtenido el texto de la noticia solicitada, se usa similitud cosénica para determinar los 3 documentos a devolver.  


## Insuficiencias en la solución y mejoras:
La principal limitación sería en el motor de búsqueda, en el que no hicimos mucho énfasis por razones ya mencionadas, se pueden agregar retroalimentación, expansión de consulta, entre otros mecanismos. Lo otro sería la base de datos para extraer las noticias a recomendar, crear una forma de actualizar esta desde la interfaz gráfica(lo cual requerirá realizar preprocesamiento y se estima que tarde unos minutos)