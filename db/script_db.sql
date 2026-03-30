-- ======================================================
-- SCRIPT DE BASE DE DATOS - PROYECTO REPOSTERÍA (UEA)
-- Estudiante: Aslhy Flores
-- ======================================================

-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS desarrollo_web;
USE desarrollo_web;

-- 2. Limpiar tablas si ya existen (orden inverso por llaves foráneas)
DROP TABLE IF EXISTS facturas;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS clientes;

-- 3. Crear tabla de Categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- 4. Crear tabla de Clientes (Segunda Tabla)
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(15)
);

-- 5. Crear tabla de Productos (Tercera Tabla)
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) 
    REFERENCES categorias(id_categoria) ON DELETE SET NULL
);

-- 6. Crear tabla de Facturas (Tabla de Relación / Facturación)
-- Esta tabla cumple el requisito de integración total
CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT NOT NULL,
    fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2),
    CONSTRAINT fk_cliente_factura FOREIGN KEY (id_cliente) 
    REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    CONSTRAINT fk_producto_factura FOREIGN KEY (id_producto) 
    REFERENCES productos(id_producto) ON DELETE CASCADE
);

-- 7. Insertar datos iniciales (Data de prueba)
INSERT INTO categorias (nombre) VALUES 
('Tortas y Pasteles'), 
('Postres Fríos'), 
('Galletas y Bocaditos');

INSERT INTO clientes (nombre_completo, correo, telefono) VALUES 
('Aslhy Flores', 'aslhy@estudiante.uea.edu.ec', '0999999999'),
('Juan Perez', 'juan.perez@gmail.com', '0988888888');

INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES 
('Torta de Tres Leches', 18.00, 5, 2),
('Pastel de Chocolate Premium', 25.50, 3, 1),
('Caja de Macarons x12', 12.00, 15, 3),
('Cheesecake de Frutos Rojos', 20.00, 4, 2);

-- Insertar una factura de ejemplo
INSERT INTO facturas (id_cliente, id_producto, cantidad, total) VALUES 
(1, 1, 1, 18.00);

-- 8. Verificar la creación
SELECT * FROM productos;
SELECT * FROM clientes;
SELECT * FROM facturas;