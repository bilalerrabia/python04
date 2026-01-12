filename = "ft_ancient_text.py"

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
try:
    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...")
    myfile = open(filename)
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
    exit(0)

print("\nRECOVERED DATA:")
print(myfile.read())
myfile.close()
print("Data recovery complete. Storage unit disconnected.")
