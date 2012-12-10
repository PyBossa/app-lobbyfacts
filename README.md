## Setup instructions

At first create a new PyBossa app and update the values in ``config.py``.

Run the initial scripts

```bash
python 1_load_categories.py
python 2_get_representatives.py
python 3_ids_as_csv.py
python 4_push_presenter.py
```

Now upload the created ``representatives-ids.csv`` to a web server, go to your app again and bulk-import tasks from the uploaded CSV.

