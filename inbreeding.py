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

    def get_coefficient(self) -> float:
        """Get the inbreeding coefficient of the loaded pedigree"""

        paternal = []
        maternal = []

        if self.sire_key in self.pedigree and self.pedigree[self.sire_key]:
            self._map_pedigree(self.pedigree[self.sire_key], [], paternal)

        if self.dam_key in self.pedigree and self.pedigree[self.dam_key]:
            self._map_pedigree(self.pedigree[self.dam_key], [], maternal)

        # with open("out.txt", "w") as f:
        #     f.write(f"{"-"*20} SIRE SIDE {"-"*20}\n")
        #     f.write("\n".join([str(x) for x in paternal]))
        #     f.write(f"\n\n{"-"*20} DAM SIDE {"-"*20}\n")
        #     f.write("\n".join([str(x) for x in maternal]))

        return self._calculate_from_maps(maternal, paternal)

    def _map_pedigree(self, pedigree, layers, result):
        layers = [pedigree[self.id_key]] + layers
        result.append(layers)

        if self.sire_key in pedigree and pedigree[self.sire_key]:
            self._map_pedigree(pedigree[self.sire_key], layers, result)

        if self.dam_key in pedigree and pedigree[self.dam_key]:
            self._map_pedigree(pedigree[self.dam_key], layers, result)

    def _calculate_from_maps(self, maternal, paternal):
        result = 0
        for m in maternal:
            m0 = m[0]

            for p in paternal:
                p0 = p[0]

                if m0 == p0:
                    check = True
                    for e in m:
                        if e in p and e != m0:
                            check = False

                    if check:
                        inb = 0.5 ** (len(m) + len(p) - 1)
                        result += inb

        return result
