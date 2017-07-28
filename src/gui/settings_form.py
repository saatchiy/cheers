from tkinter import *
from tkinter import messagebox
import sys
from exceptions.validation_exception import ValidationException
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType
from overlap_calculator.overlap_calculator import AlgorithmType as AproximationAlgorithmType
from overlap_calculator.calculation_conditions import CalculationConditions


class SettingsForm(Toplevel):

    def __init__(self, parent, conditions):
        self.__settings = None
        self.__init_setting_form(parent, conditions)


    def __init_setting_form(self, parent, conditions):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        self.title("Settings")
        self.minsize(320, 220)
        self.maxsize(320, 220)
        self.__create_widgets(conditions)


    def __create_widgets(self, conditions):
        """Creates controls of the settings form."""
        
        # Frame for organizing widgets related to pi
        param_frame_pi = Frame(self, borderwidth=2, padx=10, pady=5)

        # Label for pi algorithm
        lbl_pi_algorithm = Label(param_frame_pi, text="PI calculation algorithm:")
        lbl_pi_algorithm.pack(side=LEFT, fill=NONE, expand=NO)

        # OptionMenu for selecting pi algorithm
        self.__pi_algorithm_var = StringVar(self)
        pi_options = [item.name for item in PiAlgorithmType]
        self.__pi_algorithm_var.set(pi_options[conditions.get_pi_algorithm().value])
        __opt_pi_algorithm = OptionMenu(param_frame_pi, self.__pi_algorithm_var, *pi_options)
        __opt_pi_algorithm.pack(side=LEFT, fill=X, expand=YES, padx=12)

        # Frame for organizing widgets related to alpha
        param_frame_alpha = Frame(self, borderwidth=2, padx=10, pady=5)

        # Label for alpha calculation approximation algorithm
        lbl_alpha_algorithm = Label(param_frame_alpha, text="Approximation algorithm:")
        lbl_alpha_algorithm.pack(side=LEFT, fill=NONE, expand=NO)

        # OptionMenu for selecting pi algorithm
        self.__alpha_algorithm_var = StringVar(self)
        alpha_options = [item.name for item in AproximationAlgorithmType]
        self.__alpha_algorithm_var.set(alpha_options[conditions.get_approximation_algorithm().value])
        __opt_alpha_algorithm = OptionMenu(param_frame_alpha, self.__alpha_algorithm_var, *alpha_options)
        __opt_alpha_algorithm.pack(side=LEFT, fill=X, expand=YES, padx=12)

        # Frame for organizing widgets related to precision
        param_frame_precision = Frame(self, borderwidth=2, padx=10, pady=5)

        # Label for the precision
        lbl_precision = Label(param_frame_precision, text="Precision:")
        lbl_precision.pack(side=LEFT, fill=NONE, expand=NO)

        # Textbox for specifying the precision
        self.__txt_precision = Entry(param_frame_precision)
        self.__txt_precision.pack(side=LEFT, fill=NONE, expand=NO, padx=12)

        # Frame for save and cancel buttons
        buttons_frame = Frame(self, borderwidth=2, padx=10, pady=5)
        
        # Button for cancel
        btn_cancel = Button(buttons_frame, text="Cancel", command=self.__exit)
        btn_cancel.pack(side=RIGHT, fill=NONE, expand=NO, ipadx=2, padx=5)
        
        # Button for saving the changes
        btn_save = Button(buttons_frame, text="Save", command=self.__save)
        self.initial_focus = btn_save
        btn_save.pack(side=RIGHT, fill=NONE, expand=NO, ipadx=8, padx=5)

        # Making the frames visible
        param_frame_pi.pack(side=TOP, fill=X, expand=YES)
        param_frame_alpha.pack(side=TOP, fill=X, expand=YES)
        param_frame_precision.pack(side=TOP, fill=X, expand=YES)
        buttons_frame.pack(side=TOP, fill=X, expand=YES)

        # Filling the widgets with existing setting parameter values
        self.__txt_precision.delete(0, END)
        self.__txt_precision.insert(END, conditions.get_precision())

        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.__exit)
        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+50,
                                  self.parent.winfo_rooty()+50))
        
        self.initial_focus.focus_set()
        self.wait_window(self)


    def __save(self):
        """Saves the changes on the xml file"""
        try:
            precision = self.__txt_precision.get()
            self.__validate_input(precision)

            pi_algorithm = PiAlgorithmType[self.__pi_algorithm_var.get()]
            alpha_algorithm = AproximationAlgorithmType[self.__alpha_algorithm_var.get()]

            conditions = CalculationConditions(pi_algorithm, alpha_algorithm, int(precision))
            self.__settings = conditions
            self.__exit()
        except ValidationException as err:
            self.__handleError(err)


    def __validate_input(self, input_val):
        """Checks to see if the input value is valid or not. If invalid raise an exception"""
        try:
            number = int(input_val)
            if number <= 0 or number > 100:
                raise ValidationException("The entered number is not in the range. Please enter a number between 1 and 100.")
        except ValueError:
            raise ValidationException("The entered value is not a number. Please enter a number between 1 and 100.")


    def __handleError(self, errMessage):
        messagebox.showerror(title="Error", message=errMessage, parent=self)


    def __exit(self):
        self.destroy()


    def get_settings(self):
        return self.__settings
