print("Listing of Months. \n")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']

months.append('November')
print(months)
months.append('October')
print(months)
months.append('December')
print(f"{months}\n")

print("\n\nMONTHS OF YEAR 2025. \n")

for mon in months:
    print(f"{mon} of 2025 \n")

print("\nFULL NAME\n")

fullname = 'Zyan Kloe Sanchez'
fn = list(fullname)
print(f"\n {fn} \n")

for f in fullname[0 : 9]:
    print(f)

fn.reverse()
print(f"\n {fn} \n")

for f in fullname[10 : 17]:
    print(f)