# inbreeding-python
Inbreeding Coefficient Calculator for Pedigrees in Python

## How to use

1. Create a python dictionary containing a pedigree.
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
    All animals in pedigree must have a unique id. If the sire/dam of an animal is unknown the value can be set to `None` or the key can be omitted all together.


2. Create an instance of the `InbreedingCalculator` class and load the pedigree.
    ```python
    calculator = InbreedingCalculator(pedigree)
    ```
    or
    ```python
    calculator = InbreedingCalculator()
    calculator.pedigree = pedigree
    ```


3. Configure Calculator
   
    If you used keys other than `sire`, `dam` & `id` ensure you configure your `InbreedingCalculator` object for them.
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

    
4. Use the `get_coefficient` method to find the inbreeding percentage
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

**If you use this code please give proper credit.**
<br>
**Thank you, [Owen Dechow](https://github.com/Owen-Dechow)!**
