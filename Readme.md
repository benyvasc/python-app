docker build -t python-app:1.0 .
docker run --rm -p 8080:5000  python-app:1.0