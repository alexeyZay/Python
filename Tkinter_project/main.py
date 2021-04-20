from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Get_Senoirity")
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)
# new wiget main frame
mainframe = Canvas(root)
# showing mainframe
mainframe.pack()
Can1 = Canvas(root, bg="Yellow")
Can1.pack()
vsbar = Scrollbar(Can1, orient="vertical", command=mainframe.yview)
vsbar.pack()

Can1.configure(yscrollcommand=vsbar.set, scrollregion=Can1.bbox("all"))
questions = {
    "experience (years)": "",

    "General knowledge of testing types / tecniques": "Knowledge about software testing/testing approaches\nTesting expertise (ability to test independently,\nwithout help and control) \n* bugs \n* small features \n* features with not significant or without affected area",

    "": "* testing app as end user - focus on the user satisfaction (mid/senior)\n* deep issue investigation (mid/senior)",

    " Analytical skills": "",

    "Problem solving skills": "",

    "Manual testing skills": "Experience in:\n* manual testing\n* composing test scenarios of varios types\n* performance testing (not required)",

    "": "* testing app as end user - focus on the user satisfaction\n* deep issue investigation ",

    "Programming / automation skills": "* knowledge of programming language, testing tools (basic - mid / good - senior)\n* the ability to review automation (code / test cases) - senior / sdet middle",

    "Testing documentation": "* creation of test cases / plans / checklists\n* no strong need in review - middle\n* review skills - mid/senior",

    "Communication": "* answer certain questions during meetings\n* comment tasks\n* compose short emails (with certain answers)",

    "": "* voise / email / chat - strong skills required for senior/lead/manager\n* effective communication with devs - middle\n* negotiation skill - senior/lead/manager",

    "Work with tasks & issues": "Ability to follow certain plan while testing\n* big features\n* epics\n* performance testing",

    "": "* requirements review/analysis (mid/senior)\n* suggestions for improvements (mid/senior)\n* filing issues\n* identification of severity priority\n* estimation",

    "Work with testing environment": "* set up testing environment (mid)\n* identify requirements in advance, request needed resources (senior)",

    "Self-service in investigation of new systems / technologies": "Detail oriented",

    "CI / CD process understanding": "* theory\n* practice",

    "Customer support": "* investigation\n* asking qustions\n* giving advices",

    "Time management": "* fit timelines (mid)\n* plan work for team (senior/manager)",

    "Risk Management": "* issue (mid)\n* sprint (mid/senior)\n* release (senior/manager)\n* people (senior/manager)",

    "Mentoring": "* senior/manager",

    "Constant learning": "* cources/books",

    "Team Management": "\n* pro-activity\n* test strategy (senior/manager)\n* metrics for QA/team (senior/manager)\n* visability (senior/manager)\n* solving problems (senior/manager)\n* delegation (senior/manager)\n* optimization of processes (senior/manager)"
}
#
# list_of_questions_keys = list(questions)
# list_of_questions_values = list(questions.values())
#
# ttk.Label(mainframe.grid(column=1, row=2, sticky=E), text=(list_of_questions_keys[0]))
# text1 = Text(mainframe, width=6, height=1)
# text1.insert(INSERT, list_of_questions_values[0])
# text1.grid(column=2, row=2, sticky=(W, E))
# ttk.Label(mainframe, text=(list_of_questions_keys[1])).grid(column=1, row=3, sticky=E)
# text2 = Text(mainframe, width=60, height=6)
# text2.insert(INSERT, list_of_questions_values[1])
# text2.grid(column=2, row=3, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[2]).grid(column=1, row=4, sticky=E)
# text3 = Text(mainframe, width=60, height=6)
# text3.insert(INSERT, list_of_questions_values[2])
# text3.grid(column=2, row=4, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[3]).grid(column=1, row=5, sticky=E)
# text4 = Text(mainframe, width=60, height=6)
# text4.insert(INSERT, list_of_questions_values[3])
# text4.grid(column=2, row=5, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[4]).grid(column=1, row=6, sticky=E)
# text5 = Text(mainframe, width=60, height=6)
# text5.insert(INSERT, list_of_questions_values[4])
# text5.grid(column=2, row=6, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[5]).grid(column=1, row=7, sticky=E)
# text6 = Text(mainframe, width=60, height=6)
# text6.insert(INSERT, list_of_questions_values[5])
# text6.grid(column=2, row=7, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[6]).grid(column=1, row=8, sticky=E)
# text7 = Text(mainframe, width=60, height=6)
# text7.insert(INSERT, list_of_questions_values[6])
# text7.grid(column=2, row=8, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[7]).grid(column=1, row=9, sticky=E)
# text8 = Text(mainframe, width=60, height=6)
# text8.insert(INSERT, list_of_questions_values[7])
# text8.grid(column=2, row=9, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[8]).grid(column=1, row=10, sticky=E)
# text9 = Text(mainframe, width=60, height=6)
# text9.insert(INSERT, list_of_questions_values[8])
# text9.grid(column=2, row=10, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[9]).grid(column=1, row=11, sticky=E)
# text10 = Text(mainframe, width=60, height=6)
# text10.insert(INSERT, list_of_questions_values[9])
# text10.grid(column=2, row=11, sticky=(W, E))
# ttk.Label(mainframe, text=list_of_questions_keys[10]).grid(column=1, row=12, sticky=E)
# text11 = Text(mainframe, width=60, height=6)
# text11.insert(INSERT, list_of_questions_values[10])
# text11.grid(column=2, row=12, sticky=(W, E))
# ttk.Button(mainframe, text="^", command=quit).grid(column=3, row=2, sticky=E)
#
# meters = StringVar()
#
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# root.bind("<Return>", next_question)
mainframe.mainloop()
root.mainloop()
