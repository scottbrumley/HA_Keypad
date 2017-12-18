# always seem to need this
import sys
import os
import paho.mqtt.client as mqtt

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# This is our window from QtCreator
import mainwindow_auto

# Default state for all buttons
STATE_DEFAULT = 0
# State when the button is currently pressed
STATE_PRESSED = 1
# Action buttons: action is available (proper pin has been entered)
STATE_AVAILABLE = 2
# Action buttons: used to indicate which state the alarm is in
STATE_ACTIVE = 3
# The following states are for the pin input indicator
STATE_1 = 4
STATE_2 = 5
STATE_3 = 6
STATE_4_GOOD = 7
STATE_4_BAD = 8

PINS = os.environ.get('PINS').split(',')
MQTT_HOST = os.environ.get('MQTT_HOST')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
MQTT_USER = os.environ.get('MQTT_USER')
MQTT_PASS = os.environ.get('MQTT_PASS')
MQTT_CLIENT_ID = os.environ.get('MQTT_CLIENT_ID', 'alarmpanel')
MQTT_STATE_TOPIC = os.environ.get('MQTT_STATE_TOPIC', 'home/alarm')
MQTT_COMMAND_TOPIC = os.environ.get('MQTT_COMMAND_TOPIC', 'home/alarm/set')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    ### functions for the buttons to call
    def pressedOnButton(self):
        if self.key_label.text() in PINS:
            print ("Armed Away!")
            client.publish(MQTT_COMMAND_TOPIC, payload='ARM_AWAY', qos=2, retain=True)
            self.key_label.setText("")
        else:
            self.setStatus("Invalid Pin")

    def pressedOffButton(self):
        if self.key_label.text() in PINS:
            print ("Armed Home")
            client.publish(MQTT_COMMAND_TOPIC, payload='ARM_HOME', qos=2, retain=True)
            self.key_label.setText("")
        else:
            self.setStatus("Invalid Pin")

    def pressedDisarmButton(self):
        if self.key_label.text() in PINS:
            print ("Disarmed")
            client.publish(MQTT_COMMAND_TOPIC, payload='DISARM', qos=2, retain=True)
            self.key_label.setText("")
        else:
            self.setStatus("Invalid Pin")

    def pressedKeyPadButton(self, valueStr):
        print ("Key Pressed: " + valueStr)
        currentVal = self.key_label.text()

        if valueStr == "#" or valueStr == "*":
            currentVal = ""
        else:
            currentVal = currentVal + valueStr

        self.key_label.setText(currentVal)

    def setStatus(self,valueStr):
        self.status_label.setText(valueStr)

    def on_message(self,client, userdata, message):
        global current_state, pending_state
        current_state = message.payload

        print ("received payload: " + str(current_state.decode("utf-8") ))

        if current_state.decode("utf-8")  == 'pending':
            self.status_label.setStyleSheet('color: yellow')
            self.setStatus("Pending")
            #self.status_label.setStyleSheet('color: yellow')

        if current_state.decode("utf-8")  == 'armed_away':
            self.button1.setStyleSheet('color: white;background-color: red')
            self.status_label.setStyleSheet('color: red')
            self.setStatus("Armed Away")
            #self.status_label.setStyleSheet('color: red')
            #self.button1.setStyleSheet('background-color: red')
            #self.button1.setStyleSheet('color: red')
        else:
            self.button1.setStyleSheet('color: black;background-color: white')

        if current_state.decode("utf-8")  == 'armed_home':
            self.button2.setStyleSheet('color: white;background-color: red')
            self.status_label.setStyleSheet('color: red')
            self.setStatus("Armed Home")
            #self.status_label.setStyleSheet('color: red')
            #self.button2.setStyleSheet('background-color: red')
            #self.button2.setStyleSheet('color: red')
        else:
            self.button2.setStyleSheet('color: black;background-color: white')

        if current_state.decode("utf-8")  == 'triggered':
            self.status_label.setStyleSheet('color: yellow')
            self.setStatus("Triggered")
            #self.status_label.setStyleSheet('color: yellow')

        if current_state.decode("utf-8")  == 'disarmed':
            self.button3.setStyleSheet('color: white;background-color: green')
            self.status_label.setStyleSheet('color: white;background-color: green')
            self.setStatus("Disarmed")
        else:
            self.button3.setStyleSheet('color: black;background-color: white')
            #self.status_label.setStyleSheet('color: white')
            #self.status_label.setStyleSheet('background-color: green')

            #self.button3.setStyleSheet('background-color: green')
            #self.button3.setStyleSheet('color: green')

        # HA will send `pending` or `triggered` when the state is about to change
        # In these cases, we can't be 100% sure what the next state will be
        # In all other cases, we definitely know the current state, so wipe out `pending_state`
        if current_state.decode("utf-8")  != 'pending' or current_state.decode("utf-8")  != 'triggered':
            pending_state = ''

        # Update the corresponding button state#
        #if current_state == 'disarmed':
        #    btnDisarm.set_state(STATE_ACTIVE)
        #elif current_state == 'armed_home':
        #    btnArmHome.set_state(STATE_ACTIVE)
        #elif current_state == 'armed_away':
        #    btnArmAway.set_state(STATE_ACTIVE)

        # Update the other button states
        #update_action_button_states()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.button1.clicked.connect(lambda: self.pressedOnButton())
        self.button2.clicked.connect(lambda: self.pressedOffButton())
        self.button3.clicked.connect(lambda: self.pressedDisarmButton())
        self.noZeroButton.clicked.connect(lambda: self.pressedKeyPadButton("0"))
        self.noOneButton.clicked.connect(lambda: self.pressedKeyPadButton("1"))
        self.noTwoButton.clicked.connect(lambda: self.pressedKeyPadButton("2"))
        self.noThreeButton.clicked.connect(lambda: self.pressedKeyPadButton("3"))
        self.noFourButton.clicked.connect(lambda: self.pressedKeyPadButton("4"))
        self.noFiveButton.clicked.connect(lambda: self.pressedKeyPadButton("5"))
        self.noSixButton.clicked.connect(lambda: self.pressedKeyPadButton("6"))
        self.noSevenButton.clicked.connect(lambda: self.pressedKeyPadButton("7"))
        self.noEightButton.clicked.connect(lambda: self.pressedKeyPadButton("8"))
        self.noNineButton.clicked.connect(lambda: self.pressedKeyPadButton("9"))
        self.noPoundButton.clicked.connect(lambda: self.pressedKeyPadButton("#"))
        self.noAstButton.clicked.connect(lambda: self.pressedKeyPadButton("*"))
        self.key_label.setText("")
        self.status_label.setText("")

    def on_connect(self,client, userdata, flags, rc):
        global connected, pending_state #, status_line_1
        pending_state = ''
        if rc == 0:
            print ("MQTT connection successful")
            #status_line_1.set('Connected')
            connected = True
            client.subscribe(MQTT_STATE_TOPIC, 2)
        elif rc == 1:
            print ("MQTT connection refused - incorrect protocol version")
            #status_line_1.set('Connection refused - incorrect protocol version')
            connected = False
        elif rc == 2:
            print ("MQTT connection refused - invalid client identifier")
            #status_line_1.set('Connection refused - invalid client identifier')
            connected = False
        elif rc == 3:
            print ("MQTT connection refused - server unavailable")
            #status_line_1.set('Connection refused - server unavailable')
            connected = False
        elif rc == 4:
            print ("MQTT connection refused - bad username or password")
            #status_line_1.set('Connection refused - invalid credentials')
            connected = False
        elif rc == 5:
            print ("MQTT connection refused - not authorized")
            #status_line_1.set('Connection refused - not authorized')
            connected = False
        else:
            print ("Unknown connection error: code ") + str(rc)
            #status_line_1.set('Unknown connection error: ' + str(rc))
            connected = False

def on_disconnect(client, userdata, rc):
    global connected #, status_line_1
    connected = False

    if rc != 0:
        print ("Disconnected unexpectedly")
        #status_line_1.set('Disconnected unexpectedly')

# python bit to figure how who started This
if __name__ == "__main__":
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setStatus('Starting')
    form.show()

    client = mqtt.Client(MQTT_CLIENT_ID)
    client.on_connect = form.on_connect
    client.on_message = form.on_message
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.connect_async(MQTT_HOST, MQTT_PORT)

    client.loop_start()
    sys.exit(app.exec_())
