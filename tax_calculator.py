from openpyxl import Workbook


def calculate_gross_salary(basic, da_percent, hra_percent, other):
    da = basic * da_percent / 100
    hra = basic * hra_percent / 100
    return basic + da + hra + other


def calculate_tax(income):
    if income <= 400000:
        return 0
    elif income <= 800000:
        return (income - 400000) * 0.05
    elif income <= 1200000:
        return (400000 * 0.05) + (income - 800000) * 0.10
    elif income <= 1600000:
        return (400000 * 0.05) + (400000 * 0.10) + (income - 1200000) * 0.15
    elif income <= 2000000:
        return (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (income - 1600000) * 0.20
    elif income <= 2400000:
        return (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (income - 2000000) * 0.25
    else:
        return (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (income - 2400000) * 0.30


def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input! Enter a number.")


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Tax Report"
    ws.append(["Month", "Salary", "Tax Deducted"])

    months = ["April", "May", "June", "July", "August", "September",
              "October", "November", "December", "January", "February", "March"]

    basic = get_input("Enter Basic Salary: ")
    da = get_input("Enter DA %: ")
    hra = get_input("Enter HRA %: ")
    other = get_input("Enter Other Allowances: ")

    tax_paid = 0

    for i in range(12):
        print(f"\n===== {months[i]} =====")

        if input("Basic changed? (yes/no): ").lower() == "yes":
            basic = get_input("Enter NEW Basic: ")

        if input("DA changed? (yes/no): ").lower() == "yes":
            da = get_input("Enter NEW DA %: ")

        if input("HRA changed? (yes/no): ").lower() == "yes":
            hra = get_input("Enter NEW HRA %: ")

        monthly_salary = calculate_gross_salary(basic, da, hra, other)

        annual_income = monthly_salary * 12
        total_tax = calculate_tax(annual_income - 75000)

        remaining_months = 12 - i
        remaining_tax = total_tax - tax_paid

        monthly_tax = remaining_tax / remaining_months
        tax_paid += monthly_tax

        print("Salary:", round(monthly_salary, 2))
        print("Tax Deducted:", round(monthly_tax, 2))

        ws.append([months[i], monthly_salary, monthly_tax])

    print("\nTotal Tax Paid:", round(tax_paid, 2))

    wb.save("tax_report.xlsx")
    print("Excel file saved successfully!")


if __name__ == "__main__":
    main()
