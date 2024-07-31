# GETTING STARTED

## Available endpoints

- `nomenclatures/sources` > list all sources
- `nomenclatures/sources/<pk>` > get one nomenclature by id
- `nomenclatures/types` > list all nomenclature types
- `nomenclatures/types/<pk>` > get one type by id
- `nomenclatures/nomenclatures` > list all nomenclatures
- `nomenclatures/nomenclatures/<pk>` > get one nomenclature by id

## Supported Python versions

- Coming soon

## Supported Django versions

- Django 2.2 (not tested) > Django 4.x


## Supported Django Rest Framework versions

- Django Rest Framework 3.12

## Installation

```bash
 > pip install -U dj-sinp-nomenclatures
```

## Configuration

Configure `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    (...),
    'rest_framework',
    'sinp_nomenclatures',
    'sinp_organisms',
    (...),
)
```

Configure `urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    (...),
    path('', include('sinp_nomenclatures.urls')),
    (...),
]
```

## Install SINP data dictionnary V1.0

source:&nbsp;: https://www.patrinat.fr/sites/patrinat/files/part_docs/DictionnaireDonn%C3%A9esSINP_V1.0.pdf

French SINP data dictionnary (v1.0) are provided within a fixture.
Those data can be loaded with this command:

```bash
manage.py loaddata sinp_dict_data_v1.0.json
```
