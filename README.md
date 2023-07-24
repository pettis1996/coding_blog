## Personal Blog Project

***

> author: @pettis1996
> Project made using Python Django. 
> Check requirements.txt file for all installed modules.

***

### Setup and Deploy on AWS EC2

**Step 1:**
Update the system.
```bash
    sudo apt-get update
```

**Step 2:**
Clone the repository on the server.
```bash
    git clone https://github.com/pettis1996/coding_blog.git
```

**Step 3:**
Download Django using pip.
```bash
    sudo apt install python3-pip -y
```

```bash
    pip install django
```

**Step 4:**
Make migrations.
```bash
    python3 manage.py makemigrations
```

**Step 5:**
Migrate changes.
```bash
    python3 manage.py migrate
```

**Step 6:**
Install required modules from requirements.txt.
```bash
    pip install -r requirements.txt
```

Now the app is ready to run. To run it use the following command:
```bash
    python3 manage.py runserver 0.0.0.0:8000
```
OR for [Local Hosting](http://127.0.0.1:8000)
```bash
    python3 manage.py runserver
```
> use 0.0.0.0:8000 for hosting on AWS EC2