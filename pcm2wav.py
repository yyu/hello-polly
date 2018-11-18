#!/usr/bin/env python3

import sys
import wave

def pcm2wav(filename):
    with wave.open(filename + '.wav', 'w') as wavf:
        with open(filename, 'rb') as pcmf:
            wavf.setframerate(16000)
            wavf.setnchannels(1)
            wavf.setsampwidth(2)
            wavf.writeframes(pcmf.read())

if __name__ == '__main__':
    pcm2wav(sys.argv[1])
