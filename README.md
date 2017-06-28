
# sum_crossing_events
The server.py script is a basic REST API framework to compute the sum of crossing events.
It was developed in Debian 8.7 with Python 3.4 and has third party dependencies (Flask, Flask-API, Flask-HTTPAuth).

To call the REST API, the user will need to be authenticated. The following credentials can be used:
- Method : Basic Authentication
- Username: evan
- Password: python3


## Setup

1. Clone the repository
```
  $ git clone https://github.com/vaggos2002/sum_crossing_events.git
  $ cd sum_crossing_events
```

2. Use pip to install pip3 and virtualenv
```
  $ sudo apt-get install python3-pip
  $ sudo -H pip3 install virtualenv
```

3. Create and activate a virtualenv and install the dependencies
```
  $ virtualenv -p python3 env
  $ source ./env/bin/activate
  $ pip3 install -r requirements

```

## Usage

1. Run the server 
```
  $ python3 server.py
```

2. Call the api : 

```
   >>> $ curl -u <username>:<password> --data 'signal=<signal>&value=<value>' <server_url>
   # Example
   >>> $ curl -u evan:python3 --data 'signal=4,5,6,8,3,5,-2,4,-1&value=5' http://127.0.0.1:5000/
   >>> {"crossing_number": 2}
   >>>
```


## Scale up and Future development

- Depending on the size of the project, improve its structure. Use django framework  to organize the models,  views
  url and templates
- The usage of a database to store user's credentials it will be needed as the application will have 
  more complicated business logic.
- By running the application like app.run(), we can get one single syncronous process (1 request at 
  a time). By using a WSGI HTTP Server (e.g. Gunicorn) it is possible to increase the number of 
  processes that can run at the same time.   
  (http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/)
  
  

## Tests

The tests.py script contains automated tests for testing the functionality of the 'server.py' script.
It was developed in Python 3.4 and has the same third party dependencies as the 'server.py'. 

To execute the test suites:
```
    # Add execute only access permission
    chmod +x tests.py
    # Execute the test cases
    python3 tests.py
```

The REST API framework was tested to return the following HTTP Status Codes: 
- 200 OK
- 404 Not Found
- 401 Unauthorized
- 422 Unprocessable Entity
