## End to end machine learning project

### Create a conda environment
```
conda create -p venv python=3.8
```
### activate conda environment
```
activate
conda activate {path of your conda env}
```

### Intall requirements in the environment
```
pip install -r requirements.txt
```

### Docker Setup In EC2 commands to be Executed
```
sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

### Run a python file
```
python python -m src.components.data_ingestion
```

### Run application
```
python app.py
```
