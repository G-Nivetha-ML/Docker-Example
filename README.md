# Docker Projects Examples

This repository contains two Dockerized applications

### Prerequisites

To run the projects locally, you'll need to have Docker installed.

1. Install Docker:
   ```bash
   sudo apt update
   sudo apt install docker.io -y
   ```

3. Ensure Docker is running:  
   Verify Docker is correctly installed by running:

   ```bash
   sudo systemctl status docker
   sudo usermod -aG docker ubuntu #logout and login back
   docker run hello-world
   ```
4. Create respective folders and enter and then login to docker :  

   ```bash
   docker login  #Then enter username and password of the dockerhub
   ```

5. Run the Docker Commands :  

    Build the Docker Image
   ```bash
   docker build -t username/Image-name:latest .
   ```

   Run the Docker Container
   ```bash
   docker run -it username/Image-name:latest
   ```
   Push the Docker Image to Docker Hub
   ```bash
   docker push username/Image-name:latest
   ```

