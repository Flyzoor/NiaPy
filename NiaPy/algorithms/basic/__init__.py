"""Implementation of basic nature-inspired algorithms."""

from NiaPy.algorithms.basic.ba import BatAlgorithm
from NiaPy.algorithms.basic.fa import FireflyAlgorithm
from NiaPy.algorithms.basic.de import DifferentialEvolutionAlgorithm
from NiaPy.algorithms.basic.fpa import FlowerPollinationAlgorithm
from NiaPy.algorithms.basic.gwo import GreyWolfOptimizer
from NiaPy.algorithms.basic.ga import GeneticAlgorithm
from NiaPy.algorithms.basic.abc import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic.pso import ParticleSwarmAlgorithm
from NiaPy.algorithms.basic.ca import CamelAlgorithm
from NiaPy.algorithms.basic.bbfwa import BareBonesFireworksAlgorithm
from NiaPy.algorithms.basic.ihc import HillClimbAlgorithm
from NiaPy.algorithms.basic.sa import SimulatedAnnealing

__all__ = [
    'BatAlgorithm',
    'FireflyAlgorithm',
    'DifferentialEvolutionAlgorithm',
    'FlowerPollinationAlgorithm',
    'GreyWolfOptimizer',
    'GeneticAlgorithm',
    'ArtificialBeeColonyAlgorithm',
    'ParticleSwarmAlgorithm',
    'BareBonesFireworksAlgorithm',
    'CamelAlgorithm',
    'HillClimbAlgorithm',
    'SimulatedAnnealing'
]
