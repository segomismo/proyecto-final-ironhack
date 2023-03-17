# Proyecto final ironhack: Pystagram
Este proyecto parte de la idea de analizar las fotografías de las distintas paginas de instagram de national geographic y otro tipo de sitios parecidos a ello.
Para ello, necesitamos crear una base de datos del mayor numero posible de fotografias que podamos conseguir mediante el escreapeo de las paginas de instagram.
El escreapeo de instagram no ha sido tan sencillo como podria parecer a simple vista, dado que tiene algunos funcionamientos un poco extraños que hacen que se pare el escrapeo a veces de forma aleatoria, y otras veces de forma inesperadamente concreta.
Tras unos dias de pruebas y error, no se ha podido conseguir una forma eficaz de escrapear todo el contenido de las paginas que se deseaba, teniendo que parchear el código para que funcionase con un mínimo de eficacia sobre lo deseado.
Tras varios intentos (muchos) intentos, se ha conseguido una base de datos de más de 6500 fotografías con sus respectivos datos en un .csv

Para analizar las fotografias, se ha investigado minuciosamente (quizá demasiado), las distintas posibilidades mediante inteligencia artificial, siendo OpenCV y PyTorch las que mas se adaptaban a mis necesidades.


## Pasos a seguir:
Los pasos a seguir han sido:
- **Creación de código para escreapeo de Instagram con Selenium**
    Para ello, se han guardado las fotografías y se ha creado un archivo .cvs con los datos de la página donde se ha recogido la fotografía, y los distintos parámetros unicos de la fotografia como pueda ser la fecha, el numero de likes, descripción, datos internos de la foto....

    *Problemas: Cierta aletoriedad de errores, y otros constantes que no se han podido solucionar.*


- **Limpieza de obtenidos en el escreapeo**:
    Mediante la utilización de pandas, se ha procedido a la limpieza del archivo obtenido en el escrapeo con la eliminación de nulos, normalización y reducción del archivo .cvs, dando como resultado un archivo con extensión "_clean.cvs". Una de las cosas que se ha podido hacer por la investigación de los datos que daba la pagina, ha sido agregar si habia personas, animales o naturaleza a cierto numero de fotografías sin necesidad de aplicar IA (aunque se haya aplicado mas adelante). Estos valores, en principio, son mas fiables que los de los obtenidos por IA. Pero al no estar completos en la mayoria de las fotografías, si se ha tenido que recurrir a otro tipo de herramientas. El unico valor fiable ha sido el de que la imagen tenga texto


- **Obtención de dominante de color**:
    Mediante la librería PIL (Python Imaging Library), se ha obtenido la dominante de color. Para simplificar el proceso, se ha dividido en solo tres colores: rojo (R), verde (G), azul (B). La elección de estos canales es porque son los principales y mas usados. Se podría haber seleccionado mas colores, pero se ha optado por la simplificación al intentar polarizar resultados. Otra cosa a considerar para el futuro sería analizar la luminosidad de las fotografías


- **Obtención de información de la fotografía** (personas, animales, naturaleza)
    Por medio de las librerias OpenCV de visión artificial y PyTorch, hemos añadido información de si hay personas, animales o naturaleza en cada fotografía. Para ello hemos tenido que crear código para poder procesar las imagenes y muchas horas de paciencia mientras se procesaban.


- **Obtención de complejidad visual**:
    Aquí hemos utilizado tres valores para obtener el nivel de complejidad visual de una fotografía:
    ***Entropía***: La entropía de una imagen es una medida de la cantidad de información o desorden en la imagen. Una imagen con una gran cantidad de detalles y variaciones de color y textura tendrá una entropía más alta que una imagen simple con pocos detalles y colores.
    ***Energía de la imagen***: La energía de una imagen se calcula a partir de su histograma de intensidades. Una imagen con una energía alta tendrá una mayor concentración de píxeles en un rango de intensidades más estrecho.
    ***Enfoque***: El enfoque de una imagen es una medida de la nitidez y los detalles en la imagen. Puedes calcular el enfoque utilizando varios métodos, como el operador de Laplaciano o el operador de Sobel.
    Mediante la libreria de visión artificial OpenCV, hemos calculado esos tres valores para poderlos aplicar luego de manera correlacional


## Correlaciones:
Si bien es cierto que no se han llegado a demasiadas conclusiones dado la variedad de correlaciones que hay entre las diferentes páginas, hay algunas cosas que si podemos ver.

- Las publicaciones que tienen en su contenido personas son en general menos atractivas que las que ofrecen otro tipo de contenido
- Los aspectos fotográficos que se han podido analizar con IA no han sido tan determinantes para que haya intereacciones en la mayoria de páginas analizadas
- Las publicaciones de instagram tienen cada vez menos interacciones

[Aquí dejo toda la información mas en detalle de las conclusiones](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

### Futuros:
Me quedo con muchas dudas en cuanto a los parámetros que he obtenido en la complejidad visual. Creo que se puede hayar bastante mas información con más tiempo. En cuanto a la entropía, por ejemplo, seguro que está más relacionada con la cantidad de objetos que se pueden identificar que en cuanto la textura de la fotografía

También me ha faltado toda la parte de predicción de impacto que creo que si se podria lograr a cierto nivel con alguna de las paginas que cumplen ciertas correlaciones cocnretas