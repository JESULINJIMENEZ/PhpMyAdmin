# Entorno Docker con MySQL y phpMyAdmin

Este proyecto configura un entorno de desarrollo con MySQL 5.7 y phpMyAdmin utilizando Docker Compose.

![Docker con MySQL y phpMyAdmin](https://via.placeholder.com/800x400?text=Docker+MySQL+phpMyAdmin)

## Requisitos previos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

## Estructura del proyecto

```
mi-proyecto-docker/
├── docker-compose.yml
└── README.md
```

## Configuración

El archivo `docker-compose.yml` define dos servicios:

1. **MySQL**: Base de datos MySQL versión 5.7
2. **phpMyAdmin**: Interfaz web para administrar la base de datos MySQL

### Network

Los servicios utilizan una red externa llamada `mi_proyecto_docker_backend_network`. Esta red debe ser creada antes de iniciar los servicios.

## Instalación y uso

### 1. Crear la red de Docker

Primero, crea la red externa necesaria para los servicios:

```bash
docker network create mi_proyecto_docker_backend_network
```

### 2. Iniciar los servicios

Navega hasta el directorio del proyPecto y ejecuta:

```bash
docker-compose up -d
```

El flag `-d` ejecuta los contenedores en segundo plano.

### 3. Verificar que los servicios estén funcionando

```bash
docker-compose ps
```

Deberías ver dos contenedores en ejecución:
- `mysql_container`
- `phpmyadmin_container`

## Acceso a los servicios

### MySQL

- **Host**: localhost
- **Puerto**: 3307 (mapeado al puerto 3306 del contenedor)
- **Usuario**: user
- **Contraseña**: userpassword
- **Base de datos**: cars_dev
- **Usuario root**: root
- **Contraseña root**: rootpassword

Para conectarte desde la línea de comandos:

```bash
mysql -h 127.0.0.1 -P 3307 -u user -p cars_dev
```

### phpMyAdmin

Accede a phpMyAdmin a través de tu navegador web:

- **URL**: http://localhost:8081
- **Servidor**: mysql
- **Usuario**: user (o root)
- **Contraseña**: userpassword (o rootpassword)

## Configuración detallada

### MySQL

```yaml
mysql:
  image: mysql:5.7
  container_name: mysql_container
  environment:
    MYSQL_ROOT_PASSWORD: rootpassword
    MYSQL_USER: user
    MYSQL_PASSWORD: userpassword
    MYSQL_DATABASE: cars_dev
  ports:
    - "3307:3306"  # Puerto externo 3307 para evitar conflictos
  networks:
    - mi_proyecto_docker_backend_network
```

#### Variables de entorno:

- `MYSQL_ROOT_PASSWORD`: Contraseña para el usuario root
- `MYSQL_USER`: Nuevo usuario creado automáticamente
- `MYSQL_PASSWORD`: Contraseña para el nuevo usuario
- `MYSQL_DATABASE`: Base de datos creada automáticamente

### phpMyAdmin

```yaml
phpmyadmin:
  image: phpmyadmin/phpmyadmin
  container_name: phpmyadmin_container
  environment:
    PMA_HOST: mysql  # Nombre del servicio MySQL
    MYSQL_ROOT_PASSWORD: rootpassword
  ports:
    - "8081:80"  # Puerto 8081 para acceder a phpMyAdmin
  networks:
    - mi_proyecto_docker_backend_network
```

#### Variables de entorno:

- `PMA_HOST`: Especifica el host MySQL al que se conectará phpMyAdmin
- `MYSQL_ROOT_PASSWORD`: Contraseña del usuario root de MySQL

## Detener los servicios

Para detener los servicios sin eliminar los contenedores:

```bash
docker-compose stop
```

Para detener y eliminar los contenedores:

```bash
docker-compose down
```
Para detener, eliminar los contenedores y los volúmenes (eliminará todos los datos):

```bash
docker-compose down -v
```

## Solución de problemas

### Error de conexión a MySQL

Si phpMyAdmin no puede conectarse a MySQL, verifica:

1. Que ambos servicios estén en la misma red:
   ```bash
   docker network inspect mi_proyecto_docker_backend_network
   ```

2. El estado de los contenedores:
   ```bash
   docker-compose ps
   ```

3. Los logs de MySQL:
   ```bash
   docker-compose logs mysql
   ```

### Puerto 3307 en uso

Si el puerto 3307 ya está en uso, modifica el mapeo de puertos en el archivo `docker-compose.yml`:

```yaml
ports:
  - "3308:3306"  # Cambia 3307 por otro puerto disponible
```

## Persistencia de datos

Por defecto, los datos de MySQL se almacenan dentro del contenedor. Si deseas persistir los datos, añade un volumen al servicio MySQL en el archivo `docker-compose.yml`:

```yaml
mysql:
  # ... configuración existente ...
  volumes:
    - mysql_data:/var/lib/mysql

# Añadir al final del archivo
volumes:
  mysql_data:
```

## Notas adicionales

- Los puertos utilizados (3307 para MySQL y 8081 para phpMyAdmin) se pueden cambiar si ya están en uso.
- La red `mi_proyecto_docker_backend_network` está configurada como externa, lo que significa que debe ser creada manualmente antes de iniciar los servicios.