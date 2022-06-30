-- SQL > STRUCTURED QUERY LANGUAGE (Lenguaje de consultas estructurado)
-- Registro > conjunto de datos
-- Dato > un  valor que por si solo no da una buena referencia
-- Las BD estan compuesta por una o varias tablas y cada tabla puede contener uno o varios registros
-- en el lenguaje de BD siempre tenemos que colocar el ";" asi se da cuenta que la instruccion ha terminado

CREATE DATABASE prueba;

-- Sirve para indicar en que BD queremos trabajar

USE prueba;

CREATE TABLE productos(
	-- Obligatoriamente para crear una tabla debemos crear al menos una columna
    -- Solamente se puede usar UNA VEZ el auto_increment por tabla
    -- Primary key > indicaremos que esta columna se comportara como la identificadora de todo este registro
    -- Nombre | Tipo de Dato | [configuraciones adicionales]
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    fecha_vencimiento DATE  
);


-- DDL data definition language(Lenguaje de manipulacion de datos)
-- con esto extraigo, iserto, actualizo y elimino la informacion de la bd

INSERT INTO productos (id,nombre,fecha_vencimiento) VALUES (DEFAULT,'Aguaymanto','2022-07-01');
INSERT INTO productos (id,nombre,fecha_vencimiento) VALUES (DEFAULT,'Cebolla','2022-07-10'),
														   (DEFAULT,'Limon','2022-06-30');	

-- SELECT
-- Al momento de insertar registros y si estamos manejando el autoincrementador y al momento de realizar un registro
-- este fallase el incrementador igual incrementa
SELECT nombre,fecha_vencimiento,id FROM productos;
SELECT * FROM productos;
SELECT fecha_vencimiento AS 'Fecha de Vencimiento' FROM productos;

-- Con la clausula de condicion WHERE indicaremos un filtro para los resultados, esta es la mejor forma
-- de poder hacer busquedas y es recomendable hacerlas a nivel de BD
SELECT*FROM productos WHERE nombre='Cebolla';

-- AND  > todas las condiciones tienen que ser Verdaderas

SELECT*FROM productos WHERE nombre='Cebolla' AND id=1;

-- OR > cualquiera de las condiciones tienen que ser verdaderas
SELECT*FROM productos WHERE nombre='Cebolla' OR id=1;

-- Que en la columna nombre tengamos la letra 'a' y luego por ahi tendremos la letra 'o'
-- % > significa un numero no determinado de letras a cumplirse
SELECT* FROM productos WHERE nombre Like '%a%o%';

-- _ > significa que tiene que respetar un numero determinado de caracteres
SELECT* FROM productos WHERE nombre Like '___a%';

-- ESTO SOLAMENTE FUNCIONA EN SQL SERVER
 -- SELECT* FROM productos WHERE nombre Like '[C-L]%';
 
 -- UPDATE > sirve para actualizar uno o varios registros dependiendo de su condicional
 UPDATE productos SET nombre = 'Cebolla China' WHERE nombre = 'Cebolla';

-- Desactivar el modo seguro > que lo que hace es que ahora podemos hacer actualizaciones sin la necesidad
-- de tener en la condicion a una columna UNIQUE O que sea una KEY
-- No se recomienda desactivar porque podria llevar a hacer modificaciones masivas sin la posibilidad
-- de deshacer esos cambios
SET SQL_SAFE_UPDATES = false; 
 
 

-- DDL data difinition laguage(Lenguaje e definicion de datos)
-- Con esto extraigo, inserto, actualizo y elimino la informacion de la bd
-- INSEERT (insertar nueva informacion)

