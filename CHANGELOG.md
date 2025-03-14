# CHANGELOG

## [1.4.0] - 2025-03-14

### Added
- Adding public API setting

### Changed
- Update dependencies

## [1.3.3] - 2025-02-06

### Added
- Add [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar) for development.

### Changed
- Fix perfs issue
- Restore simple parents nomenclature (`id` list) in NomenclatureSerializer
- Update dependencies


## [1.3.2] - 2025-02-03

- Remove parents from default NomenclatureSerializer, NomenclatureWithParents serializer could be choose by using `?with_parents=true` querystring.
- Update dependencies


## [1.3.1] - 2024-11-27

- Fix parent to parents migration on null values


## [1.3.0] - 2024-11-19

- Parent relation is now manytomany


## [1.2.2] - 2024-09-23

- Change boolean active status on nomenclatures to choice field (hidden, disabled, enabled)


## [1.2.1] - 2024-07-31

- Clarify docs on how to install SINP nomenclatures


## [1.2.0] - 2024-07-29

- Add filter on active nomenclatures (values are `yes`,`no`,`all`)


## [1.1.0] - 2024-04-22

- Reset migrations du to breaking migratio system on child modules (sinp_organisms)
- Update dependencies


## [1.0.1] - 2024-04-11

- Improve tests
- Improve github actions


## [1.0.0] - 2024-04-04

- Migrate to new SINP Standard ([Dictionnaire de données du SINP v1.0 - Mai 2023](https://inpn.mnhn.fr/docs-web/docs/download/421821))
- Improve natural key functions
- Import new official SINP nomenclatures


## [0.3.0] - 2024-03-26

- Add natural primary keys to models
- Remove foreign keys to accounts (`created_by` and `updated_by` fields)
- Refactor repository:
  - New github hooks to automate actions (docs publication, releases, tests, etc.)
  - Docs is now using markdown files


## [0.2.5]

- Add french translation
- Add parent nomenclature specification (almost required for new incoming bats gites nomenclature)

## [0.1.1]

- Update poetry config
- Rename "Item" model to "Nomenclature"


## [0.1.0]

- 3 models to structure datas:
  - Source
  - Type
  - Item
- Main admin config, managed by superusers
