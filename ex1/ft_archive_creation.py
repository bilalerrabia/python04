print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

filename = "new_discovery.txt"

print(f"Initializing new storage unit: {filename}")
new_file = open(filename, "w")
print("Storage unit created successfully...\n")

print("Inscribing preservation data...")
new_file.write("[ENTRY 001] New quantum algorithm discovered\n")
new_file.write("[ENTRY 002] Efficiency increased by 347%\n")
new_file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
print("[ENTRY 001] New quantum algorithm discovered")
print("[ENTRY 002] Efficiency increased by 347%")
print("[ENTRY 003] Archived by Data Archivist trainee")
new_file.close()
print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{filename}' ready for long-term preservation.")
