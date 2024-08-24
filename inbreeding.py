class InbreedingCalculator:
    def __init__(
        self,
        pedigree: dict[str, str] = {},
        sire_key: str = "sire",
        dam_key: str = "dam",
        id_key: str = "id",
    ):
        self.pedigree = pedigree
        self.sire_key = sire_key
        self.dam_key = dam_key
        self.id_key = id_key
        self._catch = {}

    def get_coefficient(self) -> float:
        """Get the inbreeding coefficient of the loaded pedigree"""
        return self._get_coefficient_of_pedigree(self.pedigree)

    def _get_coefficient_of_pedigree(self, pedigree) -> float:
        if pedigree[self.id_key] in self._catch:
            return self._catch[pedigree[self.id_key]]

        SK = self.sire_key
        DK = self.dam_key

        paternal = []
        maternal = []

        if SK in pedigree and pedigree[SK]:
            self._map_pedigree(pedigree[SK], [], paternal)

        if DK in pedigree and pedigree[DK]:
            self._map_pedigree(pedigree[DK], [], maternal)

        coefficient = self._calculate_from_maps(maternal, paternal)
        self._catch[pedigree[self.id_key]] = coefficient
        return coefficient

    def _map_pedigree(self, pedigree, layers, result):
        this_co = self._get_coefficient_of_pedigree(pedigree)
        layers = [
            (
                pedigree[self.id_key],
                this_co,
            )
        ] + layers
        result.append(layers)

        if self.sire_key in pedigree and pedigree[self.sire_key]:
            self._map_pedigree(pedigree[self.sire_key], layers, result)

        if self.dam_key in pedigree and pedigree[self.dam_key]:
            self._map_pedigree(pedigree[self.dam_key], layers, result)

    def _calculate_from_maps(self, maternal_maps, paternal_maps):
        result = 0

        for maternal_animal_map in maternal_maps:
            isolated_maternal_animal = maternal_animal_map[0]

            for paternal_animal_map in paternal_maps:
                isolated_paternal_animal = paternal_animal_map[0]

                if isolated_maternal_animal[0] == isolated_paternal_animal[0]:
                    joined = maternal_animal_map + paternal_animal_map
                    loop_len = len(joined) - 1
                    if len(set(joined)) == loop_len:
                        inbreeding = 0.5**loop_len
                        parental_inbreeding = (
                            isolated_paternal_animal[1] + isolated_maternal_animal[1]
                        ) / 2
                        result += inbreeding * (1 + parental_inbreeding)

        return result
