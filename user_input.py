# List of possible commands
cmds = ['1', '2', '3', '4', '5', '6', '7']


# Print the possible commands to the user
def print_choices():
    print("1: Switch LED on")
    print("2: Switch LED off")
    print("3: Get Temperature")
    print("4: Get Humidity")
    print("5: Blink LED")
    print("6: RGB LED")
    print("7: Quit program")


# Function to convert the user input into the associated command
def input_to_cmd(argument):
    switcher = {
        '1': "on",
        '2': "off",
        '3': "temperature",
        '4': "humidity",
        '5': "blink",
        '6': "rgb",
    }
    return switcher.get(argument, "")


# Get a positive integer from the command line
# Used to get arguments for commands '5' and '6'
def get_positive_integer_input(message):
    input_correct = False
    integer_input = 0
    while not input_correct:
        try:
            integer_input = int(input(message))
            if integer_input >= 0:
                input_correct = True
        except ValueError:
            print("Not not an integer value...")
    return integer_input


# Get the arguments for command '5': Blink the internal LED
def get_args_blink():
    # Get number of time to blink the LED
    repetition = get_positive_integer_input('Enter a number of repetition: ')
    # Get the duration to switch on the LED
    duration_on = get_positive_integer_input('Enter the duration (milliseconds) to switch on the LED: ')
    # Get the duration to switch off the LED
    duration_off = get_positive_integer_input('Enter the duration (milliseconds) to switch off the LED: ')

    return repetition, duration_on, duration_off


# Get a color value
# This value should be an integer between 0 and 255
def get_rgb_color(color_string):
    color = 0
    color_correct = False
    while not color_correct:
        color = get_positive_integer_input("Choose the value for the " + color_string + " color:\nPlease enter an integer between 0 and 255\n")
        if 0 <= color <= 255:
            color_correct = True
    return color


# Get the arguments for command '6': Switch on/off the RGB LED
# Get the values for the red, green and blue colors
def get_rgb_values():
    red = get_rgb_color("red")
    green = get_rgb_color("green")
    blue = get_rgb_color("blue")
    return red, green, blue


# Get the user choice for the command
def get_cmd():
    print("\nChoose an action:")
    print_choices()
    input_cmd = ""
    try:
        input_cmd = raw_input()
    except SyntaxError:
        print("Unexpected character")

    while input_cmd not in cmds:
        print(input_cmd + " is not a valid action")
        print("\nPlease, choose a valid action:")
        print_choices()
        try:
            input_cmd = raw_input()
        except SyntaxError:
            print("Unexpected character")

    return input_cmd


# Convert the command chosen by the user to a command to send to the UART
# and executable by the Arduino board
def get_cmd_to_send(cmd):
    if cmd == "blink":
        repetition, duration_on, duration_off = get_args_blink()
        cmd = cmd + " " + str(repetition) + " " + str(duration_on) + " " + str(duration_off)
    if cmd == "rgb":
        red, green, blue = get_rgb_values()
        cmd = cmd + " " + str(red) + " " + str(green) + " " + str(blue)
    return cmd
