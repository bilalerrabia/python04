print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")


def crisis_response(file_to_open: str):
    try:
        with open(file_to_open) as f:
            data = f.read()
        print(f"SUCCESS: Archive recovered - ``{data}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    else:
        print("STATUS: Normal operations resumed")


print()
print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
crisis_response("lost_archive.txt")
print()
print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
crisis_response("classified_data.txt")
print()
print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
crisis_response("standard_archive.txt")
print()
print("All crisis scenarios handled successfully. Archives secure.")
