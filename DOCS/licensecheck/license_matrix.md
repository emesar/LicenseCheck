# license_matrix

> Auto-generated documentation for [licensecheck.license_matrix](../../licensecheck/license_matrix.py) module.

Define a foss compatability license_matrix.

- [Licensecheck](../README.md#licensecheck-index) / [Modules](../README.md#licensecheck-modules) / [licensecheck](index.md#licensecheck) / license_matrix
    - [depCompatibleLice](#depcompatiblelice)
    - [licenseType](#licensetype)

Standard disclaimer:: I am not a lawyer and there is no guarentee that the
information provided here is complete or correct. Do not take this as legal
advice on foss license compatability

https://en.wikipedia.org/wiki/IANAL

Types of license/ compatability

Public Domain
- Unlicense

Permissive Compatible
Permissive license compatible with gpl
- Mit
- Boost
- Bsd
- Isc
- Ncsa

Permissive Not Compatible
Permissive license NOT compatible with gpl
- Apache
- Eclipse
- Acedemic Free

Copyleft
permissive -> lgpl 2.1 -> gpl 2
permissive -> lgpl 3 -> gpl 3 -> agpl
permissive -> mpl -> gpl -> agpl (3 only)

permissive (any) -> EU
EU -> gpl -> agpl (3 only)

## depCompatibleLice

[[find in source code]](../../licensecheck/license_matrix.py#L67)

```python
def depCompatibleLice(myLicense: License, depLice: list[License]) -> bool:
```

Identify if the end user license is compatible with the dependency license(s).

#### Arguments

- `myLicense` *License* - end user license to check
- `depLice` *list[License]* - dependency license

#### Returns

- `bool` - True if compatible, otherwise False

## licenseType

[[find in source code]](../../licensecheck/license_matrix.py#L51)

```python
def licenseType(licenseStr: str) -> list[License]:
```

Return a list of license types from a license string.

#### Arguments

- `licenseStr` *str* - license name(s)

#### Returns

- `list[License]` - the license
