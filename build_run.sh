sudo docker build -t planup .

sudo docker rm -f planup
sudo docker run -it --name planup -p 8000:8000 -v $PWD:/code/ planup
