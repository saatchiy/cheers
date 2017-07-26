from tkinter import *
from tkinter import messagebox
import sys
from mpmath import mpf, nstr
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
        self.__result = -1
        self.__result_str = ""
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

        output_frame = Frame(self.__main_form, borderwidth=2, padx=10, pady=5)
        # Label for the results section
        lbl_result = Label(output_frame, text="Result: ", anchor=W, pady=5)
        lbl_result.pack(side=TOP, fill=X, expand=YES)

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
            self.__result = OverlapCalculator.calculate_overlapping_length(self.__radius, self.__conditions)
            self.__result_str = nstr(self.__result.get_overlapping_length(), self.__conditions.get_precision())

            # Filling the result textbox with the result of the calculation
            self.__txt_result.config(state=NORMAL)
            self.__txt_result.delete(1.0, END)
            self.__txt_result.insert(END, self.__result_str)
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

    def __save(self):
        """Saves the results in an xml file."""
        pass
    
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


    def __exit(self):
        sys.exit()
