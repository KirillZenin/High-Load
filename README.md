## Requirements
`>= python3.5`

## Local env
Create virtual env:
```bash
virtualenv venv -p python3
source venv/bin/activate
```

Install deps:
```bash
pip install -r requirements.txt
```

Run app:
```bash
python3 weatherman.py
```

Try it out:
```bash
curl http://127.0.0.1:5000/v1/current/?city=Tokyo
{
  "city": "Tokyo", 
  "temperature": 23.12, 
  "unit": "celsius"
}

curl http://127.0.0.1:5000/v1/forecast/?city=Tokyo\&dt=15374026
{
  "city": "Tokyo", 
  "temperature": 22.33, 
  "unit": "celsius"
}
```

Create and run docker container:
```bash
sudo docker build -t weatherman:latest .
docker run -d -p 5000:5000 weatherman
```


