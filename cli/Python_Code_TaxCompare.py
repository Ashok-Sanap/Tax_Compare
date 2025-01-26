
#GROSS Salary
gross_salary = 2298197

# Deductions and allowances used in tax calculations
# Standard Deduction (available to all salaried individuals, typically ₹50,000)
standard_deducation = 50000  # Deduction of ₹50,000 for salaried individuals

# Professional tax paid (deduction available for salaried individuals, based on the state tax laws)
professional_tax = 2500  # This is state-dependent and should be added as per the actual tax paid
#---------------------------------------------------------------------------------------------------------

# Section 80C, 80CCC, 80CCD (combined limit of ₹1,50,000)
section_80c = 150000  # Deduction for contributions to retirement savings, life insurance premiums, etc. (Part of the ₹1,50,000 limit)
section_80ccc = 0  # Deduction for contributions to pension funds (e.g., LIC pension, UTI pension). Combined with 80C
section_80ccd_1 = 0  # Deduction for individual contributions to NPS (Part of the ₹1,50,000 limit for 80C)

# Combine 80C, 80CCC, and 80CCD(1) under a shared ₹1,50,000 limit
combined_80c_limit = 150000  # Total combined limit for 80C, 80CCC, and 80CCD(1)

# Total deductions for 80C, 80CCC, and 80CCD(1) 
total_80c_deductions = section_80c + section_80ccc + section_80ccd_1
if total_80c_deductions > combined_80c_limit:
    total_80c_deductions = combined_80c_limit  # If combined value exceeds ₹1,50,000, set to limit
#---------------------------------------------------------------------------------------------------------

# Section 80CCD(1B) - Additional contribution to NPS
section_80ccd_1b = 50000  # Additional NPS deduction, up to ₹50,000 over and above Section 80C limit
section_80ccd_1b_limit = 50000  # Max limit for section 80CCD(1B)
if section_80ccd_1b > section_80ccd_1b_limit:
    section_80ccd_1b = section_80ccd_1b_limit  # If value exceeds limit, set to limit
#--------------------------------------------------------------------------------------------------------

# Section 80CCD(2) - Employer's contribution to NPS
section_80_ccd2 = 0  # Employer’s contribution to NPS. Not subject to the ₹1,50,000 limit of Section 80C. Deduction is allowed up to 10% of salary (Basic + DA)
section_80_ccd2_limit = 0.1  # Max limit as percentage of Basic + DA
# You can check the employer's contribution by calculating salary and applying the limit
#-------------------------------------------------------------------------------------------------------

# Variable to select if the individual is a senior citizen
is_senior_citizen = False  # Set to True if the individual is a senior citizen, else False

# Section 80D - Health Insurance Premiums
section_80d = 2814  # Deduction for premiums paid for health insurance. ₹25,000 for self/family and ₹50,000 for senior citizens.
section_80d_limit = 25000  # Max limit for section 80D for self/family
section_80d_senior_limit = 50000  # Max limit for senior citizens

# Adjust the limit based on whether the individual is a senior citizen or not
if is_senior_citizen:
    if section_80d > section_80d_senior_limit:
        section_80d = section_80d_senior_limit  # If value exceeds limit for senior citizens, set to limit
else:
    if section_80d > section_80d_limit:
        section_80d = section_80d_limit  # If value exceeds limit for self/family, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80DD - Deduction for the care of a dependent person with a disability
section_80dd = 75000  # Deduction for individuals caring for a dependent with a disability. ₹75,000 (₹1,25,000 for severe disability)
section_80dd_limit = 75000  # Max limit for section 80DD for disability (₹1,25,000 for severe disability)
if section_80dd > section_80dd_limit:
    section_80dd = section_80dd_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Variable to select if the individual is a senior citizen
is_senior_citizen = False  # Set to True if the individual is a senior citizen, else False

# Section 80DDB - Deduction for medical treatment of specified diseases (like cancer, neurological diseases)
section_80ddb = 0  # Deduction for expenses incurred on medical treatment for specified diseases
section_80ddb_limit = 40000  # Max limit for section 80DDB for general individuals
section_80ddb_senior_limit = 100000  # Max limit for senior citizens

