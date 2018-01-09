# mytardis-app-process_embargo
Mytardis app to make experiments public after embargo expiry period of 1095 days(3 Years)

This app should be installed in "tardis/apps/mydata":

```cd /mytardis/taris/apps
git clone https://github.com/manishkumr/mytardis-app-process_embargo.git
```
Add this app to tardis/settings.py:

```
INSTALLED_APPS += ('tardis.apps.process_embargo',)
```
Add celerybeat schedule to tardis/settings.json:

```
"process_embargo": {
                "schedule": {
                    "minutes": 2
                },
                "task": "tardis_portal.process_embargo"
            },
 ```


Restart MyTardis.
