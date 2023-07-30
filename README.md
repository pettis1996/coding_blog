## Personal Blog Project - In Development
---

> author: @pettis1996 <br>
> Project made using Python Django for practice. <br>
> Check requirements.txt file for all installed modules. <br>


---

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
<br>

![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

---

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

### Test Account Credentials

> Username
```bash
    test
```

> Password
```bash
    testpassword
```