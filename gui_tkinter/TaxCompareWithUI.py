import tkinter as tk
from tkinter import messagebox

# Function to handle the input collection and tax calculation
def collect_values():
    try:
        # Retrieve values from UI
        gross_salary = float(entry_gross_salary.get())
        professional_tax = float(entry_professional_tax.get())
        
        section_80c = float(entry_section_80c.get())
        section_80ccc = float(entry_section_80ccc.get())
        section_80ccd_1 = float(entry_section_80ccd_1.get())
        
        section_80ccd_1b = float(entry_section_80ccd_1b.get())
        section_80ccg = float(entry_section_80ccg.get())
        
        section_80d = float(entry_section_80d.get())
        section_80dd = float(entry_section_80dd.get())
        section_80ddb = float(entry_section_80ddb.get())
        section_80e = float(entry_section_80e.get())
        section_80ee = float(entry_section_80ee.get())
        section_80eea = float(entry_section_80eea.get())
        section_80gg = float(entry_section_80gg.get())
        section_80gga = float(entry_section_80gga.get())
        section_80ggb = float(entry_section_80ggb.get())
        section_80ggc = float(entry_section_80ggc.get())
        section_80u = float(entry_section_80u.get())
        section_80qqb = float(entry_section_80qqb.get())
        section_80rrb = float(entry_section_80rrb.get())
        section_80tta = float(entry_section_80tta.get())

        allowances_u_s_10 = float(entry_allowances_u_s_10.get())

        # Gross Salary Old
        gross_salary_new = gross_salary
        # Deduct Standard Deductoin 
        standard_deduction = 50000
        gross_salary -= standard_deduction
        # Apply deductions to the gross salary, after applying limits for each section
        gross_salary -= professional_tax  # Professional tax
        
        # 80C, 80CCC, 80CCD(1) combined limit: ₹1,50,000
        total_80c_deductions = min(section_80c + section_80ccc + section_80ccd_1, 150000)
        gross_salary -= total_80c_deductions
        
        # 80CCD(1B) additional NPS contribution: ₹50,000
        gross_salary -= min(section_80ccd_1b, 50000)
        
        # 80D: ₹25,000 (₹50,000 for senior citizens)
        gross_salary -= min(section_80d, 25000)
        
        # 80DD, 80DDB, 80E, 80EE, 80EEA, 80GG, 80GGA, 80GGB, 80GGG, 80U, 80CCG, 80QQB, 80RRB, 80TTA: No limits for deductions
        gross_salary -= section_80dd
        gross_salary -= section_80ddb
        gross_salary -= section_80e
        gross_salary -= section_80ee
        gross_salary -= section_80eea
        gross_salary -= section_80gg
        gross_salary -= section_80gga
        gross_salary -= section_80ggb
        gross_salary -= section_80ggc
        gross_salary -= section_80u
        gross_salary -= section_80ccg
        gross_salary -= section_80qqb
        gross_salary -= section_80rrb
        gross_salary -= section_80tta
        
        # Deduction under Section 10 (Allowances under section 10)
        gross_salary -= allowances_u_s_10

        # Calculate taxable income and apply tax slabs
        taxable_income = gross_salary

        # Tax slabs for the Old Regime
        slab_1_limit = 250000  # Up to ₹2.5 lakh: No tax
        slab_2_limit = 500000  # ₹2.5 lakh to ₹5 lakh: 5%
        slab_3_limit = 1000000  # ₹5 lakh to ₹10 lakh: 20%
        slab_4_limit = float('inf')  # Above ₹10 lakh: 30%

        # Tax rates
        rate_1 = 0.05  # 5% tax for income between ₹2.5 lakh and ₹5 lakh
        rate_2 = 0.20  # 20% tax for income between ₹5 lakh and ₹10 lakh
        rate_3 = 0.30  # 30% tax for income above ₹10 lakh

        # Section 80C Limit: ₹1,50,000 (combined limit for 80C, 80CCC, and 80CCD)
        section_80c_limit = 150000
        section_80ccc_limit = 150000
        section_80ccd_1_limit = 150000

        # Section 80CCD(1B) Limit: ₹50,000 (additional NPS contribution)
        section_80ccd_1b_limit = 50000

        # Section 80D Limit: ₹25,000 (₹50,000 for senior citizens)
        section_80d_limit = 25000
        section_80d_senior_limit = 50000

        # Section 80EE and 80EEA Limits: ₹50,000 (each for home loan interest)
        section_80ee_limit = 50000
        section_80eea_limit = 50000

        # Section 80GG Limit: ₹5,000 per month (for rent paid without receiving HRA)
        section_80gg_limit = 5000

        # Function to calculate tax based on slabs
        def calculate_old_tax(taxable_income):
            tax = 0
            if taxable_income <= slab_1_limit:
                return tax
            if taxable_income <= slab_2_limit:
                tax += (taxable_income - slab_1_limit) * rate_1
                return tax
            if taxable_income <= slab_3_limit:
                tax += (slab_2_limit - slab_1_limit) * rate_1
                tax += (taxable_income - slab_2_limit) * rate_2
                return tax
            tax += (slab_2_limit - slab_1_limit) * rate_1
            tax += (slab_3_limit - slab_2_limit) * rate_2
            tax += (taxable_income - slab_3_limit) * rate_3
            return tax

        # Calculate tax
        tax = calculate_old_tax(taxable_income)

        # Apply rebate under Section 87A (if applicable) - Available for taxable income less than ₹5 lakh
        if taxable_income <= 500000:
            tax -= 12500  # Section 87A Rebate

        # Apply cess (4% on tax payable)
        cess = tax * 0.04
        total_tax = tax + cess  # Total tax including cess

        # Calculate net salary after tax
        net_salary = gross_salary - total_tax
        """
        # Display the results
        messagebox.showinfo("Tax Calculation Result", f"Gross Salary After Deductions: ₹{gross_salary}\n"
                                                     f"Taxable Income: ₹{taxable_income}\n"
                                                     f"Tax before Rebate and Cess: ₹{tax}\n"
                                                     f"Tax after Rebate: ₹{max(tax, 0)}\n"
                                                     f"Total Tax after Cess: ₹{total_tax}\n"
                                                     f"Net Salary after Tax: ₹{net_salary}")
        """

        #-------------------- New Tax Regime  ---------------------------------------
        # New Tax Regime Slabs for FY 2024-25
        new_slab_1_limit = 300000  # Up to ₹3 lakh: No tax
        new_slab_2_limit = 700000  # ₹3 lakh to ₹7 lakh: 5%
        new_slab_3_limit = 1000000  # ₹7 lakh to ₹10 lakh: 10%
        new_slab_4_limit = 1200000  # ₹10 lakh to ₹12 lakh: 15%
        new_slab_5_limit = 1500000  # ₹12 lakh to ₹15 lakh: 20%
        new_slab_6_limit = float('inf')  # Above ₹15 lakh: 30%

        #-------------------- New Tax Regime Rates ---------------------------------------
        new_rate_1 = 0.05  # 5% tax for income between ₹3 lakh and ₹7 lakh
        new_rate_2 = 0.10  # 10% tax for income between ₹7 lakh and ₹10 lakh
        new_rate_3 = 0.15  # 15% tax for income between ₹10 lakh and ₹12 lakh
        new_rate_4 = 0.20  # 20% tax for income between ₹12 lakh and ₹15 lakh
        new_rate_5 = 0.30  # 30% tax for income above ₹15 lakh

        # Function to calculate tax based on the New Tax Regime slabs
        def calculate_new_tax(taxable_income):
            tax_new = 0
            if taxable_income <= new_slab_1_limit:
                return tax_new  # No tax if income is less than or equal to ₹3 lakh
            if taxable_income <= new_slab_2_limit:
                tax_new += (taxable_income - new_slab_1_limit) * new_rate_1
                return tax_new
            if taxable_income <= new_slab_3_limit:
                tax_new += (new_slab_2_limit - new_slab_1_limit) * new_rate_1
                tax_new += (taxable_income - new_slab_2_limit) * new_rate_2
                return tax_new
            if taxable_income <= new_slab_4_limit:
                tax_new += (new_slab_2_limit - new_slab_1_limit) * new_rate_1
                tax_new += (new_slab_3_limit - new_slab_2_limit) * new_rate_2
                tax_new += (taxable_income - new_slab_3_limit) * new_rate_3
                return tax_new
            if taxable_income <= new_slab_5_limit:
                tax_new += (new_slab_2_limit - new_slab_1_limit) * new_rate_1
                tax_new += (new_slab_3_limit - new_slab_2_limit) * new_rate_2
                tax_new += (new_slab_4_limit - new_slab_3_limit) * new_rate_3
                tax_new += (taxable_income - new_slab_4_limit) * new_rate_4
                return tax_new
            # For income above ₹15 lakh
            tax_new += (new_slab_2_limit - new_slab_1_limit) * new_rate_1
            tax_new += (new_slab_3_limit - new_slab_2_limit) * new_rate_2
            tax_new += (new_slab_4_limit - new_slab_3_limit) * new_rate_3
            tax_new += (new_slab_5_limit - new_slab_4_limit) * new_rate_4
            tax_new += (taxable_income - new_slab_5_limit) * new_rate_5
            return tax_new
        
        #Standard Deduction
        standard_deduction_new = 75000
        taxable_income_new = gross_salary_new - standard_deduction_new
        # Calculate tax
        tax_new = calculate_new_tax(taxable_income_new)

        # Apply rebate under Section 87A (if applicable) - Available for taxable income less than ₹5 lakh
        if taxable_income_new <= 700000:
            tax_new -= 25000  # Section 87A Rebate

        # Apply cess (4% on tax payable)
        cess_new = tax_new * 0.04
        total_tax_new = tax_new + cess_new  # Total tax including cess

        # Calculate net salary after tax
        net_salary_new = gross_salary_new - total_tax_new
        """
        # Display the results
        messagebox.showinfo("Tax Calculation Result", f"Gross Salary After Deductions: ₹{gross_salary_new}\n"
                                                     f"Taxable Income: ₹{taxable_income_new}\n"
                                                     f"Tax before Rebate and Cess: ₹{tax_new}\n"
                                                     f"Tax after Rebate: ₹{max(tax_new, 0)}\n"
                                                     f"Total Tax after Cess: ₹{total_tax_new}\n"
                                                     f"Net Salary after Tax: ₹{net_salary_new}")
        """
        # Compare and suggest tax regime
        if total_tax < total_tax_new:
            suggestion = f"Suggestion:\nThe **Old Tax Regime** is better with a tax of ₹{total_tax}. Total benefit: ₹{total_tax_new - total_tax}"
        elif total_tax > total_tax_new:
            suggestion = f"Suggestion:\nThe **New Tax Regime** is better with a tax of ₹{total_tax_new}. Total benefit: ₹{total_tax - total_tax_new}"
        else:
            suggestion = "Both tax regimes result in the same tax liability. You can choose either based on other factors."

        # Merged results with comparison and suggestion
        messagebox.showinfo("Tax Calculation Result", 
                            f"Old Tax Regime:\n"
                            f"Gross Salary After Deductions: ₹{gross_salary}\n"
                            f"Taxable Income: ₹{taxable_income}\n"
                            f"Tax before Rebate and Cess: ₹{tax}\n"
                            f"Tax after Rebate: ₹{max(tax, 0)}\n"
                            f"Total Tax after Cess: ₹{total_tax}\n"
                            f"Net Salary after Tax: ₹{net_salary}\n\n"
                            f"New Tax Regime:\n"
                            f"Gross Salary After Deductions: ₹{gross_salary_new}\n"
                            f"Taxable Income: ₹{taxable_income_new}\n"
                            f"Tax before Rebate and Cess: ₹{tax_new}\n"
                            f"Tax after Rebate: ₹{max(tax_new, 0)}\n"
                            f"Total Tax after Cess: ₹{total_tax_new}\n"
                            f"Net Salary after Tax: ₹{net_salary_new}\n\n"
                            f"{suggestion}")


    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

