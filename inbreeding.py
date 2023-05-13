class InbreedingCalculator:
    def __init__(
        self,
        pedagree: dict = {},
        sire_key: str = "sire",
        dam_key: str = "dam",
        id_key: str = "id",
    ):
        self.pedagree = pedagree
        self.sire_key = sire_key
        self.dam_key = dam_key
        self.id_key = id_key

    def get_coefficient(self):
        """Get the inbreeding coefficient of the loaded pedigree"""

        p = self.pedagree

        paternal = self._map_parents(p[self.sire_key], {}, 0, "Y")
        fraternal = self._map_parents(p[self.dam_key], {}, 0, "X")

        inbreeding = 0
        for animal_paternal, depths_paternal in paternal.items():
            if animal_paternal in fraternal:
                for depth_fraternal in fraternal[animal_paternal]:
                    for depth_paternal in depths_paternal:
                        inbreeding += 0.5 ** (depth_paternal + depth_fraternal + 1)

        return inbreeding

    def _map_parents(self, p, dic, depth, sex):
        if p[self.id_key] + sex in dic:
            dic[p[self.id_key] + sex].append(depth)
        else:
            dic[p[self.id_key] + sex] = [depth]

        if p[self.sire_key]:
            dic = self._map_parents(p[self.sire_key], dic, depth + 1, "Y")

        if p[self.dam_key]:
            dic = self._map_parents(p[self.dam_key], dic, depth + 1, "X")

        return dic
