from abc import ABC, abstractmethod
# A base abstract class for different implementations of algorithms
# to calculate Pi number

class PiAlgorithmBase(ABC):
    """A base abstract class for different implementations of algorithms
    to calculate Pi number
    """
    @abstractmethod
    def calculate(precision):
        """Abstract method which will be implemented to calculate Pi number

        precision -- the desired precision of calculation
        """
        pass