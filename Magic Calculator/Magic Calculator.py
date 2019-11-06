from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.configure(bg='#bfbfbf')
root.title("Magic Calculator")
root.iconbitmap("calculator.ico")
myFont = font.Font(family='Arial', size=20, weight='bold')

def open1():
	global operator
	calc = Toplevel()
	myFont = font.Font(family='Arial', size=20, weight='bold')
	calc.title("Calculator")
	calc.iconbitmap("calculator.ico")
	calc.geometry("354x460")
	calclabel = Label(calc,text="CALCULATOR",bg='#bfbfbf')
	calclabel['font'] = myFont
	calclabel.pack(side=TOP)
	calc.config(background='#bfbfbf')

	textin=StringVar()
	operator= ""


	def clrbut():
		 global operator
		 textin.set('')
		 operator=""

	def clickbut(number):   #lambda:clickbut(1)
	     global operator
	     operator=operator+str(number)
	     textin.set(operator)

	def equlbut():
	     global operator
	     add=str(eval(operator))
	     textin.set(add)
	     operator=''
	def equlbut():
	     global operator
	     sub=str(eval(operator))
	     textin.set(sub)
	     operator=''     
	def equlbut():
	     global operator
	     mul=str(eval(operator))
	     textin.set(mul)
	     operator=''
	def equlbut():
	     global operator
	     div=str(eval(operator))
	     textin.set(div)
	     operator=""

	     
	metext = Entry(calc,textvar=textin,width=25,bd=5,bg='#d9d9d9')
	metext.pack()

	but1=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(1),text="1")
	but1.place(x=10,y=100)

	but2=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(2),text="2")
	but2.place(x=10,y=170)

	but3=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(3),text="3")
	but3.place(x=10,y=240)

	but4=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(4),text="4")
	but4.place(x=75,y=100)

	but5=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(5),text="5")
	but5.place(x=75,y=170)

	but6=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(6),text="6")
	but6.place(x=75,y=240)

	but7=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(7),text="7")
	but7.place(x=140,y=100)

	but8=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(8),text="8")
	but8.place(x=140,y=170)

	but9=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(9),text="9")
	but9.place(x=140,y=240)

	but0=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut(0),text="0")
	but0.place(x=10,y=310)

	butdot=Button(calc,padx=47,pady=14,bd=4,bg='#e6e6e6',command=lambda:clickbut("."),text=".")
	butdot.place(x=75,y=310)

	butpl=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',text="+",command=lambda:clickbut("+"))
	butpl.place(x=205,y=100)

	butsub=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',text="-",command=lambda:clickbut("-"))
	butsub.place(x=205,y=170)

	butml=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',text="*",command=lambda:clickbut("*"))
	butml.place(x=205,y=240)

	butdiv=Button(calc,padx=14,pady=14,bd=4,bg='#e6e6e6',text="/",command=lambda:clickbut("/"))
	butdiv.place(x=205,y=310)

	butclear=Button(calc,padx=14,pady=119,bd=4,bg='#e6e6e6',text="CE",command=clrbut)
	butclear.place(x=270,y=100)

	butequal=Button(calc,padx=151,pady=14,bd=4,bg='#e6e6e6',command=equlbut,text="=")
	butequal.place(x=10,y=380)
	calc.mainloop()

