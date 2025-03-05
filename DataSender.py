import serial
import time

# Configure the serial port
ser = serial.Serial(
    port='COM3',        # Replace with your port name
    baudrate=9600,      # Match the baud rate with FPGA configuration
    timeout=1           # Timeout in seconds
)

# Ensure the serial port is open
if ser.is_open:
    print(f"Connected to {ser.portstr}")
else:
    print("Failed to open serial port.")
    exit()

# Function to send data
def send_data(data):
    ser.write(data.encode())  # Send data to FPGA
    print(f"Sent: {data}")

# Function to receive data
def receive_data():
    response = ser.readline().decode().strip()  # Read response from FPGA
    print(f"Received: {response}")
    return response

# Example usage
try:
    while True:
        data_to_send = input("Enter data to send: ")
        send_data(data_to_send)
        time.sleep(1)  # Wait for FPGA to process
        receive_data()
except KeyboardInterrupt:
    print("Communication terminated.")
finally:
    ser.close()
