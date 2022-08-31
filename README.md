# SCRAPING TEMPLATE

This app serves as a template for preparing scraping scripts. It already includes basic API created with FastAPI,
db creation with migrations configuration (alembic), celery worker to perform async scraping and notifications through 
email and Slack in case of script fail. Everything is prepared to work in Docker containers.

To run it simpy hit `docker-compose up` but first you should prepare some stuff:

1. Your code - you already have folders prepared. Put your scraping scripts into `./api/scraping/`, create db models in 
`./api/scraping/`. You can also create routes and pydantic schemas to present and filter your scraping results in FastAPI.


2. Create db migration with [alembic](https://alembic.sqlalchemy.org/en/latest/autogenerate.html).


3. Prepare email notification - this feature is prepared to work with your Google account. All you need to do is create a 
few env variables:
    - MAIL_LOGIN - login to your sender email
    - MAIL_PASSWORD - password generated for this app in your Google account security settings
    - NOTIFICATION_EMAIL - email where the messages should be sent


4. Prepare Slack notification - everything you should prepare is described in this [tutorial](https://api.slack.com/messaging/sending).
Although here is some brief to make your life easier:
    - create Slack app (name it whatever you want)
    - grant scope `chat:write` to your Slack app
    - add your Slack app to your Slack workspace
    - choose channel where you want to receive your notifications and invite your app to this channel by writing `/invite @APP_NAME`
    - prepare two env variables that you will get going through previous steps:
      - SLACK_BOT_OAUTH_TOKEN
      - SLACK_CHANNEL_ID


5. Add your scraping functions to celery task `scraping` in `./app/celery_worker/tasks.py` file. 
This task is set to be invoked by crontab every sunday at midnight, but you can easily change it by editing `./app/celery_worker/celery.py` file.