"""Define a foss compatability license_matrix.

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
"""
from __future__ import annotations

from json import load
from pathlib import Path

import licensematrix as lm
from licensematrix.license_type import License

THISDIR = Path(__file__).resolve().parent
with open(str(THISDIR / "license_matrix.json")) as sMatrix:
	SUPPLEMENT_MATRIX = load(sMatrix)


def licenseType(licenseStr: str) -> list[License]:
	"""Return a list of license types from a license string.

	Args:
		licenseStr (str): license name(s)

	Returns:
		list[License]: the license
	"""
	licenses = []
	liceList = licenseStr.split(", ") # Deal with multilicense
	for lice in liceList:
		licenses.append(lm.licenseMatrix.licenseFromAltName(lice.strip()))
	return licenses


def depCompatibleLice(myLicense: License, depLice: list[License]) -> bool:
	"""Identify if the end user license is compatible with the dependency license(s).

	Args:
		myLicense (License): end user license to check
		depLice (list[License]): dependency license

	Returns:
		bool: True if compatible, otherwise False
	"""
	for dep in depLice:
		if not myLicense.naiveCompatSourceLinking(dep):
			# if the dep appears on the rhs then compatible
			if dep.spdx in SUPPLEMENT_MATRIX[myLicense.spdx]:
				return True
			return False
	return True
