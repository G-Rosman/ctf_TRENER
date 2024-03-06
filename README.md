# CTF Trainer

CTF Trainer - это веб-приложение, которое позволяет пользователям просматривать информацию о предстоящих событиях CTF (Capture The Flag).

## Установка и запуск

### Бэкенд


```
cd back
sudo apt install python3-venv
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
uvicorn start:app --reload
```


### Фронтенд

1. Убедитесь, что у вас установлен Node.js и npm.
2. Перейдите в директорию фронтенда:

```cd ./front```

3. Установите зависимости:

```pnpm install```


4. Запустите проект:

```pnpm run serve```