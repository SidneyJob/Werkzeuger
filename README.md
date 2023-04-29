# Werkzeuger

The script was written to generate a debug pin and correct cookie for flask applications based on Werkzeug. 
Read more about generating pin in my article: LINK

![Screenshot](https://github.com/SidneyJob/Generate-flask-pin/blob/main/img/help.png)

**Required options:**
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



Example to use:

![Screenshot](https://github.com/SidneyJob/Generate-flask-pin/blob/main/img/gen.png)

```python3 gen.py --username user --path /home/user/.local/lib/python3.11/site-packages/flask/app.py --mac fc:44:82:9d:ba:02 --machine_id b643ebdac5ee44789d21e98a03ce4bb5 --cgroup 0::/user.slice/user-1000.slice/session-2.scope --modname flask.app --appname Flask```

Original pin:
![Screenshot](https://github.com/SidneyJob/Generate-flask-pin/blob/main/img/origin.png)



If you are doing these steps on your machine, then you can use the GET command to get some variables from your machine.
```python3 gen.py GET```

![Screenshot](https://github.com/SidneyJob/Generate-flask-pin/blob/main/img/get.png)


#### Follow me on my channel: https://t.me/SidneyJobChannel
#### If you have any questions, then write to me by mail SidneyJob13@gmail.com or telegram @SidneyJob