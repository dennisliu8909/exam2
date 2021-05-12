# exam2

In this exam, please perform the following task:
mbed run the RPC loop to get input string commands from PC/Python, and it will in turn call custom RPC functions.
PC/Python use RPC over serial to send a command to call accelerator capture mode on mbed
The custom function called by PC/Python will start to capture the accelerator values in multiple ways.
In this accelerator capture mode, mbed will start a thread function.
In this accelerator capture function, mbed will record a set of accelerator data values (as in mbed lab 8).
Please classify the saved accelerator data values with the gesture classification TF Lite model you trained in mbed lab 8 (with at least 3 classes). mbed will publish the classified gesture as an event (gesture ID and sequence number of the event) through WiFi/MQTT to a broker. #. Please show the gesture ID on LED or uLCD.
Please also extract features of the saved accelerator data values by your own method:
Please design at least one feature of your own.
The purpose of the features is to differentiate accelerator data by their classified gesture, e.g., circle vs. z-shape. They are manually tuned features for classification.
One possible feature is number of change of direction larger than a threshold, e.g., 30 degrees. We call this case as "change of direction".
We can also record if the data has not change of direction larger than a threshold for a number of measured points. We can this case as "stationary".
Note that we can combine several features together. For example, we can record 1 if there is a case of "change of direction". And we record a 0 for the case of "stationary". Then a set of accelerometer values will generate a sequence of 1 and 0, which is our extracted feature.
Note that above features are not well-defined. If you implement them, you have to carefully specify your feature sets and define with mathematical equations on accelerometer vectors. For example, how do you filter short-term noise from your calculation?
Save the extracted features in another data structure.
After the PC/Python gets a preset number of gesture events, e.g., 10, from the broker, it sends a command to mbed to stop the accelerator capture mode. Therefore, the mbed is back to RPC loop.
After the PC/Python send the stop command, please send another command to retrieve the saved feature data.
Please plot the following together in two sub figures aligned with the event sequence order in PC/Python:
1.The classified gesture events.
2.The extracted features.
