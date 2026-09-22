# Ron Jerick Gamba Portfolio

A single-page portfolio built with Django, plain templates, and a responsive static stylesheet.

## Run locally

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

## Customize

- Update the profile copy and project list in `portfolio/views.py`.
- Replace the social and email links in `templates/portfolio/home.html`.
- Add a PDF resume under `static/` and wire the header action when ready.
- Adjust colors, type, and responsive layout in `static/css/site.css`.
