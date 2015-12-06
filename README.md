# Upload-File-App

Credit: Ziang Jia

This is a example application teach you how to perform Continuous Integration Testing with Drone.io on Ubuntu and Docker.

Before we start, make sure you have an Ubuntu server or Droplet from DigitalOcean or cloud server on other platform. 

You can get more information about DigitalOcean <a href = "https://www.digitalocean.com/">Here.</a>

<h2> Step 1. Install and Configure Docker on Server </h2>

First login or SSH into your Ubuntu server and initial Terminal. Here we use a Ubuntu Trusty 14.04 (LTS) provided by DigitalOcean.

To test whether Docker is already installed on your server, you can simply command:

$ docker

If it warns you application "docker" has not been installed, then you should follow this Step; Otherwise, skip Step 1.

Docker requires a 64-bit installation regardless of your Ubuntu version. Additionally, your kernel must be 3.10 at minimum. The latest 3.10 minor version or a newer maintained version are also acceptable. To check your current kernel version, open a terminal and use:

$ uname -r 

Docker’s apt repository contains Docker 1.7.1 and higher. To set apt to use packages from the new repository:

1 Add the new gpg key.

$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

2 Open the /etc/apt/sources.list.d/docker.list file in your favorite editor. If the file doesn’t exist, create it.

$ nano /etc/apt/sources.list.d/docker.list

3 Add an entry for your Ubuntu operating system.

$ deb https://apt.dockerproject.org/repo ubuntu-trusty main

4 Update the apt package index.

$ apt-get update

5 Purge the old repo if it exists.

$ apt-get purge lxc-docker

6 Verify that apt is pulling from the right repository.

$ apt-cache policy docker-engine

For Ubuntu Trusty, Vivid, and Wily, it’s recommended to install the linux-image-extra kernel package. The linux-image-extra package allows you use the aufs storage driver.

$ sudo apt-get install linux-image-extra-$(uname -r)

Make sure you have installed the prerequisites for your Ubuntu version. Then, install Docker using the following:

1 Install Docker.

$ sudo apt-get install docker-engine

2 Start the docker daemon.

$ sudo service docker start

3 Verify docker is installed correctly.

$ sudo docker run hello-world

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message. Then, it exits.

If you want to play with Docker a bit more, refer to this introduction including some optional configuration <a href = "https://docs.docker.com/engine/installation/ubuntulinux/">Here.</a>

<h2> Step 2. Prepare GitHub </h2>

Click the Register new application button on the upper right. This will bring up a new form to fill out.

1 Add your Application name. The Homepage URL should be http://YOUR_DROPLET_IP:8080/. 

2 Make sure the Authorization callback URL is set to http://YOUR_DROPLET_IP:8080/api/auth/github.com.

You'll need the Client ID and Client Secret for next step to configure Dockerfile.

<h2> Step 3. Configure Dockerfile </h2>

1 Create a new directory called droneio or whatever you want just to make sure everything organized:

$ mkdir droneio
$ cd droneio

2 Configure Dockerfile

$ nano Dockerfile

press i to Insert into following line:

======================================
FROM ubuntu

RUN apt-get update
RUN apt-get -y upgrade
RUN sudo apt-get -y install git wget
RUN apt-get clean

RUN wget http://downloads.drone.io/master/drone.deb
RUN dpkg -i drone.deb

EXPOSE 8080

ENV DRONE_SERVER_PORT 0.0.0.0:8080
ENV DRONE_DATABASE_DATASOURCE /var/lib/drone/drone.sqlite

ENV DRONE_GITHUB_CLIENT <CLIENT_TOKEN_HERE>
ENV DRONE_GITHUB_SECRET <CLIENT_SECRET_HERE>

CMD /usr/local/bin/droned

==================================

Save it as it is. Replace the <CLIENT_TOKEN_HERE> and <CLIENT_SECRET_HERE> with the tokens noted from the step above.


<h2> Step 4. Build Drone Image and Launch Drone Container </h2>

Now we can build the image using the following command:

$ docker build -t my_drone .

Once it builds successfully, we can spin up a container using our new image. Drone.io needs a place to store information, using an SQLite database file for example.

$ touch drone.sqlite

Launching Drone is fairly straightforward, but we need to do a few extra steps to ensure that Drone can access our host's Docker server. we could use a volume to bind the host socket file to the location where the container's socket file would be. 

$ sudo docker run -d --name="droneci" \
 -p 8080:8080 \ 
 -v /var/lib/drone/:/var/lib/drone \
 -v /var/run/docker.sock:/var/run/docker.sock  \ 
 -v /root/droneio/drone.sqlite:/var/lib/drone/drone.sqlite \
 my_drone

To ensure the container is running, do a quick status check:

$ docker ps

<h2> Step 5. Play with your .drone.yml </h2>

Open your web browser and navigate to: http://YOUR_DROPLET_IP:8080/login. Follow the instruction to syc your application.

To tell Drone how to build and test the code in the GitHub repository, we need to make a new file in the repository called .drone.yml.

========================================
image: python2.7

notify:
  email:
    recipients:
    - zj2170@columbia.edu
  
script:
  - pip install -r requirements.txt
  - pip install Pillow
  - python manage.py test

========================================

<h2> Note </h2>

Here our example is to test whether a POST request to the upload route actually returns the uploaded photo as the response body, so I install an extra python package called "Pillow".

Note that package Pillow has some historical issue and would request extra lib in Ubuntu, we could use following command to install some lib that Pillow needs.

Before running any test on Drone, login to your Ubuntu server and command:

sudo apt-get build-dep python-imaging
sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

This will help you deploy and run this example in the right way.








