mkdir droneio
cd droneio

nano Dockerfile

# Insert into following line

# Pull from base Ubuntu image
FROM ubuntu

# Do system updates and install dependencies
RUN apt-get update
RUN apt-get -y upgrade
RUN sudo apt-get -y install git wget
RUN apt-get clean

# Download Drone.io
RUN wget http://downloads.drone.io/master/drone.deb
RUN dpkg -i drone.deb

# Expose the Drone.io port
EXPOSE 8080

ENV DRONE_SERVER_PORT 0.0.0.0:8080
ENV DRONE_DATABASE_DATASOURCE /var/lib/drone/drone.sqlite

# Define our GitHub oAuth keys below
ENV DRONE_GITHUB_CLIENT <CLIENT_TOKEN_HERE>
ENV DRONE_GITHUB_SECRET <CLIENT_SECRET_HERE>

# The command we'll be running when the container starts
CMD /usr/local/bin/droned

# Save

docker build -t my_drone .

touch drone.sqlite

sudo docker run -d --name="droneci" -p 8080:8080  -v /var/lib/drone/:/var/lib/drone  -v /var/run/docker.sock:/var/run/docker.sock   -v /root/droneio/drone.sqlite:/var/lib/drone/drone.sqlite  my_drone

sudo apt-get build-dep python-imaging
sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
sudo pip install Pillow