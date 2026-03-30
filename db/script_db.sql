-- ======================================================
-- SCRIPT DE BASE DE DATOS - PROYECTO REPOSTERÍA (UEA)
-- Estudiante: Aslhy Flores
-- ======================================================

-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS desarrollo_web;
USE desarrollo_web;

-- 2. Limpiar tablas si ya existen (para evitar errores al re-ejecutar)
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;

-- 3. Crear tabla de Categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- 4. Crear tabla de Productos (Entidad principal con Relación)
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) 
    REFERENCES categorias(id_categoria) ON DELETE SET NULL
);

-- 5. Insertar datos iniciales (Data de prueba para el docente)
INSERT INTO categorias (nombre) VALUES 
('Tortas y Pasteles'), 
('Postres Fríos'), 
('Galletas y Bocaditos');

INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES 
('Torta de Tres Leches', 18.00, 5, 2),
       ('Pastel de Chocolate Premium', 25.50, 3, 1),
       ('Caja de Macarons x12', 12.00, 15, 3),
       ('Cheesecake de Frutos Rojos', 20.00, 4, 2);

-- 6. Verificar la creación
SELECT * FROM productos;