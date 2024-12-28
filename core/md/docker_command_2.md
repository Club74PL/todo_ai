### Docker Commands and Their Descriptions

| **Command**                      | **Description**                                                                                  |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| `docker compose build`           | Builds images defined in the `docker-compose.yml` file.                                         |
| `docker compose build --no-cache`| Builds images without using the cache, ensuring a fresh build.                                 |
| `docker compose up`              | Creates and starts containers based on the `docker-compose.yml` file.                          |
| `docker compose up --build`      | Builds images before starting the containers.                                                  |
| `docker compose up --build -d`   | Builds images, starts containers in detached mode (running in the background).                 |
| `docker compose down`            | Stops and removes containers defined in the `docker-compose.yml` file.                        |
| `docker compose down -v`         | Stops and removes containers along with associated volumes.                                    |
| `docker system prune`            | Removes unused containers, networks, images, and build cache.                                  |
| `docker system prune -a`         | Removes all unused containers, networks, images, and build cache, including unused images.     |
