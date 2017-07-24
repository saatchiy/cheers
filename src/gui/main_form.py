from tkinter import *
import sys
from src.overlap_calculator.overlap_calculator import OverlapCalculator

class MainForm:

    def __init__(self):
        self.__radius = -1
        self.__result = ""
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


    def __compute(self):
        radius_str = self.__txt_radius.get("1.0", END)
        
        if self.__validate_input(radius_str):
            self.__radius = mpf(radius_str)
            length = OverlapCalculator.calculate_overlapping_length(self.__radius)


    def display(self):
        self.__main_form.mainloop()

    def __change_settings(self):
        pass

    def __save(self):
        pass

    def __exit(self):
        sys.exit()
