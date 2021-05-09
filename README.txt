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

5. Run the flask server at port 5000 with respective routes:
localhost:5000