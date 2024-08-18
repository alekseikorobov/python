import pyaudio
import time
import pickle

p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))

WIDTH = 1
INDEX = 1 #{'index': 1, 'structVersion': 2, 'name': 'Microphone (2- JAZZTEL JT-FN-52', 'hostApi':
FORMAT=p.get_format_from_width(WIDTH)
print(FORMAT)
CHANNELS = 2
RATE = 44100
CHUNK = 512

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
#stream.start_stream()


# stream = p.open(format=FORMAT, input_device_index = INDEX,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# p = pyaudio.PyAudio()

# def callback(in_data, frame_count, time_info, status):
#     return (in_data, pyaudio.paContinue)

# stream = p.open(format=p.get_format_from_width(WIDTH),
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 output=True,
#                 stream_callback=callback)

# stream.start_stream()

# while stream.is_active():    
#     time.sleep(0.1)

# stream.stop_stream()
# stream.close()

# p.terminate()