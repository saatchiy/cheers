from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import sys
from mpmath import mpf, nstr
import xml.etree.ElementTree as ET
from xml.dom import minidom
from overlap_calculator.overlap_calculator import OverlapCalculator
from settings.settings_manager import SettingsManager
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType
from overlap_calculator.calculation_conditions import CalculationConditions
from exceptions.validation_exception import ValidationException
from exceptions.calculation_exception import CalculationException
from gui.settings_form import SettingsForm

class MainForm:

    def __init__(self):
        self.__radius = -1
        self.__result_list = []
        self.__init_main_form()

    def __init_main_form(self):
        self.__main_form = Tk()
        self.__main_form.title("Cheers")
        self.__main_form.minsize(450, 300)
        self.__main_form.maxsize(450, 300)
        self.__create_widgets()

    def __create_widgets(self):
        """Creates controls of the main form."""

        # Main Menu
        menubar = Menu(self.__main_form)

        # File Cascading Menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save results as XML", command=self.__save)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.__change_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.__exit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Frame holder of input
        input_frame = Frame(self.__main_form, borderwidth=2, padx=10, pady=10)

        # Label for radius input
        lbl_radius = Label(input_frame, text="Overlapping coasters radius:")
        lbl_radius.pack(side=LEFT, fill=NONE, expand=NO)

        # Textbox for radius input
        self.__txt_radius = Entry(input_frame)
        self.__txt_radius.pack(side=LEFT, fill=BOTH, expand=YES, padx=12)

        # Button for starting the calculation
        btn_calculate = Button(input_frame, text="Start Calculation", command=self.__compute)
        btn_calculate.pack(side=LEFT, fill=NONE, expand=NO)

        # Output frame
        output_frame = Frame(self.__main_form, borderwidth=2, padx=10, pady=5)

        # Top output frame
        top_output_frame = Frame(output_frame)

        # Label for the results section
        lbl_result = Label(top_output_frame, text="Result: ", anchor=W, pady=5)
        lbl_result.pack(side=TOP, fill=X, expand=YES)

        # Button for starting the calculation
        btn_clear = Button(top_output_frame, text="Clear results", command=self.__clear_results)
        btn_clear.pack(side=RIGHT, fill=NONE, expand=NO)

        # Textbox for the results
        self.__txt_result = Text(output_frame)
        self.__txt_result.config(state=DISABLED)

        # Scrollbar for the result textbox
        scrl_result = Scrollbar(output_frame, orient=VERTICAL, command=self.__txt_result.yview)

        # Attaching scrollbar to the result textbox
        self.__txt_result['yscroll'] = scrl_result.set
        scrl_result.pack(side=RIGHT, fill=Y)
        self.__txt_result.pack(side=TOP, fill=BOTH, expand=YES)

        # Making the frames visible
        input_frame.pack(side=TOP, fill=X, expand=YES)
        top_output_frame.pack(side=TOP, fill=X, expand=YES)
        output_frame.pack(side=TOP, fill=BOTH, expand=YES)

        self.__main_form.config(menu=menubar)

        # Reading settings from the xml file
        self.__conditions = self.__read_settings()


    def __compute(self):
        """Uses OverlapCalculator class to compute the length of overlapping segment."""
        radius_str = self.__txt_radius.get()

        try:
            self.__validate_input(radius_str)
            self.__radius = mpf(radius_str)
            result = OverlapCalculator.calculate_overlapping_length(self.__radius, self.__conditions)
            result_str = nstr(result.get_overlapping_length(), self.__conditions.get_precision())

            # Adding the current result to the list of results
            self.__result_list.append(result)

            # Filling the result textbox with the result of the calculation
            self.__txt_result.config(state=NORMAL)
            if len(self.__result_list) != 1:
                self.__txt_result.insert(END, "\n---------------------------------\n")    
            self.__txt_result.insert(END, result_str)
            self.__txt_result.config(state=DISABLED)

        except ValidationException as err:
            self.__handleError(err)
        except CalculationException as err:
            self.__handleError(err)


    def __validate_input(self, input_val):
        """Checks to see if the input value is valid or not. If invalid raise an exception"""
        try:
            number = mpf(input_val)
            if number <= 0:
                raise ValidationException("The entered number is not in the range. Please enter a positive number.")
        except ValueError:
            raise ValidationException("The entered value is not a number. Please enter a positive number.")


    def __handleError(self, errMessage):
        messagebox.showerror(title="Error", message=errMessage)
    
    def display(self):
        """Displays the main form."""
        self.__main_form.mainloop()

    def __change_settings(self):
        """Changes the settings of the application by saving new values in the xml file."""
        settings_form = SettingsForm(self.__main_form, self.__conditions)
        conditions = settings_form.get_settings()

        if conditions != None:
            self.__conditions = conditions
            # Writing the new settings on xml file
            try:
                SettingsManager.write_settings(conditions)
            except IOError as err:
                messagebox.showerror(title="Error", message=err)

    def __save(self):
        """Saves the results in an xml file."""
        path = asksaveasfilename(title="Save Results", defaultextension="xml", 
                    filetypes=[("XML files", "*.xml")], parent=self.__main_form, initialdir="./")
        try:
            self.__save_on_file(path)
        except IOError as err:
            messagebox.showerror(title="Error", message=err)

    def __save_on_file(self, path):
        # Creating the root element "results" and adding subelements "result"
        results_elem = ET.Element("results")

        for res_elem in self.__result_list:
            results_elem.append(res_elem.to_xml_element())

        # Adding indentation
        xml_string = ET.tostring(results_elem, "utf-8")
        parsed = minidom.parseString(xml_string)
        indented_xml = parsed.toprettyxml(indent="\t")

        # Generating the xml tree
        xml_element = ET.fromstring(indented_xml)
        tree = ET.ElementTree(xml_element)

        try:
            # Writing on file
            tree.write(path, encoding="utf-8", xml_declaration=True)
        except Exception as err:
            errormsg = "Saving the results failed. " + err
            print(errormsg)
            raise IOError(errormsg)

    def __read_settings(self):
        # Default algorithm to calculate pi
        pi_algorithm = PiAlgorithmType.BBP
        alpha_approximation_algorithm = AlphaAlgorithmType.Newton
        precision = 11

        conditions = None

        try:
            conditions = SettingsManager.read_settings()
        except IOError as err:
            conditions = CalculationConditions(pi_algorithm, alpha_approximation_algorithm, precision)
            messagebox.showwarning(title="Warning", message=err)

        return conditions

    def __clear_results(self):
        # Clearing the result list and the textbox
        self.__txt_result.config(state=NORMAL)
        self.__txt_result.delete(1.0, END)
        self.__txt_result.config(state=DISABLED)


    def __exit(self):
        sys.exit()