# Adjust the limit based on whether the individual is a senior citizen or not
if is_senior_citizen:
    if section_80ddb > section_80ddb_senior_limit:
        section_80ddb = section_80ddb_senior_limit  # If value exceeds limit for senior citizens, set to limit
else:
    if section_80ddb > section_80ddb_limit:
        section_80ddb = section_80ddb_limit  # If value exceeds limit for general individuals, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80E - Deduction for interest on loans taken for higher education
section_80e = 0  # Deduction for interest on loans taken for higher education. No upper limit, available for 8 years
section_80e_limit = "No limit"  # No limit for section 80E for interest on education loans
#-------------------------------------------------------------------------------------------------------

# Section 80EE - Deduction for interest on home loan for first-time home buyers
section_80ee = 0  # Deduction for home loan interest for first-time home buyers. ₹50,000
section_80ee_limit = 50000  # Max limit for section 80EE
if section_80ee > section_80ee_limit:
    section_80ee = section_80ee_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80EEA - Deduction for interest on home loans for affordable housing
section_80eea = 0  # Additional deduction for home loan interest for affordable housing. ₹1,50,000
section_80eea_limit = 150000  # Max limit for section 80EEA
if section_80eea > section_80eea_limit:
    section_80eea = section_80eea_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80GG - Deduction for rent paid without receiving House Rent Allowance (HRA)
section_80gg = 0  # Deduction for individuals paying rent but not receiving HRA. ₹5,000 per month (maximum ₹60,000 per year)
section_80gg_limit = 60000  # Max limit for section 80GG
if section_80gg > section_80gg_limit:
    section_80gg = section_80gg_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80GGA - Deduction for donations to scientific research or rural development
section_80gga = 0  # Deduction for donations to scientific research, rural development, or similar causes
section_80gga_limit = "No limit"  # No limit for section 80GGA for donations
#-------------------------------------------------------------------------------------------------------

# Section 80GGB - Deduction for contributions to political parties by companies
section_80ggb = 0  # Deduction for companies contributing to political parties
section_80ggb_limit = "No limit"  # No limit for section 80GGB
#-------------------------------------------------------------------------------------------------------

# Section 80GGC - Deduction for contributions to political parties by individuals
section_80ggc = 0  # Deduction for individuals contributing to political parties
section_80ggc_limit = "No limit"  # No limit for section 80GGC
#-------------------------------------------------------------------------------------------------------

# Section 80U - Deduction for individuals with disabilities
section_80u = 0  # Deduction for individuals with disabilities. ₹75,000 (₹1,25,000 for severe disability)
section_80u_limit = 75000  # Max limit for section 80U for disability (₹1,25,000 for severe disability)
if section_80u > section_80u_limit:
    section_80u = section_80u_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80CCG - Rajiv Gandhi Equity Savings Scheme (RGESS) - Investment in eligible stocks
section_80ccg = 0  # Deduction for investment under RGESS for individuals with income up to ₹12 lakh. Maximum ₹50,000
section_80ccg_limit = 50000  # Max limit for section 80CCG
if section_80ccg > section_80ccg_limit:
    section_80ccg = section_80ccg_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80QQB - Deduction for royalty income earned by authors
section_80qqb = 0  # Deduction for royalty income earned by authors of books. Maximum ₹3,00,000
section_80qqb_limit = 300000  # Max limit for section 80QQB
if section_80qqb > section_80qqb_limit:
    section_80qqb = section_80qqb_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80RRB - Deduction for royalty income from patents
sectoin_80rrb = 0  # Deduction for income earned from patents. Maximum ₹3,00,000
section_80rrb_limit = 300000  # Max limit for section 80RRB
if sectoin_80rrb > section_80rrb_limit:
    sectoin_80rrb = section_80rrb_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 80TTA - Deduction for interest income from savings accounts
