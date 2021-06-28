# asgiref-thread-bug

## How to get the bug to trigger

```
git clone https://github.com/rdmrocha/asgiref-thread-bug.git

docker-compose up
```
After that, access http://localhost:8000 on your browser

## How to get it to run last version

- edit requirements.txt
- uncomment 3.3.4 and comment 3.4.0, save the file
- re-run ```docker-compose up```
- access http://localhost:8000 on your browser again
