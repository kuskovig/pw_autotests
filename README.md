## Test automation for Planyway webapp
Those test aren't much usefull, whole thing have been done just for learning purpose.

<center><h3>Description </h3></center>

Within this project there are UI test  for Planyway webapp written in Python with Pytest framework, wrapped in container. Those test can be executed either directly on host machine via terminal, on Selenoid container or with Jenkins pipeline.

#### Basic pipeline:
1. <ins>Jenkins</ins> (runs as container from a custom image with Docker CLI) grabs code from <ins>GitHub</ins> repo
2. <ins>Jenkins</ins> builds Docker image from Dockerfile provided. To build image, <ins>Jenkins</ins> calls Docker Daemon on host machine
3. Based on params provided on pipeline start, tests are executed either on local machine or in <ins>Selenoid</ins> container within desired browser
4. After running the tests, <ins> Allure </ins> report is generated, which can be accessed from <ins>Jenkins</ins>

#### What is in this project:
- `Python` 
- `Docker` 
- `Jenkins` CI/CD tool. Works as  a container on host machine  from custom image with Docker CLI
- `Selenoid` Running test in browsers-as-containers. Works as container on host machine
- `Allure` Report generating tool
#### As for Python, packages that were used are:
- `Pytest`  - as testing framework
- `Selenium` - browser automation
- `Allure-pytest`  - logs collector for Allure reporting
- `Pytest-xdist` - distributing tests across multiple CPUs to speed up test execution
- `Requests` - simple http requests

<center> <h3>How to start</h3></center>

1. Build Selenoid and run it  [Official documentation](https://aerokube.com/selenoid/latest/#_quick_start_guide)
2. Download/update browsers for Selenoid with `cm selenoid update`
3.  Build Jenkins + Docker CLI  via Dockerfile from `/jenkinsdocker`
4. Create volume which will be used for Jenkins with `docker volume create VOLUMENAME`
5. Run Jenkins with `docker run -d --restart=always -u root --name CONTAINERNAME --link socat:socat -p 8085:8080 -p 50000:50000 -v VOLUMENAME:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock IMAGENAME` where:
	CONTAINERNAME - desired name for your container
	VOLUMENAME - name of volume, created in step #4
	IMAGENAME - name of image, created in step #3
6. Run socat container with `docker run -d --restart=always -p 127.0.0.1:2376:2375 -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock`. This container connects Jenkins with Docker Daemon on host machine.
7.  Start test via Jenkins TBD

