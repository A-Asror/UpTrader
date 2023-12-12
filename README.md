# UpTrader Project ⚙️🛠️

##  Скачать Приложение | Download App 📖
### **HTTPS**
_**git clone**_ _https://github.com/A-Asror/UpTrader.git_

### **SSH**
_**git clone**_ _https://github.com/A-Asror/UpTrader.git_

##  Настройка проекта | Set up the project 🔨
### **Create folders in the root of the app: assets, static, logs**
### **Update .env file**
```shell
Linux
  sudo mv .env.example .env
Windows:
  ren .\.env.example .env
```

##  Настройка виртуального окружения | Configuring the Virtual Environment ☁️
### **Linux 🐧**
```shell
python3 -m venv venv OR python -m venv venv
source venv\bin\activate
```
### **Windows 💻**
```shell
cmd
py -m venv venv OR python -m venv venv
venv\scripts\activate
```

##  Установка зависимости | Installing requirements ⚡️
```shell
pip install -r requirements/dev.txt
```

##  Запуск проект локально | Run the project locally ✅
``` shell
python manage.py runserver
```
