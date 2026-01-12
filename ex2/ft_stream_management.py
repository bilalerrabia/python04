import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

ID = input("Input Stream active. Enter archivist ID: ")
report = input("Input Stream active. Enter status report: ")
print("", file=sys.stdout)
sys.stdout.write(f"[STANDARD] Archive status from {ID}: {report}\n")

print(
    "[ALERT] System diagnostic: Communication channels verified",
    file=sys.stderr
    )
sys.stdout.write("[STANDARD] Data transmission complete\n")

sys.stdout.write("\nThree-channel communication test successful.\n")
