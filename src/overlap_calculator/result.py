from mpmath import nstr
import xml.etree.ElementTree as ET
from .calculation_conditions import CalculationConditions

class Result:
    """Implementation of a class to hold a result and conditions of the calculation."""

    def __init__(self, radius, conditions, length, alpha, pi):
        self.__coaster_radius = radius
        self.__calculation_conditions = conditions
        self.__overlapping_length = length
        self.__alpha = alpha
        self.__pi = pi

    def to_xml_element(self):
        """Creats a result XML element."""

        # Creating result element : This is a root for each result but a subelement for the results file
        result_elem = ET.Element("result")

        precision = self.__calculation_conditions.get_precision()

        # Creating conditions element
        conditions_elem = ET.SubElement(result_elem, "conditions")

        # Creating pi element
        pi_elem = ET.SubElement(conditions_elem, "pi")
        pi_algorithm = ET.SubElement(pi_elem, "algorithm").text = self.__calculation_conditions.get_pi_algorithm().name
        pi_val_elem = ET.SubElement(pi_elem, "value").text = nstr(self.__pi, precision)

        # Creating Alpha Element
        alpha_elem = ET.SubElement(conditions_elem, "alpha")
        alpha_algorithm = ET.SubElement(alpha_elem, "algorithm").text = self.__calculation_conditions.get_approximation_algorithm().name
        alpha_precision = ET.SubElement(alpha_elem, "precision").text = str(precision)
        alpha_value = ET.SubElement(alpha_elem, "value").text = nstr(self.__alpha, precision)

        # Creating radius and length
        radius_elem = ET.SubElement(result_elem, "radius").text = nstr(self.__coaster_radius, precision)
        overlap_len_elem = ET.SubElement(result_elem, "overlaplength").text = nstr(self.__overlapping_length, precision)

        return result_elem


    def get_coaster_radius(self):
        return self.__coaster_radius

    def get_pi_algorithm(self):
        return self.__calculation_conditions.get_pi_algorithm()

    def get_approximation_algorithm(self):
        return self.__calculation_conditions.get_approximation_algorithm()

    def get_precision(self):
        return self.__calculation_conditions.get_precision()

    def get_overlapping_length(self):
        return self.__overlapping_length

    def get_alpha(self):
        return self.__alpha

    def get_pi(self):
        return self.__pi
