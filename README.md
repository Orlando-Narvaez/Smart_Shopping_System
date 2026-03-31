
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

## 🗄️ Modelo de Base de Datos

El sistema está diseñado con una base de datos relacional en PostgreSQL, estructurada para soportar listas compartidas, comparación de precios y análisis histórico.

### 📊 Diagrama ERD

![ERD](https://chatgpt.com/c/docs/erd.png)

---

### 👥 Usuarios y Familias

* **users** → información de usuarios
* **families** → grupos familiares
* **family_members** → relación muchos a muchos entre usuarios y familias

---

### 🛒 Listas de Compra

* **shopping_lists** → lista activa por familia
* **shopping_list_items** → productos dentro de la lista
  * Incluye cantidad, unidad y estado de compra
  * Relación directa con **product_variants** (no productos genéricos)

---

### 🏪 Productos y Variantes

* **products** → producto base (ej: arroz)
* **brands** → marca (ej: Diana)
* **product_variants** → combinación producto + marca
  * Incluye imagen del producto (`image_url`)

---

### 💰 Precios

* **prices** → precio de un producto en un supermercado
  * Relación con:
    * product_variants
    * supermarkets
  * Incluye fecha de última actualización (`updated_at`)

---

### 🏬 Supermercados

* **supermarkets** → tiendas donde se comparan precios

---

### 📊 Historial de Compras

* **purchases** → compra realizada por una familia
* **purchase_items** → detalle de productos comprados

Esto permite:

* Analizar hábitos de compra
* Calcular gasto total
* Generar estadísticas

---

## 🔄 Flujo del Sistema

1. Usuario crea o se une a una familia
2. Se crea una lista de compras activa
3. Se agregan productos (variantes específicas)
4. El sistema permite comparar precios entre supermercados
5. Usuario marca productos como comprados
6. Usuario finaliza la compra
7. El sistema:
   * Guarda la compra en el historial
   * Registra los productos comprados
   * Cierra la lista actual
   * Genera una nueva lista

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
* Comparación de precios entre supermercados

---

### 🧠 Sistema Inteligente (Planeado)

* Recomendaciones basadas en:
  * Precio
  * Preferencias del usuario

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

* PostgreSQL

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
* Historial de precios
* Notificaciones (ofertas, cambios de precio, sugerencias)
* Interfaz adaptable a dispositivos móviles

---

## 📈 Estado del Proyecto

🚧 En fase de desarrollo inicial con base de datos completamente diseñada

---

## 💡 Motivación

Este proyecto busca resolver un problema real del día a día combinando buenas prácticas de desarrollo de software con análisis de datos y toma de decisiones inteligentes.
