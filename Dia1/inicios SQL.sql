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
select * from productos;