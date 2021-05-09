# FlaskAPI-with-SQLAmchemy

Steps to test the API

1. Create a virtual environment such as ISI-env with the below command:
python -m venv ISI-env

2. Activate the virtual environment using:
source ISI-env/Scripts/activate

3. Git clone the repo as: 
git clone https://github.com/ashutosh-1407/FlaskAPI-with-SQLAmchemy.git

4. Go inside the cloned repo:
cd FlaskAPI-with-SQLAmchemy

4. Build the docker image containing postgresql and flask server using below command:
docker-compose up

5. check the container-id of flask image
docker ps

6. open the container using the below command and cd into app folder
docker exec -it <container-id> bash
cd app

7. Run the tests by running the below command
pytest

8. Run the flask server at port 5000 with respective routes:
localhost:5000/