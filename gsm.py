import serial
import time

# Function to send AT command and get the response
def send_at_command(command):
    ser.write(command.encode() + b'\r\n')
    time.sleep(1)
    response = b''
    while ser.in_waiting:
        response += ser.read(ser.in_waiting)
    return response.decode()

# Initialize the serial port with the appropriate settings
ser = serial.Serial('COM10', 9600, timeout=1)  # Replace 'COMx' with the actual port name
signal_response = send_at_command('AT+CSQ')
print(signal_response)
response = send_at_command('AT')
print(response)
signal_response = send_at_command('AT+CSQ')
print(signal_response)
response = send_at_command('AT+CSCA?')
print(response)

try:
    # Send an AT command to check if the modem is responsive
    response = send_at_command('AT')
    if 'OK' not in response:
        raise Exception("Modem not responding!")

    # Set the SMS text mode
    send_at_command('AT+CMGF=1')

    # Send an SMS
    phone_number = '+1*******'  # Replace with the recipient's phone number
    message = 'Hello, this is a test SMS from Python!'  # Replace with your message
    send_at_command(f'AT+CMGS="{phone_number}"')
    send_at_command(message + chr(26)) 
    time.sleep(2)  # Ctrl+Z to send the message

    print("SMS sent successfully!")

    # Wait for incoming SMS
    print("Waiting for incoming SMS...")

    while True:
        response = send_at_command('AT+CMGL="REC UNREAD"')
        print("Raw response:", response)  # Add this line for debugging
        if '+CMGL:' in response:
            # Parse the response to extract the sender's phone number and message
            index = response.index('+CMGL:')
            sender_info = response[index:].splitlines()[0].split(',')
            print("Sender info:", sender_info)  # Add this line for debugging
            sender_number = sender_info[2].strip('"')
            sms_index = int(sender_info[0].split(':')[1])
            message_start = index + len(response[index:]) + 2
            message = response[message_start:].splitlines()[0].strip()

            print(f"Received SMS from: {sender_number}")
            print(f"Message: {message}")

            # Mark the received message as read
            send_at_command(f'AT+CMGR={sms_index}')
            break
        time.sleep(5)


except Exception as e:
    print("Error:", str(e))

finally:
    ser.close()
