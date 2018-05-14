hours = float(input('Enter hours worked: '))
rate = float(input('Pay rate without $: '))
if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
print(pay)
