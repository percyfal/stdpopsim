import pytest

import stdpopsim
from tests import test_species


class TestSpeciesData(test_species.SpeciesTestBase):

    species = stdpopsim.get_species("DroSec")

    def test_ensembl_id(self):
        assert self.species.ensembl_id == "drosophila_sechellia"

    def test_name(self):
        assert self.species.name == "Drosophila sechellia"

    def test_common_name(self):
        assert self.species.common_name == "Drosophila sechellia"

    # QC Tests. These tests are performed by another contributor
    # independently referring to the citations provided in the
    # species definition, filling in the appropriate values
    # and deleting the pytest "skip" annotations.
    @pytest.mark.skip("Population size QC not done yet")
    def test_qc_population_size(self):
        assert self.species.population_size == -1

    @pytest.mark.skip("Generation time QC not done yet")
    def test_qc_generation_time(self):
        assert self.species.generation_time == -1


class TestGenomeData(test_species.GenomeTestBase):

    genome = stdpopsim.get_species("DroSec").genome

    @pytest.mark.parametrize(
        ["name", "rate"],
        {
            "X": 2.99601570921329e-8,
            "2L": 2.40487093035123e-8,
            "2R": 2.66915626038874e-8,
            "3L": 1.79556372412945e-8,
            "3R": 1.97317740267327e-8,
            "4": 2.31848167461603e-8,
        }.items(),
    )
    def test_recombination_rate(self, name, rate):
        assert rate == pytest.approx(
            self.genome.get_chromosome(name).recombination_rate
        )

    @pytest.mark.skip("Mutation rate QC not done yet")
    @pytest.mark.parametrize(["name", "rate"], {}.items())
    def test_mutation_rate(self, name, rate):
        assert pytest.approx(rate, self.genome.get_chromosome(name).mutation_rate)
