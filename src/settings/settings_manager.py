import os, sys
import xml.etree.ElementTree as ET
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType
from overlap_calculator.calculation_conditions import CalculationConditions

class SettingsManager:

    @staticmethod
    def read_settings():
        fullpath = os.path.dirname(__file__)

        # Default settings
        pi_algorithm = PiAlgorithmType.BBP
        alpha_approximation_algorithm = AlphaAlgorithmType.Newton
        precision = 11

        settings = None

        try:
            settings = ET.parse(os.path.join(fullpath, "./settings.xml"))
        except Exception:
            errormsg = "Unable to open settings file. Running the default settings."
            print(errormsg)
            raise IOError(errormsg)

        if settings != None:
            settings_root = settings.getroot()

            if settings_root != None:
                # Reading pi settings from the XML
                pi_element = settings_root.find("pi")
                pi_algorithm_text = ""

                if pi_element != None:
                    pi_algorithm_elem = pi_element.find("algorithm")
                    if pi_algorithm_elem != None:
                        pi_algorithm_text = pi_algorithm_elem.text

                if pi_algorithm_text != "":
                    pi_algorithm = PiAlgorithmType[pi_algorithm_text]

                # Reading alpha settings from the XML : alpha approximation algorithm
                alpha_elemet = settings_root.find("alpha")
                alpha_algorithm_text = ""
                precision_text = ""

                if alpha_elemet != None:
                    alpha_algorithm_elem = alpha_elemet.find("algorithm")
                    if alpha_algorithm_elem != None:
                        alpha_algorithm_text = alpha_algorithm_elem.text

                    # Reading alpha settings from the XML : precision of calculation
                    precision_element = alpha_elemet.find("precision")
                    if precision_element != None:
                        precision_text = precision_element.text

                if alpha_algorithm_text != "":
                    alpha_approximation_algorithm = AlphaAlgorithmType[alpha_algorithm_text]

                if precision_text != "":
                    precision = int(precision_text)

        conditions = CalculationConditions(pi_algorithm, alpha_approximation_algorithm, precision)
        return conditions
