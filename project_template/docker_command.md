# Docker Commands Cheat Sheet

| **Category**       | **Command**                                        | **Description**                                                                 |
|---------------------|----------------------------------------------------|---------------------------------------------------------------------------------|
| **Images**         | `docker images`                                    | Lists all images.                                                              |
|                    | `docker tag <image_id> <new_name>`                 | Renames an existing image.                                                     |
|                    | `docker save -o <file.tar> <image_name>`           | Saves an image to a file.                                                      |
|                    | `docker load -i <file.tar>`                        | Loads an image from a file.                                                    |
| **Containers**     | `docker ps`                                        | Lists running containers.                                                      |
|                    | `docker ps -a`                                     | Lists all containers (including stopped ones).                                 |
|                    | `docker start <container_name>`                    | Starts a stopped container.                                                    |
|                    | `docker stop <container_name>`                     | Stops a running container.                                                     |
|                    | `docker logs <container_name>`                     | Displays logs from a container.                                                |
|                    | `docker exec -it <container_name> sh`              | Opens a shell inside a container.                                              |
|                    | `docker cp <container_name>:<path_in_container> <path_on_host>` | Copies a file from a container to the host.                                    |
|                    | `docker cp <path_on_host> <container_name>:<path_in_container>` | Copies a file from the host to a container.                                    |
| **Build**          | `docker build -t <name> .`                         | Builds an image from a Dockerfile in the current directory.                    |
| **Remove**         | `docker rm <container_name>`                       | Removes a container.                                                           |
|                    | `docker rmi <image_name>`                          | Removes an image.                                                              |
|                    | `docker system prune`                              | Cleans up unused images, containers, volumes, and networks.                    |
|                    | `docker image prune`                               | Removes unused images.                                                         |
|                    | `docker container prune`                           | Removes stopped containers.                                                    |
|                    | `docker volume prune`                              | Removes unused volumes.                                                        |
| **Stats & Logs**   | `docker stats`                                     | Displays resource usage statistics for containers.                             |
|                    | `docker inspect <id>`                              | Displays detailed information about an image or container.                     |
| **Networks**       | `docker network ls`                                | Lists all Docker networks.                                                     |
|                    | `docker network inspect <network_name>`            | Displays details of a specific network.                                        |
|                    | `docker network create <network_name>`             | Creates a new Docker network.                                                  |
| **Volumes**        | `docker volume ls`                                 | Lists all Docker volumes.                                                      |
|                    | `docker volume inspect <volume_name>`              | Displays details of a specific volume.                                         |
|                    | `docker volume rm <volume_name>`                   | Removes a specific volume.                                                     |
| **Compose**        | `docker compose up`                                | Builds, creates, starts, and attaches to containers.                           |
|                    | `docker compose down`                              | Stops and removes containers, networks, and images created by `docker compose`.|
|                    | `docker compose stop`                              | Stops running containers without removing them.                                |
|                    | `docker compose ps`                                | Lists services defined in the `docker-compose.yml` file.                       |
|                    | `docker compose logs <service_name>`               | Displays logs for a specific service.                                          |
