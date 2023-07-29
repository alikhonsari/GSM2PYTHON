# SMS Modem Python Script

This is a Python script that allows you to communicate with an SMS modem using AT commands. With this script, you can send SMS messages to a recipient and receive incoming SMS messages. The script uses the `serial` library to establish a serial connection with the SMS modem and sends AT commands to interact with it.

## Requirements

Before using this script, ensure you have the following:

1. An SMS modem connected to your computer through a serial port.
2. Python installed on your system.
3. The `serial` library, which can be installed using pip:

```bash
pip install pyserial
```

## Usage

Open the script in a Python environment or editor.

Make sure to replace '**COM10**' in the line **ser = serial.Serial('COM10', 9600, timeout=1)** with the appropriate serial port name that corresponds to your GSM modem.

Update the **phone_number** variable with the recipient's phone number, and the message variable with the desired message content.

Save the changes.

## Functionality

The script provides the following functionality:

**Sending an SMS:** The script can send an SMS message to the specified recipient. It sets the SMS text mode, sends the SMS, and then waits for a response to confirm successful delivery.

**Receiving an SMS:** The script continuously checks for incoming SMS messages. Once it detects an unread message, it extracts the sender's phone number and the message content, prints them out, and marks the message as read.
