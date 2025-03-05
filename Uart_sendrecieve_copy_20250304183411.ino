// Arduino Serial Echo Program
void setup() {
    Serial.begin(9600);  // Set baud rate to match Python script
    while (!Serial) {
        ; // Wait for serial port to connect
    }
}

void loop() {
    if (Serial.available() > 0) {  // Check if data is available
        String receivedData = Serial.readStringUntil('\n'); // Read incoming data
        receivedData.trim(); // Remove any leading/trailing whitespace

        Serial.print("Echo: "); // Add prefix before sending back
        Serial.println(receivedData); // Send received data back
    }
}
