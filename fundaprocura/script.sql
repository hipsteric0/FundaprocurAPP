
CREATE TABLE fundaprocura.clasificacion (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NULL
);

CREATE TABLE fundaprocura.estado (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NULL
);

CREATE TABLE fundaprocura.parentesco (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NULL
);

CREATE TABLE fundaprocura.instituciones (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NULL,
    nombre VARCHAR(200) NULL,
    direccion VARCHAR(500) NULL,
    correo VARCHAR(100) NULL,
    telefonos VARCHAR(100) NULL,
    fax VARCHAR(100) NULL,
    nombre_contacto VARCHAR(200) NULL,
    grupo VARCHAR(10) NULL,
    tipo_institucion VARCHAR(10) NULL
);

CREATE TABLE fundaprocura.donaciones (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    fecha_donancion DATE NULL,
    equipo VARCHAR(200) NULL,
    observaciones VARCHAR(500) NULL,
    fk_institucion INTEGER NULL,
    FOREIGN KEY (fk_institucion) REFERENCES instituciones(id)
);

CREATE TABLE fundaprocura.casos (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    grupo VARCHAR(10) NULL,
    tipo_caso VARCHAR (10) NULL,
    fecha DATE NULL,
    REF VARCHAR(50) NULL,
    cedula BIGINT NULL,
    apellidos VARCHAR(200) NULL,
    nombres VARCHAR(200) NULL,
    sexo VARCHAR(20) NULL,
    direccion VARCHAR(500) NULL,
    telefono VARCHAR(100) NULL,
    correo VARCHAR(100) NULL,
    locacion_don VARCHAR(100) NULL,
    fecha_accidente DATE NULL,
    causa VARCHAR(100) NULL,
    lesion VARCHAR(100) NULL,
    fecha_nacimiento DATE NULL, 
    lugar_nacimiento VARCHAR(200) NULL,
    municipio_ciudad VARCHAR(200) NULL,
    equipo_actual VARCHAR(200) NULL,
    donacion VARCHAR(10) NULL,
    medidas VARCHAR(500) NULL,
    medidas_instrucciones VARCHAR(500) NULL,
    ultima_medicion DATE NULL,
    serie VARCHAR(50) NULL,
    control_WF VARCHAR(50) NULL,
    nombre_familiar VARCHAR(100) NULL,
    cedula_familiar BIGINT NULL,
    direccion_familiar VARCHAR(500) NULL,
    telefono_familiar VARCHAR(100) NULL,
    recaudos VARCHAR(200) NULL,
    observaciones_comentarios VARCHAR(1000) NULL,
    fk_clasificacion INTEGER NULL,
    fk_esado INTEGER NULL,
    fk_parentesco INTEGER NULL,
    FOREIGN KEY (fk_clasificacion) REFERENCES clasificacion(id),
    FOREIGN KEY (fk_esado) REFERENCES estado(id),
    FOREIGN KEY (fk_parentesco) REFERENCES parentesco(id)
);

CREATE TABLE fundaprocura.historico_donaciones (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    equipo VARCHAR(100) NULL,
    fecha_donancion DATE NULL,
    donaciones INTEGER NULL,
    fecha_prestada DATE NULL,
    equipo_prestado VARCHAR(100) NULL,
    fecha_devolucion DATE NULL,
    fk_caso INTEGER NULL,
    fk_donacion INTEGER NULL,
    FOREIGN KEY (fk_caso) REFERENCES casos(id),
    FOREIGN KEY (fk_donacion) REFERENCES donaciones(id)
);


#Estados
INSERT INTO fundaprocura.estado (nombre) VALUES ('Amazonas');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Anzoátegui');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Apure');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Aragua');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Barinas');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Bolívar');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Carabobo');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Cojedes');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Delta Amacuro');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Dependencias Federales');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Distrito Federal');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Falcón');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Guárico');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Lara');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Mérida');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Miranda');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Monagas');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Nueva Esparta');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Portuguesa');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Sucre');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Táchira');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Trujillo');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Vargas');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Yaracuy');
INSERT INTO fundaprocura.estado (nombre) VALUES ('Zulia');

#Clasificación
INSERT INTO fundaprocura.clasificacion (nombre) VALUES ('Niño');
INSERT INTO fundaprocura.clasificacion (nombre) VALUES ('Adolescente');
INSERT INTO fundaprocura.clasificacion (nombre) VALUES ('Adulto');
INSERT INTO fundaprocura.clasificacion (nombre) VALUES ('Adulto mayor');

#Parentesco
INSERT INTO fundaprocura.parentesco (nombre) VALUES ('Madre/Padre');
INSERT INTO fundaprocura.parentesco (nombre) VALUES ('Abuelo/Abuela');
INSERT INTO fundaprocura.parentesco (nombre) VALUES ('Tio/Tia');
INSERT INTO fundaprocura.parentesco (nombre) VALUES ('Otro');

