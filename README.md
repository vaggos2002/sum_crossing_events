
# sum_crossing_events
Compute the sum of crossing events

# Setup

1. Clone the repository
```
  $ git clone https://github.com/vaggos2002/sum_crossing_events.git
  cd sum_crossing_events
```

2. Use pip to install pip3 and virtualenv
```
  $ sudo apt-get install python3-pip libsqlite3-dev
  sqlite3
  $ sudo -H pip3 install virtualenv
```

3. Create and activate a virtualenv and install the dependencies
```
  $ virtualenv -p python3 env
  $ source ./env/bin/activate
  $ pip3 install -r requirements

```


https://realpython.com/blog/python/token-based-authentication-with-flask/

# Usage

1. Run the server 
```
  $ python3 server.py
```

2. Call the api : 
```
   $ curl --data 'signal=4,5,6,8,3,5,-2,4,-1&value=5' http://127.0.0.1:5000/
```


## Running the service

1. Installation
2. User registration 
3. API access

In order to identify a user, the web server uses a 


https://blog.miguelgrinberg.com/post/restful-authentication-with-flask

# Scale up



# Tests

* Verify the sum function
* Verify the reponce codes
* Verify concurrent connections
