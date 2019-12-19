
# import keyboard as k
from tkinter import *



# def PrintName(event):
# 	print("Hi this is Fatima")

# button1 = Button(root, text = "printmyname", bg = "yellow", fg = "blue")
# button1.bind("<Button-1>", PrintName)

# # button1 = Button(root, text = "printmyname", bg = "yellow", fg = "blue", command = PrintName)
# button1.pack(side = LEFT, fill = Y)

# label1 = Label(root, text = "Name")
# label2 = Label(root, text = "Password")
# entry1 = Entry(root)
# entry2 = Entry(root)
# label1.grid(row = 0, column = 0, sticky = E) #column is always 0 by default
# label2.grid(row = 1, sticky = E) #column is always 0 by default
# entry1.grid(row = 0, column = 1)
# entry2.grid(row = 1, column = 1)

# c = Checkbutton(root, text = "Keep me logged in")
# c.grid(columnspan = 2) #will take 2 columns 

# label1  = Label(root, text = "Label 1", bg = "yellow", fg = "blue")
# label1.pack()
# label2 = Label(root, text = "Label 2", bg = "green", fg = "black")
# label2.pack(fill = X)
# label3 = Label(root, text = "Label 3", bg = "blue", fg = "white")
# label3.pack(side = LEFT, fill = Y)


# topFrame = Frame(root)
# topFrame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side = BOTTOM) #Pack from bottom

# button1 = Button(topFrame, text = "Button1Click", fg = "red")
# button2 = Button(topFrame, text = "Button2Click", fg = "blue")
# button3 = Button(topFrame, text = "Button3Click", fg = "green")
# button4 = Button(bottomFrame, text = "Button4Click", fg = "purple")
# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)
# button4.pack()

# label = Label(root, text = "new label")
# label.pack() #Just pack it in there 

# root.mainloop() #run an infinite loop on root so it continuously displays; doesn't flash for a split second


class AtpGui:
	__premiseList = None
	__conclusion = None    

	__root = None
	__enterPremiseLabel = None
	__enterConclusionLabel = None
	__outputLabel  = None
	__entryPremise = None
	__entryConclusion = None
	__addPremiseButton = None
	__addConclusionButton = None
	# __outputSText = None


	def __init__(self):
		self.__premiseList = []

		self.__root = Tk()
		self.__root.title("Automated Theorem Proving")
		self.__root.configure(bg = "light blue")

		self.__outputLabel = Label(self.__root, text = "Output :", bg = "white", fg = "blue")
		self.__outputLabel.grid(row = 2, column = 0, sticky = E)

		self.__enterPremiseLabel = Label(self.__root, text = "Enter Premise :", bg = "white", fg = "blue")
		self.__enterPremiseLabel.grid(row = 0, column = 0, sticky = E)

		self.__enterConclusionLabel = Label(self.__root, text = "Enter Conclusion :", bg = "white", fg = "blue")
		self.__enterConclusionLabel.grid(row = 1, column = 0, sticky = E)

		self.__entryPremise = Entry(self.__root)
		self.__entryPremise.grid(row = 0, column = 1)

		self.__entryConclusion = Entry(self.__root)
		self.__entryConclusion.grid(row = 1, column = 1)

		self.__addPremiseButton = Button(self.__root, text = "Add Premise", bg = "white", fg = "black")
		self.__addPremiseButton.grid(row = 0, column = 2, sticky = W)

		self.__addConclusionButton = Button(self.__root, text = "Add Conclusion", bg = "white", fg = "black")
		self.__addConclusionButton.grid(row = 1, column = 2, sticky = W)

		# self.__outputSText = ScrolledText(root)
		# self.__outputSText.grid(row = 2, column = 1)

		self.__root.mainloop() #run an infinite loop on root so it continuously displays; doesn't flash for a split second


	def TakeInput(self):
		premiseEntered = False
		conclusionEntered = False
		premise = None
		while (not premiseEntered):
				premise = input("Add premise > ")
				if premise == "c":
					premiseEntered = True
				else:
					self.__premiseList.append(premise)
				print(self.__premiseList)
		self.__conclusion = input("Enter conclusion > ")


atpgui = AtpGui()
atpgui.TakeInput()



