from timeit import timeit
from json import load as json_load
from inbreeding import InbreedingCalculator

pedigrees = json_load(open("test_data.json"))


def test_all():
    for pedigree in pedigrees:
        calculator = InbreedingCalculator(
            pedigree[0], sire_key="s", dam_key="d", id_key="name"
        )
        calculator.get_coefficient()


print(timeit(test_all, number=10000))
