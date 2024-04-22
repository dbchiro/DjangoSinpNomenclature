# CHANGELOG

## 1.1.0 - 2024-04-22

- Reset migrations du to breaking migratio system on child modules (sinp_organisms)
- Update dependencies

## 1.0.1 - 2024-04-11

- Improve tests
- Improve github actions

## 1.0.0 - 2024-04-04

- Migrate to new SINP Standard ([Dictionnaire de données du SINP v1.0 - Mai 2023](https://inpn.mnhn.fr/docs-web/docs/download/421821))
- Improve natural key functions
- Import new official SINP nomenclatures

## 0.3.0 - 2024-03-26

- Add natural primary keys to models
- Remove foreign keys to accounts (`created_by` and `updated_by` fields)
- Refactor repository:
  - New github hooks to automate actions (docs publication, releases, tests, etc.)
  - Docs is now using markdown files

## v0.2.5

- Add french translation
- Add parent nomenclature specification (almost required for new incoming bats gites nomenclature)

## v0.1.1

- Update poetry config
- Rename "Item" model to "Nomenclature"

## v0.1.0

- 3 models to structure datas:
  - Source
  - Type
  - Item
- Main admin config, managed by superusers
