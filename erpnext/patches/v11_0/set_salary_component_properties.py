import frappe

def execute():
    frappe.db.sql("update `tabSalary Component` set is_payable=1, is_tax_applicable=1 where type='Earning'")
    frappe.db.sql("update `tabSalary Component` set is_payable=0 where type='Deduction'")

    frappe.db.sql("""update `tabSalary Component` set variable_based_on_taxable_salary=1
        where type='Deduction' and name in ('TDS', 'Tax Deducted at Source')""")

    frappe.db.sql("""update `tabSalary Detail` set is_tax_applicable=1 
        where parentfield='earnings' and statistical_component=0""")
    frappe.db.sql("""update `tabSalary Detail` set variable_based_on_taxable_salary=1 
        where parentfield='deductions' and salary_component in ('TDS', 'Tax Deducted at Source')""")