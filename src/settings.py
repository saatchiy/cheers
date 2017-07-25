import xml.etree.ElementTree as ET
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType

class Settings:
    """Implements a setting class to keep the settings of the program."""

    __pi_algorithm = PiAlgorithmType.BBP
    __alpha_calculation_algorithm = AlphaAlgorithmType.Newton
    __precision = 10

    def __init__(self, setting_file_address):
        xml_tree = ET.parse("settings.xml")
        settings_root = xml_tree.getroot()
        