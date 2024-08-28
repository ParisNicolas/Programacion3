/*Obtener los nombres de los equipos y sus integrantes*/
/*(LEFT JOIN) incluyendo equipos que no tienen integrantes asignados*/
SELECT equipo.nombre AS Equipo, integrante.nombre AS Integrante
FROM equipo
LEFT JOIN integrante ON equipo.id = integrante.group_id;

/*Obtener los integrantes de cada colegio*/
SELECT 
    equipo.colegio AS colegio,
    integrante.nombre AS integrante
FROM integrante
INNER JOIN equipo ON integrante.group_id = equipo.id
ORDER BY equipo.colegio, integrante.nombre;

/*Obtener la cantidad de integrantes de cada equipo*/
SELECT equipo.nombre AS Equipo, COUNT(integrante.id) AS Total_integrantes
FROM equipo
JOIN integrante ON equipo.id = integrante.group_id
GROUP BY equipo.nombre;

/*Obtener la cantidad de integrantes de cada colegio*/
SELECT 
    equipo.colegio AS colegio, 
    COUNT(integrante.id) AS cantidad_integrantes
FROM integrante
INNER JOIN equipo ON integrante.group_id = equipo.id
GROUP BY equipo.colegio
ORDER BY cantidad_integrantes DESC;


/*Buscar a una persona en especifico, y traer su telefono, su colegio y el deporte en que participa*/
SELECT 
    integrante.nombre AS integrante, 
    integrante.telefono AS telefono, 
    equipo.colegio AS colegio, 
    equipo.deporte AS deporte
FROM integrante
INNER JOIN equipo ON integrante.group_id = equipo.id
WHERE integrante.nombre LIKE '%nombre%';

/*Obtener los integrantes de los equipos que son veganos o celíacos*/
/*INNER JOIN*/
SELECT equipo.nombre AS equipo, integrante.nombre AS integrante
FROM equipo
INNER JOIN integrante ON equipo.id = integrante.group_id
WHERE integrante.vegano = TRUE OR integrante.celiaco = TRUE;

/*Marcar todos los equipos sin integrantes como no pagados*/
/*Tecnicamente imposible esto deberia ser observado*/
UPDATE equipo
SET pagado = FALSE
FROM equipo
LEFT JOIN integrante ON equipo.id = integrante.group_id
WHERE integrante.id IS NULL;

/*Muestra todos los integrantes cuyo telefono es igual al del encargado*/
/*Esto sirve para saber en que equipos el encargado podria estar jugando*/
SELECT integrante.nombre AS integrante, equipo.nombre AS equipo, integrante.telefono AS telefono
FROM integrante
INNER JOIN equipo ON integrante.group_id = equipo.id
WHERE integrante.telefono = equipo.telefono_encargado;

