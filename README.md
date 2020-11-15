# PIA


Se solicita codificar en Python 3 una solución a la necesidad de un comercio dedicado a la venta de
bisutería.
Los requerimientos funcionales son los siguientes:
1. Se debe ofrecer un menú navegable con las siguientes opciones:
    1.1. Registrar una venta
    1.2. Consultar ventas de un día específico
    1.3. Salir

2. Para el caso de registrar una venta considere que en una sola venta pueden venderse uno o más
artículos y, para cada uno de ellos, se debe capturar el detalle consistente en:
    2.1. Descripción del artículo
    2.2. Cantidad de piezas vendidas
    2.3. Precio de venta

3. Al final del registro de cada venta, se debe informar el monto total a pagar por parte del cliente
4. Al final del registro de cada venta, se debe almacenar su detalle, incluyendo la fecha actual del
sistema.
5. Para consultar las ventas de un día específico, se le debe solicitar al usuario la fecha que desea
consultar; si existen ventas de la fecha indicada se le deben mostrar al usuario, de lo contrario se le
debe informar que no se registraron ventas para dicha fecha.
Los requerimientos no funcionales son los siguientes:

1. Todos los datos deben almacenarse de manera no volátil en SQLite 3 al momento del registro de la
transacción.
2. Todas las interacciones con el almacenamiento de datos no volátil deben estar protegidas contra
excepciones.
3. La interacción con el usuario será a través del modo texto
Indicaciones específicas:

1. Se debe validar que:
    1.1. En el menú principal solamente se acepten opciones válidas. Si se proporciona una opción no
    válida, se le informa al usuario y se vuelve a presentar el menú.
    1.2. La descripción proporcionada (2.1) no quede vacía, ni formada solamente por espacios en
    blanco
    1.3. La cantidad de piezas y el precio unitario de venta proporcionado (2.2 y 2.3) no sean valores
    negativos
2. Es responsabilidad del equipo de trabajo comprobar la correcta implementación de la funcionalidad
indicada para el proyecto a desarrollar.
Reporte técnico
Especificaciones

Debe contener la siguiente estructura reflejada en el índice (pueden agregarse secciones adicionales,
pero no pueden omitirse las indicadas):

1. Introducción y presentación
2. Especificación y explicación de los objetivos a obtener.
3. Descripción del entorno tecnológico de trabajo
4. Instrucciones de uso del script
5. Roles y aportaciones específicas de los integrantes del equipo
6. Argumentación del cumplimiento de los objetivos basada en el marco teórico presentado
7. Conclusiones generales y discusión de los resultados obtenidos
8. Conclusiones individuales
9. Referencias (En formato APA)
10. Anexos

a. Diagramas de código o Pseudocódigo del script desarrollado
b. Código Python del script
c. Modelo E/R del almacen de datos a utilizar.
d. Presentación de los valores UANL observados durante la elaboración y
presentación del presente trabajo exponiendo de qué manera se logró esto.

Indicaciones específicas

a) El reporte técnico deberá entregarse en:
a. Un solo documento en formato de MsWord (.docx)
b. Fuente Calibri 11
c. Si contiene figuras, o capturas de pantalla, estas deberán identificarse y numerarse para
su referencia en el documento (Los identificadores de estas si podrán estar en una
tipografía de menor tamaño que el cuerpo del documento)
b) La introducción y presentación debe considerar un especial cuidado a la ortografía
c) La especificación y explicación de los objetivos a obtener se refiere a los requerimientos
funcionales del programa, se sugiere generar un checklist de los mismos.
d) El entorno tecnológico de trabajo se refiere al hardware y software utilizado para el desarrollo y
pruebas del código, incluyendo versiones y especificaciones técnicas según corresponda.
e) Las instrucciones de uso del script corresponden a un manual del usuario que incluya capturas
de pantalla para guiar a los nuevos usuarios en la operación del desarrollo.
f) Cada integrante del equipo deberá realizar una aportación sustantiva al desarrollo de este
proyecto; en este apartado se indicará específicamente dicha participación de tal manera que si
se le cuestiona al participante por lo reportado sea capaz de identificar y explicar su trabajo.
g) La argumentación del cumplimiento de los objetivos puede basarse en el checklist previamente
recomendado, aportando capturas de pantalla o algún otro tipo de evidencia legible que
permitan comprobar el cumplimiento de cada elemento, incluyendo las indicaciones específicas
del caso teórico.
h) Cada estudiante deberá expresar sus conclusiones personales después de haber concluido el
caso proponiendo mejoras y extensiones futuras para el caso teórico desarrollado en forma de
una lista de las mismas
i) Las citas y referencias deben estar en formato APA 7, es importante indicar también las fuentes
de la web de acuerdo con el mismo estándar
j) Los anexos 10.a y 10.b de la estructura indicada deben contener números de línea que permitan
referirlos al argumentar el cumplimiento de los objetivos solicitado con respecto al código
python.