def open2():
	physics = Toplevel()
	physics.configure(bg='#bfbfbf')
	myFont = font.Font(family='Arial', size=20, weight='bold')
	physics.title("Physics")
	physics.geometry("235x285")
	physics.iconbitmap("calculator.ico")

	def openE():
		electric = Toplevel()
		electric.configure(bg='#bfbfbf')
		myFont = font.Font(family='Arial', size=20, weight='bold')
		electric.title("Electricity")
		electric.iconbitmap("calculator.ico")

		einfo = LabelFrame(electric, text="Here is some helpful information about Electricity.", padx=20, pady=20)
		einfo.grid(row=0,column=0, padx=5, pady=5)
		einfo.configure(bg='#bfbfbf')
		p_e1 = Label(einfo, text="Series Circuit - Electric circuit whose component parts are arranged end-to-end so that the current passes consecutively through each part.")
		p_e1.grid(row=0, column=0)
		p_e1.configure(bg='#bfbfbf')
		p_e2 = Label(einfo, text="Parallel Circuit - Component parts are connected as branches of main circuit so that current is divided among them.")
		p_e2.grid(row=1, column=0)
		p_e2.configure(bg='#bfbfbf')
		p_e3 = Label(einfo, text="Power - The electric energy expended per second.")
		p_e3.grid(row=2, column=0)
		p_e3.configure(bg='#bfbfbf')
		p_e4 = Label(einfo, text="UNIT for power - Watt")
		p_e4.grid(row=3, column=0)
		p_e4.configure(bg='#bfbfbf')
		p_e5 = Label(einfo, text="Define direct current - Current flowing in ONE direction.")
		p_e5.grid(row=4, column=0)
		p_e5.configure(bg='#bfbfbf')
		p_e6 = Label(einfo, text="3 components of an electric current - Battery, conductor, Load/resistance")
		p_e6.grid(row=5, column=0)
		p_e6.configure(bg='#bfbfbf')
		p_e7 = Label(einfo, text="Circuit device that must be connected in parallel - Voltmeter")
		p_e7.grid(row=6, column=0)
		p_e7.configure(bg='#bfbfbf')

		def powerc():
			currint = float(curr.get())
			voltint = float(volt.get())
			powera = voltint * currint
			global label1
			global watt
			label1 = Label(power, text=powera, bg='#bfbfbf')
			label1.grid(row=0,column=4)
			watt= Label(power, text="Watt", bg='#bfbfbf')
			watt.grid(row=0, column=5)

		def clrbut5():
			label1.destroy()
			watt.destroy()

		power = LabelFrame(electric, text="Power = Volatage * Current", padx=10, pady=10)
		power.grid(row=1,column=0)
		power.configure(bg='#bfbfbf')

		volt = Entry(power)
		volt.grid(row=0,column=0)
		volt.configure(bg='#bfbfbf')

		times = Label(power,text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		curr = Entry(power)
		curr.grid(row=0, column=2)
		curr.configure(bg='#bfbfbf')

		powere = Button(power, text="=", command=powerc)
		powere.grid(row=0,column=3)
		powere.configure(bg='#bfbfbf')

		clear5 = Button(power, text="Clr", command=clrbut5)
		clear5.grid(row=0,column=6)
		clear5.configure(bg='#bfbfbf')

		def volatagec():
			curr1f = float(curr1.get())
			resistance1f = float(resistance.get())
			volta = curr1f * resistance1f
			global label2
			global volts
			label2 = Label(voltage, text=volta, bg='#bfbfbf')
			label2.grid(row=0,column=4)
			volts= Label(voltage, text="Volts", bg='#bfbfbf')
			volts.grid(row=0, column=5)

		def clrbut4():
			label2.destroy()
			volts.destroy()

		voltage = LabelFrame(electric, text="Voltage = Current * Resistance", padx=10, pady=10)
		voltage.grid(row=2,column=0)
		voltage.configure(bg='#bfbfbf')

		curr1 = Entry(voltage)
		curr1.grid(row=0,column=0)
		curr1.configure(bg='#bfbfbf')

		times1 = Label(voltage,text="*")
		times1.grid(row=0,column=1)
		times1.configure(bg='#bfbfbf')

		resistance = Entry(voltage)
		resistance.grid(row=0, column=2)
		resistance.configure(bg='#bfbfbf')

		voltagee = Button(voltage, text="=", command=volatagec)
		voltagee.grid(row=0,column=3)
		voltagee.configure(bg='#bfbfbf')

		clear4 = Button(voltage, text="Clr", command=clrbut4)
		clear4.grid(row=0,column=6)
		clear4.configure(bg='#bfbfbf')

		def chargec():
			curr2f = float(curr2.get())
			time1f = float(time.get())
			chargea = curr2f * time1f
			global label3
			global coulombs
			label3 = Label(charge, text=chargea, bg='#bfbfbf')
			label3.grid(row=0,column=4)
			coulombs= Label(charge, text="Coulombs", bg='#bfbfbf')
			coulombs.grid(row=0, column=5)

		def clrbut3():
			label3.destroy()
			coulombs.destroy()

		charge = LabelFrame(electric, text="Charge = Current * Time", padx=10, pady=10)
		charge.grid(row=3,column=0)
		charge.configure(bg='#bfbfbf')

		curr2 = Entry(charge)
		curr2.grid(row=0,column=0)
		curr2.configure(bg='#bfbfbf')

		times1 = Label(charge,text="*")
		times1.grid(row=0,column=1)
		times1.configure(bg='#bfbfbf')

		time = Entry(charge)
		time.grid(row=0, column=2)
		time.configure(bg='#bfbfbf')

		chargee = Button(charge, text="=", command=chargec)
		chargee.grid(row=0,column=3)
		chargee.configure(bg='#bfbfbf')

		clear3= Button(charge, text="Clr", command=clrbut3)
		clear3.grid(row=0,column=6)
		clear3.configure(bg='#bfbfbf')

		def energyc():
			voltflt = float(voltage1.get())
			chargeflt = float(charge1.get())
			energya = voltflt * chargeflt
			global label4
			global joule1
			label4 = Label(energy, text=energya, bg='#bfbfbf')
			label4.grid(row=0,column=4)
			joule1 = Label(energy, text="Joules", bg='#bfbfbf')
			joule1.grid(row=0,column=5)

		def clrbut1():
			label4.destroy()
			joule1.destroy()

		energy = LabelFrame(electric, text="Energy = Voltage * Charge", padx=10, pady=10)
		energy.grid(row=4, column=0)
		energy.configure(bg='#bfbfbf')

		voltage1 = Entry(energy)
		voltage1.grid(row=0,column=0)
		voltage1.configure(bg='#bfbfbf')

		times = Label(energy, text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		charge1 = Entry(energy)
		charge1.grid(row=0,column=2)
		charge1.configure(bg='#bfbfbf')

		energye = Button(energy, text="=", command=energyc)
		energye.grid(row=0,column=3)
		energye.configure(bg='#bfbfbf')

		clear1 = Button(energy, text="Clr", command=clrbut1)
		clear1.grid(row=0, column=6)
		clear1.configure(bg='#bfbfbf')

		def energyc1():
			voltflt1 = float(voltage2.get())
			currflt1 = float(curr3.get())
			timeflt1 = float(time1.get())
			energya1 = voltflt1 * currflt1 * timeflt1
			global label5
			global joule2
			label5 = Label(energy1, text=energya1, bg='#bfbfbf')
			label5.grid(row=0,column=6)
			joule2 = Label(energy1, text="Joules", bg='#bfbfbf')
			joule2.grid(row=0,column=7)
		
		def clrbut2():
			label5.destroy()
			joule2.destroy()
		
		energy1 = LabelFrame(electric, text="Energy = Voltage * Current * Time", padx=10, pady=10)
		energy1.grid(row=5, column=0)
		energy1.configure(bg='#bfbfbf')

		voltage2 = Entry(energy1)
		voltage2.grid(row=0,column=0)
		voltage2.configure(bg='#bfbfbf')

		times = Label(energy1, text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		curr3 = Entry(energy1)
		curr3.grid(row=0,column=2)
		curr3.configure(bg='#bfbfbf')

		times1 = Label(energy1, text="*")
		times1.grid(row=0,column=3)
		times1.configure(bg='#bfbfbf')

		time1 = Entry(energy1)
		time1.grid(row=0,column=4)
		time1.configure(bg='#bfbfbf')

		energye1 = Button(energy1, text="=", command=energyc1)
		energye1.grid(row=0,column=5)
		energye1.configure(bg='#bfbfbf')


		clear2 = Button(energy1, text="Clr", command=clrbut2)
		clear2.grid(row=0, column=8)
		clear2.configure(bg='#bfbfbf')

	def openEn():
		energy = Toplevel()
		myFont = font.Font(family='Arial', size=20, weight='bold')
		energy.configure(bg='#bfbfbf')
		energy.title("Energy")
		energy.iconbitmap("calculator.ico")

		infoenergy= LabelFrame(energy, text="Here is some helpful information about this topic", padx=10, pady=10)
		infoenergy.grid(row=0,column=0,padx=5, pady=5)
		infoenergy.configure(bg='#bfbfbf')
		info1 = Label(infoenergy, text="Law of conservation of energy - Energy cannot be created or destroyed, it can only be converted from one form to another.")
		info1.grid(row=0,column=0)
		info1.configure(bg='#bfbfbf')
		info2 = Label(infoenergy, text="Joule - 1 joule is the amount of energy required to heat 1ml of water by 1 degree")
		info2.grid(row=1,column=0)
		info2.configure(bg='#bfbfbf')
		info3 = Label(infoenergy, text="Energy - Energy is the ability to do some work.")
		info3.grid(row=2,column=0)
		info3.configure(bg='#bfbfbf')
		info4 = Label(infoenergy, text="Work done = Energy transferred")
		info4.grid(row=3,column=0)
		info4.configure(bg='#bfbfbf')
		info5 = Label(infoenergy, text="Gravitational Potential Energy (GPE) - If you move upwards, you work against gravity.")
		info5.grid(row=4,column=0)
		info5.configure(bg='#bfbfbf')
		info6 = Label(infoenergy, text="Kinetic Energy - Kinetic energy is the type of energy moving objects contain.")
		info6.grid(row=5,column=0)
		info6.configure(bg='#bfbfbf')
		info7 = Label(infoenergy, text="Hydroelectric energy - Water flowing in a river has kinetic energy. Water stored in a reservoir flows down through pipes to drive turbines which turns generators, producing electrical energy.")
		info7.grid(row=6,column=0)
		info7.configure(bg='#bfbfbf')
		info8 = Label(infoenergy, text="Biomass energy - Biomass contains chemical potential energy which can be burned to release heat energy.")
		info8.grid(row=7,column=0)
		info8.configure(bg='#bfbfbf')
		info9 = Label(infoenergy, text="Geothermal energy - Some rocks under the Earth's surface are hot. Cold water pumped through these rocks become hot and turn in to steam which is used to generate electricity.")
		info9.grid(row=8,column=0)
		info9.configure(bg='#bfbfbf')
		info10 = Label(infoenergy, text="Solar energy - The Earth gets heat and light energy from the sun, which can be transferred into electrical energy to use in homes, using solar cells.")
		info10.grid(row=9,column=0)
		info10.configure(bg='#bfbfbf')

		def efficiencyc():
			usefulflt = float(useful.get())
			totalflt = float(total.get())
			effia= (usefulflt/totalflt)*100
			global label6
			global percentage
			label6 = Label(efficiency, text=effia, bg='#bfbfbf')
			label6.grid(row=0, column=8)
			percentage = Label(efficiency, text="%", bg='#bfbfbf')
			percentage.grid(row=0,column=9)

		def clrbutt():
			label6.destroy()
			percentage.destroy()

		efficiency = LabelFrame(energy, text="Efficiency = (Useful energy out/total energy out) * 100")
		efficiency.grid(row=1,column=0)
		efficiency.configure(bg='#bfbfbf')

		brack1 = Label(efficiency, text="(")
		brack1.grid(row=0, column=0)
		brack1.configure(bg='#bfbfbf')

		useful = Entry(efficiency)
		useful.grid(row=0,column=1)
		useful.configure(bg='#bfbfbf')

		divide = Label(efficiency, text="/")
		divide.grid(row=0,column=2)
		divide.configure(bg='#bfbfbf')

		total = Entry(efficiency)
		total.grid(row=0,column=3)
		total.configure(bg='#bfbfbf')

		brack2 = Label(efficiency, text=")")
		brack2.grid(row=0,column=4)
		brack2.configure(bg='#bfbfbf')

		times = Label(efficiency, text="*")
		times.grid(row=0,column=5)
		times.configure(bg='#bfbfbf')

		perc = Label(efficiency, text="100")
		perc.grid(row=0,column=6)
		perc.configure(bg='#bfbfbf')

		efficiencye = Button(efficiency, text="=", command=efficiencyc)
		efficiencye.grid(row=0,column=7)
		efficiencye.configure(bg='#bfbfbf')

		clrbutton = Button(efficiency, text="Clr", command=clrbutt)
		clrbutton.grid(row=0,column=10)
		clrbutton.configure(bg='#bfbfbf')

		def gpec():
			massflt = float(mass.get())
			gravityflt = float(gravity.get())
			heightflt = float(height.get())
			gpea = massflt * gravityflt * heightflt
			global label7
			global joule3
			label7 = Label(gpe, text=gpea, bg='#bfbfbf')
			label7.grid(row=0,column=6)
			joule3 = Label(gpe, text="Joules", bg='#bfbfbf')
			joule3.grid(row=0,column=7)
		
		def clrbutt2():
			label7.destroy()
			joule3.destroy()
		
		gpe = LabelFrame(energy, text="GPE = Mass * Gravity * Height", padx=10, pady=10)
		gpe.grid(row=2, column=0)
		gpe.configure(bg='#bfbfbf')

		mass = Entry(gpe)
		mass.grid(row=0,column=0)
		mass.configure(bg='#bfbfbf')

		times = Label(gpe, text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		gravity = Entry(gpe)
		gravity.insert(0, "9.832")
		gravity.grid(row=0,column=2)
		gravity.configure(bg='#bfbfbf')

		times1 = Label(gpe, text="*")
		times1.grid(row=0,column=3)
		times1.configure(bg='#bfbfbf')

		height = Entry(gpe)
		height.grid(row=0,column=4)
		height.configure(bg='#bfbfbf')

		gpee = Button(gpe, text="=", command=gpec)
		gpee.grid(row=0,column=5)
		gpee.configure(bg='#bfbfbf')

		clrbutton1 = Button(gpe, text="Clr", command=clrbutt2)
		clrbutton1.grid(row=0, column=8)
		clrbutton1.configure(bg='#bfbfbf')

		def kineticc():
			massflt = float(mass1.get())
			velocityflt = float(velocity.get())
			kinetica = 0.5 * massflt * (velocityflt * velocityflt)
			global label8
			global joule4
			label8 = Label(kinetic, text=kinetica, bg='#bfbfbf')
			label8.grid(row=0, column=7)
			joule4 = Label(kinetic, text="Joules", bg='#bfbfbf')
			joule4.grid(row=0, column=8)

		def clrbutto():
			label8.destroy()
			joule4.destroy()

		kinetic = LabelFrame(energy, text="Kinetic Energy = 0·5 * Mass * Velocity^2")
		kinetic.grid(row=3,column=0)
		kinetic.configure(bg='#bfbfbf')

		half = Label(kinetic, text="1/2")
		half.grid(row=0,column=0)
		half.configure(bg='#bfbfbf')

		times = Label(kinetic, text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		mass1 = Entry(kinetic)
		mass1.grid(row=0,column=2)
		mass1.configure(bg='#bfbfbf')

		times = Label(kinetic, text="*")
		times.grid(row=0,column=3)
		times.configure(bg='#bfbfbf')

		velocity = Entry(kinetic)
		velocity.grid(row=0,column=4)
		velocity.configure(bg='#bfbfbf')

		power2 = Label(kinetic, text="^2")
		power2.grid(row=0, column=5)
		power2.configure(bg='#bfbfbf')

		kinetice = Button(kinetic, text="=", command=kineticc)
		kinetice.grid(row=0, column=6)
		kinetice.configure(bg='#bfbfbf')

		clrbutt2 = Button(kinetic, text="Clr", command=clrbutto)
		clrbutt2.grid(row=0, column=9)
		clrbutt2.configure(bg='#bfbfbf')

		def workdonec():
			forceflt = float(force.get())
			distanceflt = float(distance.get())
			workdonea = forceflt * distanceflt
			global label9
			global joule5
			label9 = Label(workdone, text=workdonea, bg='#bfbfbf')
			label9.grid(row=0, column=4)
			joule5 = Label(workdone, text="Joules", bg='#bfbfbf')
			joule5.grid(row=0, column=5)

		def clrbutt():
			label9.destroy()
			joule5.destroy()

		workdone = LabelFrame(energy, text="Work done = Force * Distance")
		workdone.grid(row=4, column=0)
		workdone.configure(bg='#bfbfbf')

		force = Entry(workdone)
		force.grid(row=0, column=0)
		force.configure(bg='#bfbfbf')

		times = Label(workdone, text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		distance = Entry(workdone)
		distance.grid(row=0, column=2)
		distance.configure(bg='#bfbfbf')

		workdonee = Button(workdone, text="=", command=workdonec)
		workdonee.grid(row=0, column=3)
		workdonee.configure(bg='#bfbfbf')

		clrbut = Button(workdone,text="Clr", command=clrbutt)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def powerc():
			energyflt= float(energy22.get())
			timeflt= float(time.get())
			powera= energyflt/timeflt
			global label11
			global watt1
			label11= Label(power,text=powera, bg='#bfbfbf')
			label11.grid(row=0,column=4)
			watt1=Label(power,text="Joules", bg='#bfbfbf')
			watt1.grid(row=0, column=5)

		def clrbut():
			label11.destroy()
			watt1.destroy()

		power = LabelFrame(energy, text="Power = Energy/Time")
		power.grid(row=5, column=0)
		power.configure(bg='#bfbfbf')

		energy22= Entry(power)
		energy22.grid(row=0,column=0)
		energy22.configure(bg='#bfbfbf')

		divide= Label(power,text="/")
		divide.grid(row=0, column=1)
		divide.configure(bg='#bfbfbf')

		time= Entry(power)
		time.grid(row=0,column=2)
		time.configure(bg='#bfbfbf')

		powere= Button(power, text="=", command=powerc)
		powere.grid(row=0, column=3)
		powere.configure(bg='#bfbfbf')

		clrbut= Button(power, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def energyc22():
			shcflt= float(shc.get())
			mass2flt= float(mass2.get())
			changetflt= float(changet.get())
			energya= shcflt * mass2flt * changetflt
			global label12
			global joule6
			label12 = Label(energy1,text=energya, bg='#bfbfbf')
			label12.grid(row=0,column=6)
			joule6 = Label(energy1,text="Joules", bg='#bfbfbf')
			joule6.grid(row=0, column=7)

		def clrbut():
			label12.destroy()
			joule6.destroy()

		energy1= LabelFrame(energy, text="Energy = Specific heat capacity * Mass * Change in temperature")
		energy1.grid(row=6, column=0)
		energy1.configure(bg='#bfbfbf')

		shc = Entry(energy1)
		shc.grid(row=0,column=0)
		shc.configure(bg='#bfbfbf')

		times = Label(energy1,text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		mass2= Entry(energy1)
		mass2.grid(row=0,column=2)
		mass2.configure(bg='#bfbfbf')

		times = Label(energy1,text="*")
		times.grid(row=0, column=3)
		times.configure(bg='#bfbfbf')

		changet= Entry(energy1)
		changet.grid(row=0,column=4)
		changet.configure(bg='#bfbfbf')

		energye22 = Button(energy1, text="=", command=energyc22)
		energye22.grid(row=0, column=5)
		energye22.configure(bg='#bfbfbf')

		clrbut= Button(energy1, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=8)
		clrbut.configure(bg='#bfbfbf')


	def openF():
		forces = Toplevel()
		myFont = font.Font(family='Arial', size=20, weight='bold')
		forces.configure(bg='#bfbfbf')
		forces.title("Forces & Motion")
		forces.iconbitmap("calculator.ico")

		infoforces = LabelFrame(forces,text="Here is some helpful information about this topic", padx=10, pady=10)
		infoforces.grid(row=0,column=0, padx=5, pady=5)
		infoforces.configure(bg='#bfbfbf')

		info0= Label(infoforces, text="Scalar forces - Distance, Speed, Mass, Time, Volume, Temperature")
		info0.grid(row=0,column=0)
		info0.configure(bg='#bfbfbf')

		info1= Label(infoforces, text="Vector forces - Displacement, Velocity, Weight, Force")
		info1.grid(row=1,column=0)
		info1.configure(bg='#bfbfbf')

		info2= Label(infoforces, text="Scalar quantities - Scalar quantities have magnitude (size) only.")
		info2.grid(row=2,column=0)
		info2.configure(bg='#bfbfbf')

		info3= Label(infoforces, text="Vector quantities - Vector quantities have magnitude (size) and direction.")
		info3.grid(row=3,column=0)
		info3.configure(bg='#bfbfbf')

		info4= Label(infoforces, text="Forces that act at a distance - Magnetism, Electrostatic, Gravitational pull")
		info4.grid(row=4,column=0)
		info4.configure(bg='#bfbfbf')

		info5= Label(infoforces, text="Newton's first law - If forces are balanced then an object will remain stationary or will remain traveling at a constant speed.")
		info5.grid(row=5,column=0)
		info5.configure(bg='#bfbfbf')

		info6= Label(infoforces, text="Newton's second law - If forces are unbalanced then an object will accelerate, slow down or change direction.")
		info6.grid(row=6,column=0)
		info6.configure(bg='#bfbfbf')

		info7= Label(infoforces, text="Newton's third law - For every push force, there is a force the other way.")
		info7.grid(row=7,column=0)
		info7.configure(bg='#bfbfbf')

		info8= Label(infoforces, text="Pivot - A pivot is a point that an object can rotate around.")
		info8.grid(row=8,column=0)
		info8.configure(bg='#bfbfbf')

		info9= Label(infoforces, text="Moment - A moment is the turning effect of a force.")
		info9.grid(row=9,column=0)
		info9.configure(bg='#bfbfbf')

		info10= Label(infoforces, text="Lever - A lever is an object that can be used to increase the effect of the force on a pivot.")
		info10.grid(row=10,column=0)
		info10.configure(bg='#bfbfbf')


		def speedc():
			distanceflt= float(distance.get())
			timeflt= float(time.get())
			speeda= distanceflt/timeflt
			global labels
			global speedu
			labels=Label(speed,text=speeda, bg='#bfbfbf')
			labels.grid(row=0,column=4)
			speedu=Label(speed,text="m/s", bg='#bfbfbf')
			speedu.grid(row=0, column=5)

		def clrbut():
			labels.destroy()
			speedu.destroy()

		speed= LabelFrame(forces, text="Speed = Distance / Time")
		speed.grid(row=1, column=0)
		speed.configure(bg='#bfbfbf')

		distance= Entry(speed)
		distance.grid(row=0,column=0)
		distance.configure(bg='#bfbfbf')

		divide= Label(speed,text="/")
		divide.grid(row=0, column=1)
		divide.configure(bg='#bfbfbf')

		time= Entry(speed)
		time.grid(row=0,column=2)
		time.configure(bg='#bfbfbf')

		speede= Button(speed, text="=", command=speedc)
		speede.grid(row=0, column=3)
		speede.configure(bg='#bfbfbf')

		clrbut= Button(speed, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def forcec1():
			massflt= float(mass3.get())
			accelerationflt= float(acceleration.get())
			forcea1= accelerationflt * massflt
			global labelf1
			global newt
			labelf1= Label(force2,text=forcea1, bg='#bfbfbf')
			labelf1.grid(row=0,column=4)
			newt= Label(force2,text="Newtons", bg='#bfbfbf')
			newt.grid(row=0, column=5)

		def clrbut():
			labelf1.destroy()
			newt.destroy()

		force2= LabelFrame(forces, text="Force = Mass x Acceleration")
		force2.grid(row=2, column=0)
		force2.configure(bg='#bfbfbf')

		mass3= Entry(force2)
		mass3.grid(row=0,column=0)
		mass3.configure(bg='#bfbfbf')

		times= Label(force2,text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		acceleration= Entry(force2)
		acceleration.grid(row=0,column=2)
		acceleration.configure(bg='#bfbfbf')

		forcee1= Button(force2, text="=", command=forcec1)
		forcee1.grid(row=0, column=3)
		forcee1.configure(bg='#bfbfbf')

		clrbutt= Button(force2, text="Clr", command=clrbut)
		clrbutt.grid(row=0, column=6)
		clrbutt.configure(bg='#bfbfbf')

		def weightc():
			massflt= float(mass21.get())
			gravityflt= float(gravity.get())
			weighta=gravityflt * massflt
			global labelw
			global newtw
			labelw=Label(weight,text=weighta, bg='#bfbfbf')
			labelw.grid(row=0,column=4)
			newtw=Label(weight,text="Newtons", bg='#bfbfbf')
			newtw.grid(row=0, column=5)

		def clearbut():
			labelw.destroy()
			newtw.destroy()

		weight= LabelFrame(forces, text="Weight = Mass * Gravity")
		weight.grid(row=3, column=0)
		weight.configure(bg='#bfbfbf')

		mass21= Entry(weight)
		mass21.grid(row=0,column=0)
		mass21.configure(bg='#bfbfbf')

		times= Label(weight,text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		gravity= Entry(weight)
		gravity.grid(row=0,column=2)
		gravity.configure(bg='#bfbfbf')

		weighte= Button(weight, text="=", command=weightc)
		weighte.grid(row=0, column=3)
		weighte.configure(bg='#bfbfbf')

		clrbut= Button(weight, text="Clr", command=clearbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def momentc():
			massflt3= float(mass31.get())
			velocityflt= float(velocity.get())
			momenta=velocityflt * massflt3
			global labelm
			global momentu
			labelm=Label(moment12,text=momenta, bg='#bfbfbf')
			labelm.grid(row=0,column=4)
			momentu=Label(moment12,text="kg⋅m/s", bg='#bfbfbf')
			momentu.grid(row=0, column=5)

		def clearbutt():
			labelm.destroy()
			momentu.destroy()

		moment12= LabelFrame(forces, text="Momentum = Mass x Velocity.")
		moment12.grid(row=4, column=0)
		moment12.configure(bg='#bfbfbf')

		mass31= Entry(moment12)
		mass31.grid(row=0,column=0)
		mass31.configure(bg='#bfbfbf')

		times= Label(moment12,text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		velocity= Entry(moment12)
		velocity.grid(row=0,column=2)
		velocity.configure(bg='#bfbfbf')

		momente= Button(moment12, text="=", command=momentc)
		momente.grid(row=0, column=3)
		momente.configure(bg='#bfbfbf')

		clrbutt1= Button(moment12, text="Clr", command=clearbutt)
		clrbutt1.grid(row=0, column=6)
		clrbutt1.configure(bg='#bfbfbf')

		def densityc():
			massflt= float(mass.get())
			volumeflt= float(volume.get())
			densitya=massflt/volumeflt
			global labeld
			global densityu
			labeld=Label(density,text=densitya, bg='#bfbfbf')
			labeld.grid(row=0,column=4)
			densityu=Label(density,text="kg/m^3", bg='#bfbfbf')
			densityu.grid(row=0, column=5)

		def clrbut():
			labeld.destroy()
			densityu.destroy()

		density= LabelFrame(forces, text="Density = Mass / Volume")
		density.grid(row=5, column=0)
		density.configure(bg='#bfbfbf')

		mass= Entry(density)
		mass.grid(row=0,column=0)
		mass.configure(bg='#bfbfbf')

		divide= Label(density,text="/")
		divide.grid(row=0, column=1)
		divide.configure(bg='#bfbfbf')

		volume= Entry(density)
		volume.grid(row=0,column=2)
		volume.configure(bg='#bfbfbf')

		densitye= Button(density, text="=", command=densityc)
		densitye.grid(row=0, column=3)
		densitye.configure(bg='#bfbfbf')

		clrbut= Button(density, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def pressurec():
			forceflt2= float(force5.get())
			areaflt= float(area.get())
			pressurea= forceflt2/areaflt
			global labelp
			global pressureu
			labelp=Label(pressure,text=pressurea, bg='#bfbfbf')
			labelp.grid(row=0,column=4)
			pressureu=Label(pressure,text="Pascals", bg='#bfbfbf')
			pressureu.grid(row=0, column=5)

		def clrbut():
			labelp.destroy()
			pressureu.destroy()

		pressure= LabelFrame(forces, text="Pressure = Force / Area. ")
		pressure.grid(row=6, column=0)
		pressure.configure(bg='#bfbfbf')

		area= Entry(pressure)
		area.grid(row=0,column=0)
		area.configure(bg='#bfbfbf')

		divide= Label(pressure,text="/")
		divide.grid(row=0, column=1)
		divide.configure(bg='#bfbfbf')

		force5= Entry(pressure)
		force5.grid(row=0,column=2)
		force5.configure(bg='#bfbfbf')

		pressuree= Button(pressure, text="=", command=pressurec)
		pressuree.grid(row=0, column=3)
		pressuree.configure(bg='#bfbfbf')

		clrbut= Button(pressure, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')

		def momentc():
			forceflt= float(force.get())
			pivotflt= float(pivot.get())
			momenta=pivotflt*forceflt
			global labelmo
			global momentun
			labelmo=Label(moment,text=momenta, bg='#bfbfbf')
			labelmo.grid(row=0,column=4)
			momentun=Label(moment,text="Newton Metres", bg='#bfbfbf')
			momentun.grid(row=0, column=5)

		def clrbut():
			labelmo.destroy()
			momentun.destroy()

		moment= LabelFrame(forces, text="Moment = Force * Perpendicular distance from pivot.")
		moment.grid(row=7, column=0)
		moment.configure(bg='#bfbfbf')

		force= Entry(moment)
		force.grid(row=0,column=0)
		force.configure(bg='#bfbfbf')

		times= Label(moment,text="*")
		times.grid(row=0, column=1)
		times.configure(bg='#bfbfbf')

		pivot= Entry(moment)
		pivot.grid(row=0,column=2)
		pivot.configure(bg='#bfbfbf')

		momente= Button(moment, text="=", command=momentc)
		momente.grid(row=0, column=3)
		momente.configure(bg='#bfbfbf')

		clrbut= Button(moment, text="Clr", command=clrbut)
		clrbut.grid(row=0, column=6)
		clrbut.configure(bg='#bfbfbf')


	def openW():
		waves = Toplevel()
		myFont = font.Font(family='Arial', size=20, weight='bold')
		waves.configure(bg='#bfbfbf')
		waves.title("Waves")
		waves.iconbitmap("calculator.ico")

		infowaves = LabelFrame(waves, text="Here is some helpful information about this topic", padx=10, pady=10)
		infowaves.grid(row=0, column=0, padx=5, pady=5)
		infowaves.configure(bg='#bfbfbf')
		info1 = Label(infowaves, text="Electromagnetic Waves - waves that travel through a vacuum at 300,000,000 m/s")
		info1.grid(row=0,column=0)
		info1.configure(bg='#bfbfbf')
		info2 = Label(infowaves, text="Longitudinal Wave - oscillations are parallel to direction of energy transfer")
		info2.grid(row=1,column=0)
		info2.configure(bg='#bfbfbf')
		info3 = Label(infowaves, text="Transverse Wave - oscillations are perpendicular to direction of energy transfer")
		info3.grid(row=2,column=0)
		info3.configure(bg='#bfbfbf')
		info4 = Label(infowaves, text="Compression - part of a longitudinal wave where the particles are closer together")
		info4.grid(row=3,column=0)
		info4.configure(bg='#bfbfbf')
		info5 = Label(infowaves, text="Rarefaction - part of a longitudinal wave where the particles are further apart")
		info5.grid(row=4,column=0)
		info5.configure(bg='#bfbfbf')
		info6 = Label(infowaves, text="Amplitude - height of a wave measured from equilibrium position to peak or trough")
		info6.grid(row=5,column=0)
		info6.configure(bg='#bfbfbf')
		info7 = Label(infowaves, text="Wavelength - distance from one peak to another")
		info7.grid(row=6,column=0)
		info7.configure(bg='#bfbfbf')
		info8 = Label(infowaves, text="Frequency - number of wave crests passing a point each second")
		info8.grid(row=7,column=0)
		info8.configure(bg='#bfbfbf')
		info9 = Label(infowaves, text="1 Hertz - 1 wavelength per second")
		info9.grid(row=8,column=0)
		info9.configure(bg='#bfbfbf')
		info10 = Label(infowaves, text="Period - time taken for one complete wave to pass")
		info10.grid(row=9,column=0)
		info10.configure(bg='#bfbfbf')


		def velocityc():
			frequencyflt = float(frequency.get())
			wavelengthflt = float(wavelength.get())
			velocitya = frequencyflt * wavelengthflt
			global label
			global ms
			label = Label(velocity, text=velocitya, bg='#bfbfbf')
			label.grid(row=0,column=4)
			ms = Label(velocity, text="M/S", bg='#bfbfbf')
			ms.grid(row=0,column=5)

		def clrbut():
			label.destroy()
			ms.destroy()

		velocity = LabelFrame(waves, text="Velocity = Frequency * Wavelength", padx=10, pady=10)
		velocity.grid(row=1, column=0)
		velocity.configure(bg='#bfbfbf')

		frequency = Entry(velocity)
		frequency.grid(row=0,column=0)
		frequency.configure(bg='#bfbfbf')

		times = Label(velocity, text="*")
		times.grid(row=0,column=1)
		times.configure(bg='#bfbfbf')

		wavelength = Entry(velocity)
		wavelength.grid(row=0,column=2)
		wavelength.configure(bg='#bfbfbf')

		velocitye = Button(velocity, text="=", command=velocityc)
		velocitye.grid(row=0,column=3)
		velocitye.configure(bg='#bfbfbf')

		clear = Button(velocity, text="Clr", command=clrbut)
		clear.grid(row=0, column=6)
		clear.configure(bg='#bfbfbf')


	menu = Menu(physics)
	physics.config(menu=menu)

	subMenu = Menu(physics)
	menu.add_cascade(label="       Physics Topics       ", menu=subMenu)
	subMenu.add_command(label="Electricity", command=openE)
	subMenu.add_command(label="Energy", command=openEn)
	subMenu.add_command(label="Forces & Motion", command=openF)
	subMenu.add_command(label="Waves", command=openW)


calculator = Button(root, text="Calculator", command=open1, padx=80, pady=40, bg='#bfbfbf')
calculator['font'] = myFont
calculator.grid(row=0, column=0)
calc_img = ImageTk.PhotoImage(Image.open("magic.png"))
my_calc = Label(image=calc_img, bg='#bfbfbf')
my_calc.grid(row=1, column=0)

physics = Button(root, text="Physics", command=open2, padx=95, pady=40, bg='#bfbfbf')
physics['font'] = myFont
physics.grid(row=0, column=1)
phys_img = ImageTk.PhotoImage(Image.open("physics.png"))
my_phys = Label(image=phys_img, bg='#bfbfbf')
my_phys.grid(row=1, column=1)


root.mainloop()