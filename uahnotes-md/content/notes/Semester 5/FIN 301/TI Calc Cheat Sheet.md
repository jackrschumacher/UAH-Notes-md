---
title: TI Calculator Cheat Sheet
---
## 2. Effective Interest Rate (EAR)
**Definition:** The actual annual interest rate earned/paid, accounting for compounding.

**TI-84 Plus CE Function:**
* `▶Eff(nominal rate, compounding periods per year)`
* *Location: `apps` > `Finance...` > `C:▶Eff(`*
* *Note: Enter the nominal rate as a whole percentage (e.g., 8 for 8%).*

**Mathematical Formula:**
`EAR = (1 + r/n)^n - 1`
*(r = nominal rate as a decimal, n = compounding periods per year)*

## 3. Loan Payments (TVM)
**Definition:** Finding the regular monthly payment to pay down a lump sum loan to zero.

**TI-84 Plus CE Function:**
* **TVM Solver**
* *Location: `apps` > `Finance...` > `1:TVM Solver...`*
* **Variables:**
    * **N:** Total number of payments (Months * Years)
    * **I%:** Annual interest rate (as a whole number, e.g., 7 for 7%)
    * **PV:** Total loan amount (positive number)
    * **PMT:** *Solve for this* (Hover over and press `ALPHA` + `ENTER`)
    * **FV:** 0
    * **P/Y & C/Y:** Payments/Compounding per year (usually 12)
    * **PMT:** END

**Mathematical Formula:**
`PMT = (PV * (r/n)) / (1 - (1 + r/n)^-N)`
*(PV = Loan Amount, r = annual rate decimal, n = payments per year, N = total number of payments)*

## 4. Interest Paid on Specific Payments
**Definition:** Calculating the dollar amount of a payment that goes toward interest rather than principal.

**TI-84 Plus CE Function:**
* `ΣInt(start payment, end payment)`
* *Location: `apps` > `Finance...` > `A:ΣInt(`*
* *Note: Requires TVM Solver variables to be filled out and solved first.*
* *Example: `ΣInt(1,1)` finds the interest for the first payment. `ΣInt(1,12)` finds the total interest paid in the first year.*

**Mathematical Formula (For the 1st Payment only):**
`I_1 = PV * (r/n)`
*(PV = Loan Amount, r = annual rate decimal, n = payments per year)*