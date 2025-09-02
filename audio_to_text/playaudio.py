import numpy as np
import pyaudio

class MyPlayAudio():

    def __init__(self,device_index=None):
        self.device_index = device_index
        
    # Параметры аудио
    RATE = 48000  # Изменено под твое устройство

    def play(self, audio_data):
        # Запуск PyAudio
        stream = None
        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,  # Два канала, так как устройство поддерживает 2
                            rate=self.RATE,
                            output=True,
                            output_device_index=self.device_index)  # Указываем index устройства

            # Дублируем аудиоданные для стерео (если нужен моно, можно оставить один канал)
            #stereo_data = np.repeat(audio_data[:, np.newaxis], 2, axis=1).flatten()

            # Воспроизведение
            stream.write(audio_data.tobytes())
        finally:
            if stream is not None:
                # Закрытие
                stream.stop_stream()
                stream.close()
            p.terminate()


if __name__ == '__main__':
    mp = MyPlayAudio()
    DURATION = 2  # Длительность в секундах
    FREQ = 440.0  # Частота сигнала (Гц)
    # Генерация сигнала (синусоида)
    RATE = mp.RATE
    t = np.linspace(0, DURATION, int(RATE * DURATION), endpoint=False)
    audio_data = (0.5 * np.sin(2 * np.pi * FREQ * t)).astype(np.float32)  # 32-битные float

    mp.play(audio_data)