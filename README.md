# SINP Organisms for Django

[DjangoSinpNomenclature](https://github.com/dbchiro/DjangoSinpNomenclature) is a simple [Django](https://www.djangoproject.com/) reusable app to manage nomenclatures of the [French SINP standards for species data and metadata exchange](https://inpn.mnhn.fr/programme/donnees-observations-especes/references/standard-echange), respecting standard.

See docs for more details : <https://dbchiro.github.io/DjangoSinpNomenclature/>

## Quick start

1. Install app

```bash
pip install -U dj_sinp_nomenclatures
```

2. Configure `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    (...),
    'rest_framework',
    'sinp_nomenclatures',
    (...),
)
```

3. Configure `urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    (...),
    path('api/v1/', include('sinp_nomenclatures.urls')),
    (...),
]
```

4. Run `python manage.py migrate` to create the polls models.
5. Run `python manage.py loaddata <path to venv>/lib/<python version>/site-packages/sinp_nomenclatures/fixtures/sinp_dict_data_v1.0.json` to load official nomenclatures.
5. Start the development server and visit <http://127.0.0.1:8000/admin/>
   to create an nomenclatures (you'll need the Admin app enabled).

![models](./models.png)
