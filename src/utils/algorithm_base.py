from abc import ABC, abstractmethod
# A base abstract class for different implementations of algorithms

class AlgorithmBase(ABC):
    """A base abstract class for different implementations of algorithms."""
    @abstractmethod
    def calculate(self, precision):
        """Abstract method which will be implemented in each algorithm class.

        Args:
            precision: the desired precision of calculation

        Returns:
            The result of the calculation
        """
