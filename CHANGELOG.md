# CHANGELOG

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
