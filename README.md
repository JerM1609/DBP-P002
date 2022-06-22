# **DBP-P002**

## SETUP
```
node -v
npm -v
git --version
npm install -g @vue/cli
```

```
vue ui  // launch vue ui
```

## FRONTEND FOLDER

```
npm install .       // restore node project (package.json)
npm run serve       // start dev server
npm run lint --fix  // fix lint errors
```

## BACKEND FOLDER

```
py -m venv venv
pip install -r requirements.txt
pip freeze > requirements.txt
```

## DEPLOYMENT

0. Set `.env` file in `backend/api/config` folder and upload credentials.

1. Restore venv
    
    `py -m venv venv`

    `pip install -r requirements.txt`

2. Launch **Flask API server** 
    
    `py run.py`

3. Restore Nodejs project in folder where `package.json` file exists.

    `npm install .`

4. Launch **Vue.js server**    

    `npm run serve`

5. Enjoy it!

## REFERENCES

- [Full Stack Project with Vue.js and Flask](https://www.youtube.com/watch?v=lenV5aVOMp8)