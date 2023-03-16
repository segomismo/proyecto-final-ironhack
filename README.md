# proyecto-final-ironhack
Este proyecto parte de la idea de analizar las fotografías de las distintas paginas de instagram de national geographic y otro tipo de sitios parecidos a ello.
Para ello, necesitamos crear una base de datos del mayor numero posible de fotografias que podamos conseguir mediante el escreapeo de las paginas de instagram.
El escreapeo de instagram no ha sido tan sencillo como podria parecer a simple vista, dado que tiene algunos funcionamientos un poco extraños que hacen que se pare el escrapeo a veces de forma aleatoria, y otras veces de forma inesperadamente concreta.
Tras unos dias de pruebas y error, no se ha podido conseguir una forma eficaz de escrapear todo el contenido de las paginas que se deseaba, teniendo que parchear el código para que funcionase con un mínimo de eficacia sobre lo deseado.
Tras varios intentos (muchos) intentos, se ha conseguido una base de datos de más de 6500 fotografías con sus respectivos datos en un .csv

Para analizar las fotografias, se ha investigado minuciosamente (quizá demasiado), las distintas posibilidades mediante inteligencia artificial, siendo OpenCV y PyTorch las que mas se adaptaban a mis necesidades.


## Pasos a seguir:
Los pasos a seguir han sido:
- Creación de código para escreapeo de Instagram con Selenium
    Para ello, se han guardado las fotografías y se ha creado un archivo .cvs con los datos de la página donde se ha recogido la fotografía, y los distintos parámetros unicos de la fotografia como pueda ser la fecha, el numero de likes, descripción, datos internos de la foto....

    Problemas: Cierta aletoriedad de errores, y otros constantes que no se han podido solucionar. 


- Limpieza de obtenidos en el escreapeo:
    Mediante la utilización de pandas, se ha procedido a la limpieza del archivo obtenido en el escrapeo con la eliminación de nulos, normalización y reducción del archivo .cvs, dando como resultado un archivo con extensión "_clean.cvs". Una de las cosas que se ha podido hacer por la investigación de los datos que daba la pagina, ha sido agregar si habia personas, animales o naturaleza a cierto numero de fotografías sin necesidad de aplicar IA (aunque se haya aplicado mas adelante). Estos valores, en principio, son mas fiables que los de los obtenidos por IA. Pero al no estar completos en la mayoria de las fotografías, si se ha tenido que recurrir a otro tipo de herramientas. El unico valor fiable ha sido el de que la imagen tenga texto


- Obtención de dominante de color:
    Mediante la librería PIL (Python Imaging Library), se ha obtenido la dominante de color. Para simplificar el proceso, se ha dividido en solo tres colores: rojo (R), verde (G), azul (B). La elección de estos canales es porque son los principales y mas usados. Se podría haber seleccionado mas colores, pero se ha optado por la simplificación al intentar polarizar resultados


- Obtención de información de la fotografía (personas, animales, naturaleza)
    Por medio de las librerias OpenCV y PyTorch, 


- Obtención de complejidad visual

