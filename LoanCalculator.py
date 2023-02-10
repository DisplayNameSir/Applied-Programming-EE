# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:56:49 2020

Reference: https://www.geeksforgeeks.org/python-loan-calculator-using-tkinter/?ref=rp
"""
# Import tkinter
from tkinter import *
class LoanCalculator:

	def __init__(self):

		window = Tk() # Create a window
		window.title("Loan Calculator") # Set title
        
		# create the input boxes.
		Label(window, text = "Annual %Interest Rate").grid(row = 1, column = 1, sticky = W)
		Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
		Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
		Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
		Label(window, text = "Total Interest Paid").grid(row = 5, column = 1, sticky = W) #Rearranged calculator to display total interest before total payment
        #Printed additional tab that will soon display the Total Interest Paid during the duration of the loan
		Label(window, text = "Total Payment").grid(row = 6, column = 1, sticky = W)

		# for taking inputs
        #Annual Interest Input
		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)
        
        #Number of years to pay loan input
		self.numberOfYearsVar = StringVar()

        #Accepted loan from bank
		Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
		self.loanAmountVar = StringVar()

        #Monthly Loan Amount with displayed amount paid each month during duration of loan
		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)

        #Total Payment Display
		self.totalPaymentVar = StringVar()
		lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 6, column = 2, sticky = E)

        #Total Interest Paid Display
		self.totalInterestPaidVar = StringVar()
		lblTotalInterest = Label(window, textvariable = self.totalInterestPaidVar).grid(row = 5, column = 2, sticky = E)

		# create the button
		btComputePayment = Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 7, column = 2, sticky = E)
		window.mainloop() # Create an event loop

	# compute the total payment.
	def computePayment(self):

		monthlyPayment = self.getMonthlyPayment(
		float(self.loanAmountVar.get()),
		float(self.annualInterestRateVar.get()) / 1200,
		int(self.numberOfYearsVar.get()))

        #Equations used to calculate total and total interest
		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        
        #Modified Total Payment to also include loan amount 
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get()) + int(self.loanAmountVar.get())

		self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
        #Replaced Interest Paid with Total Payment Equation
		InterestPaid = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        
		self.totalInterestPaidVar.set(format(InterestPaid, '10.2f'))
        
    # Equation used to calculate to apply the interest rate to the loan amount and time it took to pay the loan
	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
		# compute the monthly payment.
		monthlyPayment = loanAmount * monthlyInterestRate / (1
		- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
		return monthlyPayment;
    

		root = Tk() # create the widget
        
# call the class to run the program.
LoanCalculator()
