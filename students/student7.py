# 1. Define the formal state configuration map
# This represents a multi-stage unauthenticated registration token validation pipeline
class AutomataValidator:
    def __init__(self):
        # Q: The set of all valid system operational states
        self.states = {"UNAUTH", "CAPTCHA_VERIFIED", "PROMO_VAL_CHECK", "ACCOUNT_CREATED", "ERROR"}
        
        # q0: The initial system entry point
        self.current_state = "UNAUTH"
        
        # F: The strict accepting state (Registration complete)
        self.accepting_state = "ACCOUNT_CREATED"

    # delta: The transition function governing logical steps
    def transition(self, event):
        print(f"[*] Processing Event: {event} | Current State: {self.current_state}")
        
        # Define strict legal sequence paths
        if self.current_state == "UNAUTH" and event == "SUBMIT_CAPTCHA":
            self.current_state = "CAPTCHA_VERIFIED"
            
        elif self.current_state == "CAPTCHA_VERIFIED" and event == "PROCESS_PROMO":
            self.current_state = "PROMO_VAL_CHECK"
            
        elif self.current_state == "PROMO_VAL_CHECK" and event == "GENERATE_PROFILE":
            self.current_state = "ACCOUNT_CREATED"
            
        else:
            # Any out-of-order execution automatically defaults to an error trap
            self.current_state = "ERROR"

# 2. Main testing verification execution
if __name__ == "__main__":
    # Test 1: Simulating an out-of-order state bypass attempt
    # An attacker attempts to jump straight to profile generation, skipping step limits
    print("--- Execution Run 1: Simulating State Machine Logic Bypass ---")
    tester_1 = AutomataValidator()
    
    # Payload attempts to invoke the profile creation process prematurely
    tester_1.transition("GENERATE_PROFILE") 
    
    if tester_1.current_state == "ACCOUNT_CREATED":
        print("[!] CRITICAL LOGIC ERROR: State machine bypassed unauthenticated!")
    else:
        print(f"[+] Security enforcement successful. Machine halted in safe state: {tester_1.current_state}\n")

    # Test 2: Evaluating standard intended operation flows
    print("--- Execution Run 2: Verifying Standard Synchronized Flow ---")
    tester_2 = AutomataValidator()
    tester_2.transition("SUBMIT_CAPTCHA")
    tester_2.transition("PROCESS_PROMO")
    tester_2.transition("GENERATE_PROFILE")
    
    if tester_2.current_state == tester_2.accepting_state:
        print("[+] Application flow logic is formally validated and secure.")
