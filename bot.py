import os
import time
import random

# GitHub Secrets se accounts file read karna
accounts = os.getenv("ACCOUNTS_FILE", "").split("\n")

def run_bot():
    if not accounts or accounts == [""]:
        print("❌ No accounts found!")
        return
    
    for account in accounts:
        if ":" in account:
            email, password = account.split(":")
            print(f"✅ Logging in with {email} and earning points...")

            # Fake delay (original bot me yaha login aur searches ka automation hoga)
            time.sleep(random.randint(5, 10))  

if __name__ == "__main__":
    run_bot()
