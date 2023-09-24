# The Twelve-Factor App

Для установки приложения на своем устройстве необходимо установить необходимые библиотеки. Для этого достаточно выполнить установку из файла requirements.txt:
```
pip install -r requirements.txt
```
Для работы понадобится Redis. При наличии Docker развернуть ее можно следующей командой:
```
docker run -p 6379:6379 redis
```
Далее просто запускаем файл main.py следующей командой:
```
python main.py
```

Данное приложение способно совершать два действия:
1. Считать количество посещений (visit)
2. Возвращать количество посещений (show)

Шаблоны запросов:
```
1. http://<host>/visit/<ID>
2. http://<host>/show/<ID>
```
