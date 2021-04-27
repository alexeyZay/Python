import tkinter as tk
from tkinter import ttk

class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0, sticky='news') # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = tk.Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = tk.Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky='snwe')
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = tk.Frame(self._canvas, bg='red')
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=2) # changed
        self.rowconfigure(0, weight=2) # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)
        self._canvas.bind('<Configure>', self.frame_width)

    def frame_width(self, event):
        # resize inner frame to canvas size
        canvas_width = event.width
        self._canvas.itemconfig(self._window, width = canvas_width)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

class Question:

    def __init__(self, parent, question,question_key):
        self.parent = parent
        self.question = question
        self.question_key = question_key
        self.create_widgets_inside()
        #self.answer=self.get_input()

    def create_widgets_inside(self):
        self.labelframe = tk.LabelFrame(self.parent, text=self.question_key)
        self.labelframe.pack(fill="both", expand=True)
        # self.labelframe.pack(fill="both", expand=True)

        self.label = tk.Label(self.labelframe, text=self.question,anchor='nw',justify='left')
        self.label.pack(expand=True, fill='both',side='left')

        self.entry = tk.Entry(self.labelframe,width='5',bd='3')
        self.entry.pack(side='right',padx='10')


# --- main ---

root = tk.Tk()
root.title("Seniority")
root.geometry("600x600")
questions = {
    "User_Name":"",
    "experience (years)": "",

    "General knowledge of testing types / tecniques": "Knowledge about software testing/testing approaches\nTesting expertise (ability to test independently,without help and control)\n* bugs\n* small features\n* features with not significant or without affected area",

    "": "* testing app as end user - focus on the user satisfaction (mid/senior)\n* deep issue investigation (mid/senior)",

    " Analytical skills": "",

    "Problem solving skills": "",

    "Manual testing skills": "Experience in:\n* manual testing\n* composing test scenarios of varios types\n* performance testing (not required)",

    "": "* testing app as end user - focus on the user satisfaction\n* deep issue investigation ",

    "Programming / automation skills": "\n* knowledge of programming language, testing tools (basic - mid / good - senior)\n* the ability to review automation (code / test cases) - senior / sdet middle",

    "Testing documentation": "\n* creation of test cases / plans / checklists\n* no strong need in review - middle\n* review skills - mid/senior",

    "Communication": "\n* answer certain questions during meetings\n* comment tasks\n* compose short emails (with certain answers)",

    "": "\n* voise / email / chat - strong skills required for senior/lead/manager\n* effective communication with devs - middle\n* negotiation skill - senior/lead/manager",

    "Work with tasks & issues": "Ability to follow certain plan while testing\n* big features\n* epics\n* performance testing",

    "": "* requirements review/analysis (mid/senior)\n* suggestions for improvements (mid/senior)\n* filing issues\n* identification of severity priority\n* estimation",

    "Work with testing environment": "\n* set up testing environment (mid)\n* identify requirements in advance, request needed resources (senior)",

    "Self-service in investigation of new systems / technologies": "Detail oriented",

    "CI / CD process understanding": "\n* theory\n* practice",

    "Customer support": "\n* investigation\n* asking qustions\n* giving advices",

    "Time management": "\n* fit timelines (mid)\n* plan work for team (senior/manager)",

    "Risk Management": "\n* issue (mid)\n* sprint (mid/senior)\n* release (senior/manager)\n* people (senior/manager)",

    "Mentoring": "\n* senior/manager",

    "Constant learning": "\n* cources/books",

    "Team Management": "\n* pro-activity\n* test strategy (senior/manager)\n* metrics for QA/team (senior/manager)\n* visability (senior/manager)\n* solving problems (senior/manager)\n* delegation (senior/manager)\n* optimization of processes (senior/manager)"
}
def get_input(*args):
    pass
    #value = self.entry.get()
    #if value:
    #    return value
    # print('value:', value)
    # if value == self.answer:
    #     print("Esatto. è " + self.answer)
    #     self.label['text'] = "Esatto"®
button = tk.Button(root, text="Calculate", command=get_input,bg='red',width='15')
button.config
button.pack(side='bottom',anchor='e', padx='18')
list_of_questions_keys = list(questions)
list_of_questions_values = list(questions.values())
window = ScrolledFrame(root)
window.pack(expand=True, fill='both')
counter=0
for i in range(len(list_of_questions_keys)):
    Question(window.inner, list_of_questions_values[counter],list_of_questions_keys[counter])
    counter+=1
root.mainloop()