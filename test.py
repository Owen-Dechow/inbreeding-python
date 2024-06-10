from inbreeding import InbreedingCalculator

PEDIGREES = [
    (
        {
            "id": "1",
            "sire": {"id": "2", "sire": {"id": "4"}, "dam": {"id": "5"}},
            "dam": {"id": "3", "sire": {"id": "4"}, "dam": {"id": "5"}},
        },
        0.25,
    ),
    ({"id": "1", "sire": {"id": "2"}, "dam": {"id": "3"}}, 0),
    (
        {
            "id": "1",
            "sire": {"id": "2", "dam": {"id": "3"}},
            "dam": {"id": "3"},
        },
        0.25,
    ),
    (
        {
            "id": "1",
            "sire": {"id": "2", "dam": {"id": "3"}},
            "dam": {"id": "3"},
        },
        0.37,
    ),
    (
        {
            "id": "1",
            "sire": {
                "id": "2",
                "dam": {
                    "id": "5",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
                "sire": {
                    "id": "4",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
            },
            "dam": {
                "id": "3",
                "sire": {
                    "id": "4",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
                "dam": {
                    "id": "5",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
            },
        },
        0.5,
    ),
    (
        {
            "id": "1",
            "sire": {
                "id": "2",
                "dam": {
                    "id": "5",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
                "sire": {
                    "id": "4",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
            },
            "dam": {
                "id": "3",
                "sire": {
                    "id": "4",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
                "dam": {
                    "id": "5",
                    "sire": {"id": "6", "sire": {"id": "8"}, "dam": {"id": "9"}},
                    "dam": {"id": "7", "sire": {"id": "8"}, "dam": {"id": "9"}},
                },
            },
        },
        0.4063,
    ),
]

if __name__ == "__main__":
    for pedigree, coefficient in PEDIGREES:
        calculator = InbreedingCalculator(pedigree)
        print(calculator.get_coefficient(), coefficient)
