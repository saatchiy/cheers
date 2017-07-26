import os, sys
import xml.etree.ElementTree as ET
from xml.dom import minidom
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType
from overlap_calculator.calculation_conditions import CalculationConditions

class SettingsManager:

    @staticmethod
    def read_settings():

        # Default settings
        pi_algorithm = PiAlgorithmType.BBP
        alpha_approximation_algorithm = AlphaAlgorithmType.Newton
        precision = 11

        settings = None

        try:
            settings = ET.parse(SettingsManager.__get_file_path())
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

    @staticmethod
    def write_settings(conditions):
        pi_algorithm = conditions.get_pi_algorithm()
        alpha_approximation_algorithm = conditions.get_approximation_algorithm()
        precision = conditions.get_precision()

        # Creating the root element
        settings_elem = ET.Element("settings")
        
        # Creating Pi element
        pi_elem = ET.SubElement(settings_elem, "pi")
        pi_algorithm_elem = ET.SubElement(pi_elem, "algorithm")
        pi_algorithm_elem.text = pi_algorithm

        # Creating alpha element and its algorithm
        alpha_elem = ET.SubElement(settings_elem, "alpha")
        alpha_algorithm_elem = ET.SubElement(alpha_elem, "algorithm")
        alpha_algorithm_elem.text = alpha_approximation_algorithm
        
        # Creating precision element
        precision_elem = ET.SubElement(alpha_elem, "precision")
        precision_elem.text = precision

        # Adding indentation
        xml_string = ET.tostring(settings_elem, "utf-8")
        parsed = minidom.parseString(xml_string)
        indented_xml = parsed.toprettyxml(indent="\t")

        # Generating the xml tree
        xml_element = ET.fromstring(indented_xml)
        tree = ET.ElementTree(xml_element)

        try:
            # Writing on file
            tree.write(SettingsManager.__get_file_path(), encoding="utf-8", xml_declaration=True)
        except Exception:
            errormsg = "Saving the settings failed. Unable to write on the file."
            print(errormsg)
            raise IOError(errormsg)

    @staticmethod
    def __get_file_path():
        fullpath = os.path.dirname(__file__)
        file_path = os.path.join(fullpath, "./settings.xml")
        return file_path

