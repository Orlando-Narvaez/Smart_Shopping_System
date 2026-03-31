# 🧠 Smart Shopping System

## 📌 Descripción

Smart Shopping System es una aplicación web diseñada para ayudar a las familias a gestionar sus compras de mercado de forma más eficiente, combinando listas compartidas, comparación de precios entre supermercados y análisis de hábitos de compra.

El sistema permite que múltiples usuarios colaboren en tiempo real, analicen su comportamiento de compra y tomen decisiones más inteligentes basadas en precios y preferencias.

---

## 🎯 Objetivo Principal

Construir un sistema inteligente que ayude a los usuarios a:

* Encontrar la forma más económica de hacer su mercado
* Tener en cuenta las preferencias familiares
* Analizar hábitos de compra a lo largo del tiempo
* Tomar decisiones basadas en datos

---

## 🚀 Funcionalidades Principales

### 👥 Gestión de Usuarios y Familias

* Registro e inicio de sesión
* Un usuario puede pertenecer a múltiples familias
* Sistema de familias con código de invitación

---

### 🛒 Lista de Mercado Compartida

* Una lista activa por familia
* Agregar, editar y eliminar productos
* Cada producto incluye:
  * Cantidad
  * Unidad (kg, litros, unidades, etc.)
* Marcar productos como comprados
* Actualización en tiempo real para todos los miembros

---

### 🏪 Supermercados y Precios

* Creación manual de supermercados (fase inicial)
* Un producto puede tener múltiples marcas
* Un mismo producto puede tener diferentes precios según:
  * Supermercado
  * Marca
* Comparación de opciones para tomar mejores decisiones

---

### 🧠 Sistema Inteligente (Planeado)

* Recomendaciones basadas en:
  * Precio
  * Preferencias del usuario
* Objetivo futuro:
  * Balance entre costo y preferencia

---

### 📊 Historial y Estadísticas

* Registro de compras realizadas
* Historial de compras
* Estadísticas como:
  * Productos más comprados
  * Gasto mensual
  * Variación de precios

---

## 🛠️ Tecnologías

### Backend

* Python
* FastAPI

### Base de Datos

* SQLite (desarrollo inicial)
* PostgreSQL (producción)

### Validación de Datos

* Pydantic

### Frontend (inicial)

* HTML
* CSS
* JavaScript

### Frontend (futuro)

* React

### Despliegue

* Backend: Render / Railway
* Frontend: Vercel / Netlify

---

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en capas:

* **Routes** → Endpoints de la API
* **Services** → Lógica de negocio
* **Repositories** → Acceso a datos
* **Models** → Entidades de base de datos
* **Schemas** → Validación y transferencia de datos

---

## 🔄 Mejoras Futuras

* Integración automática de supermercados y precios
* Sistema avanzado de recomendaciones
* Autenticación con Google
* Notificaciones (ofertas, cambios de precio, sugerencias)
* Interfaz adaptable a dispositivos móviles

---

## 📈 Estado del Proyecto

🚧 En fase de planificación y desarrollo inicial

---

## 💡 Motivación

Este proyecto busca resolver un problema real del día a día combinando buenas prácticas de desarrollo de softwa
