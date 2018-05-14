def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
    return pay
try:
    inp_hours = (input('Enter hours worked: '))
    inp_rate = (input('Pay rate without $: '))
    hours = float(inp_hours)
    rate = float(inp_rate)
    print('Pay: ', computepay(hours, rate))
except:
    print('Please enter numeric input')
    quit()
    