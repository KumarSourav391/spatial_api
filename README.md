# Spatial Data API (Flask + PostgresSQL)

A RESTful API to store and retrieve spatial Point and Polygon data using Flask and PostgresSQL.

---

## 🔧 Setup Instructions

1. **Create PostgreSQL + PostGIS Database**
   ```sql
   CREATE DATABASE spatialdb;
   \c spatialdb
   CREATE EXTENSION postgis;