# Set up the main window
root = tk.Tk()
root.title("Tax Calculation Input Form")

# Define labels
labels = [
    "Gross Salary", "Professional Tax",
    "Section 80C", "Section 80CCC", "Section 80CCD(1)", 
    "Section 80CCD(1B)", "Section 80CCG", "Section 80D", 
    "Section 80DD", "Section 80DDB", "Section 80E", "Section 80EE", 
    "Section 80EEA", "Section 80GG", "Section 80GGA", "Section 80GGB", 
    "Section 80GGC", "Section 80U", "Section 80QQB", "Section 80RRB", 
    "Section 80TTA", "Allowances u/s 10"
]

entries = {}

# Create labels and text entry boxes for each input
for i, label in enumerate(labels):
    row = i // 2  # Divide the rows into two columns
    col = i % 2
    tk.Label(root, text=label).grid(row=row, column=col * 2, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5)
    entries[label] = entry

# Set default values of 0 for each entry
for entry in entries.values():
    entry.insert(0, '0')

# Specific entries for each variable
entry_gross_salary = entries["Gross Salary"]
entry_professional_tax = entries["Professional Tax"]
entry_section_80c = entries["Section 80C"]
entry_section_80ccc = entries["Section 80CCC"]
entry_section_80ccd_1 = entries["Section 80CCD(1)"]
entry_section_80ccd_1b = entries["Section 80CCD(1B)"]
entry_section_80ccg = entries["Section 80CCG"]
entry_section_80d = entries["Section 80D"]
entry_section_80dd = entries["Section 80DD"]
entry_section_80ddb = entries["Section 80DDB"]
entry_section_80e = entries["Section 80E"]
entry_section_80ee = entries["Section 80EE"]
entry_section_80eea = entries["Section 80EEA"]
entry_section_80gg = entries["Section 80GG"]
entry_section_80gga = entries["Section 80GGA"]
entry_section_80ggb = entries["Section 80GGB"]
entry_section_80ggc = entries["Section 80GGC"]
entry_section_80u = entries["Section 80U"]
entry_section_80qqb = entries["Section 80QQB"]
entry_section_80rrb = entries["Section 80RRB"]
entry_section_80tta = entries["Section 80TTA"]
entry_allowances_u_s_10 = entries["Allowances u/s 10"]

# Button to collect values and show message
calculate_button = tk.Button(root, text="Calculate Tax", command=collect_values)
calculate_button.grid(row=len(labels) // 2 + 1, column=0, columnspan=4, pady=10)

# Run the Tkinter event loop
root.mainloop()
