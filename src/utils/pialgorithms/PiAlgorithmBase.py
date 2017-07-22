from abc import ABC, abstractmethod
# A base abstract class for different implementations of algorithms
# to calculate Pi number

class PiAlgorithmBase(ABC):
    """A base abstract class for different implementations of algorithms
    to calculate Pi number
    """
    @abstractmethod
    def calculate(self, precision):
        """Abstract method which will be implemented to calculate Pi number.

        Args:
            precision: the desired precision of calculation

        Returns:
            A decimal number calculation of PI
        """
        pass
