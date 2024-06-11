from inbreeding import InbreedingCalculator
from json import load as json_load
from random import shuffle as random_shuffle
from sys import argv
from time import time

def _test(shuffle=False, quick_fail=False, info=False):
    # Get pedigrees
    pedigrees = json_load(open("test_data.json"))
    if shuffle:
        random_shuffle(pedigrees)

    # Set initial data
    failed = {}
    passed = {}
    start_time = time()

    # Open tests meter
    print("[", end="")
    for idx, (pedigree, correct, _name) in enumerate(pedigrees):
        calculator = InbreedingCalculator(
            pedigree, sire_key="s", dam_key="d", id_key="name"
        )
        tested = calculator.get_coefficient()

        if tested == correct:
            print(".", end="")
            passed[idx] = tested
        else:
            print("F", end="")
            failed[idx] = tested
            if quick_fail:
                break
    
    # Close tests meter
    print(f"] x{len(failed) + len(passed)}{f"/{len(pedigrees)}" if quick_fail else ""}")

    # Print tests results
    if failed:
        print(
            f"TEST FAILED [failed={len(failed)}, passed={len(passed)}]"
        )
    else:
        print("ALL TESTS PASSED")
    
    # Print test time
    print(f"Time: {time() - start_time}")

    # Print info
    if info:
        print("\nPassed:")
        for idx in passed:
            pedigree = pedigrees[idx]
            print(f"\t{pedigree[2]}")

        print("Failed:")
        for idx, tested in failed.items():
            pedigree = pedigrees[idx]
            print(f"\t{pedigree[2]} [tested={tested} correct={pedigree[1]}]")

def test(**kwargs):
    print()
    print("=" * 30, "Inbreeding Python Test", "=" * 30)
    
    _test(**kwargs)

    print("=" * 84)
    print()


if __name__ == "__main__":
    test(
        **{
            "shuffle": "-s" in argv or "--shuffle" in argv,
            "quick_fail": "-q" in argv or "--quick-fail" in argv,
            "info": "-i" in argv or "--info" in argv,
        }
    )
