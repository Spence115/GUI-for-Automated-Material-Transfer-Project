<h1 align="center">GUI for Automated Material Transfer Project</h1>

This is the Graphical User Interface (GUI) delivery system I created as part of my senior capstone project at California State University, Chico. This GUI was designed to facilitate the Automated Material Transfer project. You can find the utilization of the GUI in the Automated Material Transfer project [here]( https://nolanspencer.com/files/AMTProject.pdf).

I built the GUI using the following:
  * Python
  *	SQLite3
  *	PyQt5
  *	Qt Designer

It is important to note that the GUI is designed to use the required external hardware:
  *	[Raspberry Pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)
  *	[Adafruit Ultimate GPS Breakout V3 module]( https://www.adafruit.com/product/746)
  *	[GPS Active Antenna 28dB](https://www.adafruit.com/product/960)

The GUI runs locally on the Raspberry Pi 3B+ and connects to the GPS Active Antenna 28dB through the Adafruit Ultimate GPS Breakout V3 module. Windows 10 workstations on the same network can access the GUI using [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/windows/). This setup allows simultaneous access to the same GUI instance from multiple workstations, ensuring uninterrupted delivery requests. <b>It is essential that the Raspberry Pi is connected to the same network as all workstations to function correctly.</b>

<i>Note that I have only tested this using up to three separate Windows 10 PCs. I cannot guarantee it will function properly beyond that amount, but it should work for any number of workstations in theory.</i>

<h2 align="center">File Overview</h2>

### Python
  *	<kbd>GUI.py</kbd>: Main window displaying delivery statuses, timestamps, and buttons.
  *	<kbd>WorkOrder.py</kbd>: Pop-up window for entering and confirming the work order associated with the delivery.
  *	<kbd>DeliveryLocation.py</kbd>: Pop-up window for choosing the pickup location from three buildings.
  *	<kbd>Quantity.py</kbd>: Pop-up window for selecting the delivery quantity.
  *	<kbd>PickupLocation.py</kbd>: Pop-up window for choosing the pickup location from three buildings.
  *	<kbd>coordinates.py</kbd>: Provides real-time latitude and longitude updates (optional).

### SQL
  *	<kbd>BPT.db</kbd>: Default database file for testing.
  *	<kbd>SQLite_Database_Setup.txt</kbd>: Shows the database schema and how to insert dummy values.

If you want to see the GUI in action, check out [this screen capture]( https://www.youtube.com/watch?v=H0a9SNjjXRE) and [this demonstration]( https://www.youtube.com/watch?v=g9HrBze5j2g&t=1s) showing three workstations running simultaneously.


