# mytardis-app-process_embargo
Mytardis app to make experiments public after embargo expiry period of 1095 days(3 Years)

This app should be installed in Mytradis environment by running:

```
pip install -e git://github.com/manishkumr/mytardis-app-process_embargo#egg=process_embargo
```
Add this app to tardis/settings.py:

```
INSTALLED_APPS += ('process_embargo',)
```
Add celerybeat schedule to tardis/settings.json:

```
"process_embargo": {
                "schedule": timedelta(days=1),
                "task": "tardis_portal.process_embargo"
            },
 ```


Restart MyTardis.
