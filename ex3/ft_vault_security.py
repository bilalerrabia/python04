print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

reading_file = "read.txt"
writing_file = "write.txt"

print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols")

with open(reading_file, 'r') as r:
    print("SECURE EXTRACTION:")
    print("[CLASSIFIED] Quantum encryption keys recovered")
    data = r.read()
    print("[CLASSIFIED] Archive integrity: 100%")

with open(writing_file, 'w') as w:
    print("SECURE PRESERVATION:")
    w.write(data)
    print("[CLASSIFIED] New security protocols archived")

print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
