# Interact with an Arduino board using a Bluefruit LE UART Friend and Bluetooth
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

import user_input

# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()


# Main function implements the program logic so it can run in a background thread.
def main():
    # Clear any cached data
    ble.clear_cached_data()

    # Get the first available BLE network adapter
    adapter = ble.get_default_adapter()
    # Make sure the BLE network adapter is powered on
    adapter.power_on()
    print('Using adapter: {0}'.format(adapter.name))

    # Disconnect any currently connected UART devices.
    print('Disconnecting any connected UART devices...')
    UART.disconnect_devices()

    # Scan for UART devices.
    print('Searching for UART device...')
    try:
        adapter.start_scan()
        # Search for the first UART device found (will time out after 60 seconds
        # but you can specify an optional timeout_sec parameter to change it).
        device = UART.find_device()
        if device is None:
            raise RuntimeError('Failed to find UART device!')
    finally:
        # Make sure scanning is stopped before exiting.
        adapter.stop_scan()

    print('Connecting to device...')
    device.connect()  # Will time out after 60 seconds, specify timeout_sec parameter
                      # to change the timeout.

    # Once connected do everything else in a try/finally to make sure the device
    # is disconnected when done.
    try:
        # Wait for service discovery to complete for the UART service.  Will
        # time out after 60 seconds (specify timeout_sec parameter to override).
        print('Discovering services...')
        UART.discover(device)

        # Once service discovery is complete create an instance of the service
        # and start interacting with it.
        uart = UART(device)

        quit_program = False

        # Main loop to get user choice
        while not quit_program:
            # Get command choice from user
            cmd = user_input.get_cmd()
            if cmd == '7':
                # User chose to quit program
                quit_program = True
                print("Exiting program")
            else:
                cmd_string = user_input.input_to_cmd(cmd)
                if cmd == '5' or cmd == '6':
                    # Get additional arguments for command '5' (blink the internal LED)
                    # or for command '6' (switch on the RGB LED)
                    cmd_string = user_input.get_cmd_to_send(cmd_string)
                # Send the command to the UART
                uart.write(cmd_string)
                print("Sent cmd '" + cmd_string + "' to the device.")
                # Wait up to 40 seconds to receive data from the device.
                print('Waiting up to 40 seconds to receive data from the device...')
                received = uart.read(timeout_sec=40)
                if received is not None:
                    # Received data, print it out.
                    print('Received: {0}'.format(received))
                else:
                    # Timeout waiting for data, None is returned.
                    print('Received no data!')

    finally:
        # Make sure device is disconnected on exit.
        print("Disconnecting from UART")
        device.disconnect()


# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()

# Start the mainloop to process BLE events, and run the provided function in
# a background thread.  When the provided main function stops running, returns
# an integer status code, or throws an error the program will exit.
ble.run_mainloop_with(main)
