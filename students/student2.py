from z3 import *

# 1. Initialize the Boolean logical state variables
code_is_expired = Bool('code_is_expired')
is_first_time_user = Bool('is_first_time_user')

# 2. Create the solver engine instance
solver = Solver()

# 3. Add the developer's actual broken code constraint
developer_logic = Or(Not(code_is_expired), is_first_time_user)
solver.add(developer_logic == True)

# 4. Define the target vulnerability condition (Code IS expired, user IS NOT new, but bonus triggers)
vulnerability_condition = And(code_is_expired == True, is_first_time_user == False)
solver.add(vulnerability_condition)

# 5. Execute the mathematical solver verification check
if solver.check() == sat:
    print("[!] SYSTEM LOGIC IS BROKEN. VULNERABILITY FOUND!")
    print("Exact Input Conditions Required:")
    print(solver.model())
else:
    print("[+] System logic is secure against this state.")
