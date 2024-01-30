import numpy as np
import sounddevice as sd

recording =True # Flag to control recording

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
        # Process the audio data here

def start_recordig():
    global recording
    stream=sd.InputStream(callback=callback)
    with stream:
        print("Recording, Pres Ctrl + c to stop")
        try:
            while recording:
                sd.sleep(100) # Adjust the duration as needed
        except KeyboardInterrupt:
            pass
        finally:
            recording=False

def stop_recording():
    global recording
    recording=False
