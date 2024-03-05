#constants
ITS = {"CMPH-209", "COMM-238", "CPNT-219", "CPRG-216", "MATH-237", "CPNT-224", "CPRG-217", "CPSY-204", "CPSY-206", "PHIL-241"}
SD = {"CPRG-213", "COMM-238", "CPNT-217", "CPRG-216", "MATH-237", "CPRG-211", "CPRG-250", "CPSY-200", "CPSY-202", "PHIL-241"}

print("Common 1st Year Courses:")
for i in ITS & SD:
    print(f"{i:^18}")
print("")

print("ITS-only 1st Year Courses:")
for i in ITS - SD:
    print(f"{i:^18}")
print("")

print("SD-only 1st Year Courses:")
for i in SD - ITS:
    print(f"{i:^18}")