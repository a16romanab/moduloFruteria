# modulo Frutería
Módulo para controlar socios de una frutería.

- Éste módulo tiene cómo objetivo controlar los socios (clientes vip) de una frutería que ofrece a sus socios la opción de hacer peticiones.
Está formado por 4 modelos, que son los Socios, las frutas, las peticiones y sus respectivas lineas.

- El modelo socios hereda de res_partner y añade el campo id_socio,imagen_socio, partner_id y ids_peticiones.
En su vista de tree mostrará el id de socio y el partner_id, en su vista de form mostrará el id_socio, el partner_id, la imagen del socio y abajo de todo las peticiones realizas.

- El modelo fruta tiene los campos nombre de fruta y preciokg. Su vista mostrará (tanto en tree como en form) el nombre y su precio.

- El modelo petición constá de los campos id_socio (donde escogemos un socio, o lo creamos), una fecha escogida por nosotros en un calendario, el importeTotal que es un campo calculado y id_lineaPeticion, donde se mostrarán todas las líneas que tenga la petición.
Su vista estará formada por, en la vista tree, la fecha y el id del socio, y en su vista form la fecha, el id_socio, el importe total de la petición y las líneas de ésta. 

- El modelo lineaPeticion tiene los campos id_fruta (donde escogemos o creamos una fruta), id_petición que obtendrá de la petición, los kilos de fruta que se quieran, el importe (que es un campo calculado de kilos*preciokg de la fruta escogida) y el nombre de la fruta.
En la vista de tree se mostrará el nombre de la fruta, los kilos y el importe. En la vista de form se mostrará el id_fruta, el nombre de la fruta escogida, los kilos y el importe.

###### Interfaz 
- Al instalar el módulo frutería, nos saldrá en el menú principal la opción Fruteria,. El menú contiene 3 submenús, Socios (que se abre por defecto), Peticiones y Frutas.

- Al clickar en frutera se abrirá por defecto los socios, dejandonos la opción de crearlos o importarlos, si seleccionamos uno podremos borrarlo o editarlo.

- En el submenú Frutas podremos crear editar o borrar frutas cómo haciamos con los socios.

- Por último, en el submenú de Peticiones, podremos crear, borrar o editar las peticiones, y mientras creamos una petición podemos crear un socio y/o una fruta. Será en este formulario donde añadiremos las lineas de los pedidos, que no se podrán crear sin tener una Petición asociada.

