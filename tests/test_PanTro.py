import stdpopsim

import pytest

from tests import test_species


class TestSpecies(test_species.SpeciesTestBase):

    species = stdpopsim.get_species("PanTro")

    def test_ensembl_id(self):
        assert self.species.ensembl_id == "pan_troglodytes"

    def test_name(self):
        assert self.species.name == "Pan troglodytes"

    def test_common_name(self):
        assert self.species.common_name == "Chimpanzee"

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


class TestGenome(test_species.GenomeTestBase):

    genome = stdpopsim.get_species("PanTro").genome

    @pytest.mark.skip("Number of chromosomes QC not done yet")
    def test_basic_attributes(self):
        assert len(self.genome.chromosomes) == -1

    @pytest.mark.skip("Recombination rate QC not done yet")
    @pytest.mark.parametrize("chr_id", [chrom.id for chrom in genome.chromosomes])
    def test_recombination_rate(self, chr_id, rate):
        assert rate == pytest.approx(
            self.genome.get_chromosome(chr_id).recombination_rate
        )

    @pytest.mark.skip("Mutation rate QC not done yet")
    @pytest.mark.parametrize("chr_id", [chrom.id for chrom in genome.chromosomes])
    def test_mutation_rate(self, chr_id, rate):
        assert rate == pytest.approx(self.genome.get_chromosome(chr_id).mutation_rate)