section_80tta = 0  # Deduction for interest income from savings accounts. Maximum ₹10,000
section_80tta_limit = 10000  # Max limit for section 80TTA
if section_80tta > section_80tta_limit:
    section_80tta = section_80tta_limit  # If value exceeds limit, set to limit
#-------------------------------------------------------------------------------------------------------

# Section 10 - Income Exempt from Tax (e.g., Agricultural income, certain allowances, etc.)
allowances_u_s_10 = 452436  # Allowances under Section 10, such as HRA and other exemptions
allowances_u_s_10_limit = "Varies"  # The limit for Section 10 exemptions depends on the specific allowance


# Deductions and allowances applied to the gross salary, even if the value is zero

# Gross salary after all deductions
gross_salary -= standard_deducation  # Standard Deduction

gross_salary -= professional_tax  # Professional tax

# Deduction under Section 80C, 80CCC, 80CCD (combined limit of ₹1,50,000)
gross_salary -= total_80c_deductions  # Total deductions under 80C, 80CCC, and 80CCD

# Deduction under Section 80CCD(1B) - Additional NPS contribution
gross_salary -= section_80ccd_1b

# Deduction under Section 80D (Health insurance premiums)
gross_salary -= section_80d

# Deduction under Section 80DD (Care of dependent with disability)
gross_salary -= section_80dd

# Deduction under Section 80DDB (Medical treatment for specified diseases)
gross_salary -= section_80ddb

# Deduction under Section 80E (Interest on loans for higher education)
gross_salary -= section_80e

# Deduction under Section 80EE (Home loan interest for first-time home buyers)
gross_salary -= section_80ee

# Deduction under Section 80EEA (Home loan interest for affordable housing)
gross_salary -= section_80eea

# Deduction under Section 80GG (Rent paid without receiving HRA)
gross_salary -= section_80gg

# Deduction under Section 80GGA (Donations to scientific research or rural development)
gross_salary -= section_80gga

# Deduction under Section 80GGB (Contributions to political parties by companies)
gross_salary -= section_80ggb

# Deduction under Section 80GGC (Contributions to political parties by individuals)
gross_salary -= section_80ggc

# Deduction under Section 80U (Disability deduction)
gross_salary -= section_80u

# Deduction under Section 80CCG (Rajiv Gandhi Equity Savings Scheme)
gross_salary -= section_80ccg

# Deduction under Section 80QQB (Royalty income for authors)
gross_salary -= section_80qqb

# Deduction under Section 80RRB (Royalty income from patents)
gross_salary -= sectoin_80rrb

# Deduction under Section 80TTA (Interest income from savings accounts)
gross_salary -= section_80tta

# Deduction under Section 10 (Allowances under section 10)
gross_salary -= allowances_u_s_10

# Final gross salary after all deductions
print(f"Final gross salary after deductions: ₹{gross_salary}")

# Constants for tax slabs
taxable_income = gross_salary  # After all deductions

# Tax slabs for the Old Regime
slab_1_limit = 250000  # Up to ₹2.5 lakh: No tax
slab_2_limit = 500000  # ₹2.5 lakh to ₹5 lakh: 5%
slab_3_limit = 1000000  # ₹5 lakh to ₹10 lakh: 20%
slab_4_limit = float('inf')  # Above ₹10 lakh: 30%

# Tax rates
rate_1 = 0.05  # 5% tax for income between ₹2.5 lakh and ₹5 lakh
rate_2 = 0.20  # 20% tax for income between ₹5 lakh and ₹10 lakh
rate_3 = 0.30  # 30% tax for income above ₹10 lakh

