class InbreedingCalculator:
    def __init__(
        self,
        pedigree: dict = {},
        sire_key: str = "sire",
        dam_key: str = "dam",
        id_key: str = "id",
    ):
        self.pedigree = pedigree
        self.sire_key = sire_key
        self.dam_key = dam_key
        self.id_key = id_key

    def get_coefficient(self) -> float:
        """Get the inbreeding coefficient of the loaded pedigree"""

        p = self.pedigree

        if self.sire_key in p and p[self.sire_key]:
            paternal = {}
            self._map_parents(p[self.sire_key], paternal, 0, "Y")
        if self.dam_key in p and p[self.dam_key]:
            maternal = {}
            self._map_parents(p[self.dam_key], maternal, 0, "X")

        inbreeding = 0
        for animal_paternal, depths_paternal in paternal.items():
            if animal_paternal in maternal:
                for depth_maternal in maternal[animal_paternal]:
                    for depth_paternal in depths_paternal:
                        inbreeding += 0.5 ** (depth_paternal + depth_maternal + 1)

        return inbreeding

    def _map_parents(self, p, dic, depth, sex) -> dict:
        if f"{p[self.id_key]}{sex}" in dic:
            dic[f"{p[self.id_key]}{sex}"].append(depth)
        else:
            dic[f"{p[self.id_key]}{sex}"] = [depth]

        if self.sire_key in p and p[self.sire_key]:
            self._map_parents(p[self.sire_key], dic, depth + 1, "Y")

        if self.dam_key in p and p[self.dam_key]:
            self._map_parents(p[self.dam_key], dic, depth + 1, "X")
