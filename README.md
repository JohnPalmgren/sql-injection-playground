# Testing insecure SQL

## About 
I have done a quick and "hacky" update to the music library starter project in order to play around with some SQL injection scenarios. I've added some insecure routes which include SQL commands which have not been parameterized, and I've come up with a few ways that this can be exploited. 

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv sql-injection-venv

# Activate the virtual environment
; source sql-injection-venv/bin/activate 

# Install dependencies
(sql-injection-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Install the virtual browser we will use for testing
; playwright install
# If you encounter problems at this stage please contact your coach

# Create a development database
(sql-injection-venv); createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(sql-injection-venv); open lib/database_connection.py

# Seed the development database
(sql-injection-venv); python seed_dev_database.py

# Run the app
(sql-injection-venv); python app.py
# Now visit http://localhost:5001/login in your browser
```

## Examples 
Below are example SQL injections attacks that can be run against the insecure database:

### Command
email field: any value

password field: `') OR 1=1 --`

### What it does
It will log you in as the first user in the database

### How it works
It manipulates the intended query to be false `(email, password) = ('x', '')` and adds an `OR` clause that will always evaluate to true `1=1` This then returns all entries from the database and the authenticate function returns the first user from the query results. 
Essentially the query becomes or `SELECT * FROM users WHERE false OR true` which is always true

![query](assets/2025-11-02%2016.28.36%20127.0.0.1%20f19e14c640c7.png)
![result](assets/2025-11-02%2016.29.14%20127.0.0.1%201256c4965b93.png)


### Command
email field: any value

password field:  `') OR email = 'jake@makers.tech'; --`

### What it does
It will log you in with the provided email without a password. 

### How it works
It works as above but the `WHERE` clause is manipulated to select a user with a particular email address. So the query essentially becomes `SELECT * FROM users WHERE email = "target_email"`

![query](assets/2025-11-02%2016.34.49%20127.0.0.1%20569e654424c8.png)
![result](assets/2025-11-02%2016.36.08%20127.0.0.1%20209d6e50b509.png)

### Command
email field: any value
password field:  `') OR admin = true; --`

### What it does
It will log you in as the first admin user that exists in the database

### How it works
It works in the same way as the email attack except it looks for an admin flag on the user table. The request evaluates to `SELECT * FROM users WHERE admin = true`

![query](assets/2025-11-02%2016.39.35%20127.0.0.1%20d6af0e29784e.png)
![result](assets/2025-11-02%2016.39.51%20127.0.0.1%20db56f873a8a9.png)


### Command
url: baseurl/login/-1%20UNION%20SELECT%20id,password,email,admin,password%20FROM%20users%20WHERE%20email='nadia@makers.tech'

**The SQL**
```SQL
SELECT * FROM users 
  WHERE id = -1 
UNION
SELECT id, password, email, admin, password FROM users
  WHERE email = 'nadia@makers.tech'
```


### What it does
It displays the password of the user with the inputted email to the screen

### How it works
The url is expecting an id as a query parameter which is passed directly into the SQL query. The -1 means no users are found and the UNION keyword attaches another result to the original. Crucially, the request selects id, password... not id,name... which means that instead of the users name being displayed on the screen the password is instead. 


### Command
url: baseurl/login/-1%20UNION%20SELECT%20id,password,email,admin,password%20FROM%20users%20WHERE%20admin=true

**The SQL**
```SQL
SELECT * FROM users 
  WHERE id = -1 
UNION
SELECT id, password, email, admin, password FROM users
  WHERE admin = true
```

### What it does
Display the password of the first admin in the database

### How it works
As above except instead of selecting on email, it will select the first admin in the database and manipulate the query so the password is put in place of the name and then displayed on the screen. 

![url-email-attack](assets/2025-11-02%2016.45.14%20127.0.0.1%20d3bf34541996.png)


## Mitigation
All The above attacks can be mitigated by adding user input as parameters in the SQL rather than injecting them directly into the command, for example 

```python
    def authenticate_user(self, user):
        command = 'SELECT * FROM users WHERE (email, password) = (%s, %s)'
        rows = self.connection.execute(command, [user.email, user.password])
        if len(rows) > 0:
            row = rows[0]
            return User(row["id"], row["name"], row["email"], row["admin"])
        return None
```

Additionally typecasting the user id to an int in the route prevents a SQL string being passed in:
```python
@app.route('/login/<int:id>')
```
Rather than
```python
@app.route('/login/<id>')
```