# Calculate the income tax based on slabs
def calculate_old_tax(taxable_income):
    tax = 0

    # Slab 1: No tax for income up to ₹2.5 lakh
    if taxable_income <= slab_1_limit:
        return tax  # No tax

    # Slab 2: 5% tax for income between ₹2.5 lakh and ₹5 lakh
    if taxable_income <= slab_2_limit:
        tax += (taxable_income - slab_1_limit) * rate_1
        return tax

    # Slab 3: 20% tax for income between ₹5 lakh and ₹10 lakh
    if taxable_income <= slab_3_limit:
        tax += (slab_2_limit - slab_1_limit) * rate_1  # Tax for ₹2.5 lakh to ₹5 lakh
        tax += (taxable_income - slab_2_limit) * rate_2  # Tax for ₹5 lakh to ₹10 lakh
        return tax

    # Slab 4: 30% tax for income above ₹10 lakh
    tax += (slab_2_limit - slab_1_limit) * rate_1  # Tax for ₹2.5 lakh to ₹5 lakh
    tax += (slab_3_limit - slab_2_limit) * rate_2  # Tax for ₹5 lakh to ₹10 lakh
    tax += (taxable_income - slab_3_limit) * rate_3  # Tax for above ₹10 lakh
    return tax

# Calculate the tax based on the old regime
tax = calculate_old_tax(taxable_income)

# Apply rebate under Section 87A (if applicable) - Available for taxable income less than ₹5 lakh
if taxable_income <= 500000:
    tax -= 12500  # Section 87A Rebate

# Apply cess (4% on tax payable)
cess = tax * 0.04
total_tax = tax + cess  # Total tax including cess

# Output the tax details
print(f"Taxable income: ₹{taxable_income}")
print(f"Tax before rebate and cess: ₹{tax}")
print(f"Tax after rebate (if applicable): ₹{max(tax, 0)}")
print(f"Total tax after cess: ₹{total_tax}")
old_tax_with_cess = total_tax
# Final Gross Salary after tax deduction
net_salary = gross_salary - total_tax
print(f"Net salary after tax: ₹{net_salary}")

#--------------------------NEW TAX REGIME ---------------------------------------------------
print("\n\nNew Tax Regime")

#GROSS Salary
gross_salary = 2298197
#Standard Deductions
standard_deducation_new = 75000

# New Tax Regime Constants
new_tax_slab_limits = [300000, 700000, 1000000, 1200000, 1500000, float('inf')]  # Slab limits
new_tax_rates = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30]  # Corresponding rates

# Function to calculate tax under the new regime
def calculate_new_tax(taxable_income):
    tax = 0
    prev_limit = 0
    
    for i in range(len(new_tax_slab_limits)):
        if taxable_income > new_tax_slab_limits[i]:
            tax += (new_tax_slab_limits[i] - prev_limit) * new_tax_rates[i]
            prev_limit = new_tax_slab_limits[i]
        else:
            tax += (taxable_income - prev_limit) * new_tax_rates[i]
            break
    return tax

# Calculate Taxable Income under New Regime
taxable_income_new = gross_salary  # Base income for the New Tax Regime
taxable_income_new -= standard_deducation_new  # Standard deduction is applicable

# Calculate tax based on the slabs
new_tax = calculate_new_tax(taxable_income_new)

# Apply rebate under Section 87A (for income ≤ ₹7,00,000)
if taxable_income_new <= 700000:
    new_tax = 0  # Full rebate

# Apply 4% health and education cess
new_tax_with_cess = new_tax + (new_tax * 0.04)

# Output results for the New Tax Regime
print(f"Taxable income (New Regime): ₹{taxable_income_new}")
print(f"Tax before rebate and cess (New Regime): ₹{new_tax}")
print(f"Total tax after rebate and cess (New Regime): ₹{new_tax_with_cess}")

print("\n\n")
# Decision logic
if old_tax_with_cess < new_tax_with_cess:
    print(f"Suggestion:\nThe **Old Tax Regime** is better with a tax of ₹{old_tax_with_cess}.")
    print(f"Total benefit: {new_tax_with_cess - old_tax_with_cess}")
elif old_tax_with_cess > new_tax_with_cess:
    print(f"Suggestion:\nThe **New Tax Regime** is better with a tax of ₹{new_tax_with_cess}.")
    print(f"Total benefit: {old_tax_with_cess - new_tax_with_cess}")
else:
    print("Both tax regimes result in the same tax liability. You can choose either based on other factors.")
