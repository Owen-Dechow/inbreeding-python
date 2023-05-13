# inbreeding-python
Inbreeding Coefficient Calculator For Pedigrees

## How to use
___
### 1. Create a python dict containing the pedigree.
```python
# Pedigree example with 0.25 inbreeding coefficient (25%)
pedigree = {
    "sire": {
        "sire": None,
        "dam": None,
        "id": "2834",
    },
    "dam": {
        "sire": {
            "sire": None,
            "dam": None,
            "id": "2834",
        },
        "dam": None,
        "id": "781",
    },
    "id": "622",
}
```
All animals in pedigree must have a unique id. If the sire/dam of an animal is unknown the value can be set to None or the key can be omitted all together.

___

### 2. Create an instance of the InbreedingCalculator class and load pedigree.
```python
calculator = InbreedingCalculator(pedigree)
```
or
```python
calculator = InbreedingCalculator()
calculator.pedigree = pedigree
```

___

### 3. If you used keys other than sire, dam & id ensure you configure your InbreedingCalculator for them.
```python
pedigree = {
"Father": None,
"Mother": None,
"Name": "Billy"
}

calculator = InbreedingCalculator(pedigree, "Father", "Mother", "Name")
```
or
```python
calculator = InbreedingCalculator(pedigree)
calculator.sire_key = "Father"
calculator.dam_key = "Mother"
calculator.id_key = "Name"
```

___
### 4. Use the get_coefficient method to find the inbreeding percentage
```python
pedigree = {
    "sire": {
        "sire": None,
        "dam": None,
        "id": "2834",
    },
    "dam": {
        "sire": {
            "sire": None,
            "dam": None,
            "id": "2834",
        },
        "dam": None,
        "id": "781",
    },
    "id": "622",
}

calculator = InbreedingCalculator(pedigree)
ic = calculator.get_coefficient()
print(f"Inbreeding Coefficient: {ic} ({ic * 100}%)")
```
Output
```
Inbreeding Coefficient: 0.25 (25.0%)
````