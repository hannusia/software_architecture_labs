# Lab1: Basic architecture of the micro-services

## Requirements

You need Python 3, curl for testing and to install requirements by running:
```
$ pip install -r requirements.txt
```

## Usage

You can run servoces separately by executing following commands:
```
$ python facade-service/facade_app.py
```

```
$ python logging-service/logging_app.py
```

```
$ python message-service/message_app.py
```

To send POST requests:
```
$ curl -X POST <url> -d <message>

#For example
$ curl -X POST http://127.0.0.1:8080/facade -d "Hi! This is my first message"
```

To send GET requests:
```
curl -X GET [url]

#For example
curl -X GET http://127.0.0.1:8080/facade
```

Sent messages will be stored by logging service in local dictionary.

## Results
Examples of working services and their logs and outputs are in screenshots folder.
