from z3 import *

# 1. Initialize our operational objects as integer identifiers
requested_object_id = Int('requested_object_id')

# 2. Define our sets mathematically using conditional constraints
# Assume IDs 1-100 are Public, 101-200 are private User Invoices, 201+ are Admin configs
is_public = And(requested_object_id >= 1, requested_object_id <= 100)
is_user_private = And(requested_object_id >= 101, requested_object_id <= 200)
is_admin_private = requested_object_id >= 201

# 3. Initialize the mathematical verification solver
s = Solver()

# 4. Model a broken validation function written by a developer:
# "Allow access if it's in the public range OR if it's simply not an admin file"
allow_access = Or(is_public, Not(is_admin_private))
s.add(allow_access == True)

# 5. Define the target structural violation: An unauthenticated visitor 
# successfully accessing an ID inside the private user data set.
s.add(is_user_private == True)

# 6. Execute the proof
if s.check() == sat:
    print("[!] ACCESS POOL LEAK IDENTIFIED!")
    print("An unauthenticated actor can extract private data via this Object ID:")
    print(s.model())
else:
    print("[+] Structural isolation boundaries are mathematically sound.")
