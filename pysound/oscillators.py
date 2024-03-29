# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import math
import numpy as np
from pysound.buffer import create_buffer


def create_sine_table(size):
    args = np.linspace(0.0, 2*math.pi, num=size, endpoint=False)
    return np.sin(args)


def square_wave(params, frequency=400, amplitude=1,
                offset=0, ratio=0.5):
    '''
    Generate a square wave
    :param params: buffer parameters, controls length of signal created
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :param ratio: proportion of high to total time (array or value)
    :return: array of resulting signal
    '''
    frequency = create_buffer(params, frequency)
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    ratio = create_buffer(params, ratio)
    phase = np.add.accumulate(frequency / params.get_sample_rate()) % 1
    output = offset + amplitude * np.where(phase < ratio, 1, -1)
    return output


def saw_wave(params, frequency=400, amplitude=1,
                offset=0, ratio=0.5):
    '''
    Generate a saw wave
    :param params: buffer parameters, controls length of signal created
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :param ratio: proportion of rise time to total time (array or value)
    :return: array of resulting signal
    '''
    frequency = create_buffer(params, frequency)
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    ratio = np.clip(create_buffer(params, ratio), 0.000001, 0.999999)
    phase = np.add.accumulate(frequency / params.get_sample_rate()) % 1
    output = offset + amplitude * np.where(phase < ratio, -1 + 2*phase/ratio, 1 - 2*(phase-ratio)/(1-ratio))
    return output

def noise(params, amplitude=1, offset=0):
    '''
    Generate a noise signal
    :param params: buffer parameters, controls length of signal created
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :return: array of resulting signal
    '''
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    output = offset + amplitude * (np.random.random(params.length)*2 - 1)
    return output

def table_wave(params, frequency=400, amplitude=1.0,
                offset=0, table=None):
    '''
    Generate a wave from a wavetable
    :param params: buffer parameters, controls length of signal created
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :param table: table of values representing one full cycle of the waveform. Nominally the values
     should be between +/-1 (array). The array can be any size.
    :return: array of resulting signal
    '''
    if not table:
        table = create_sine_table(65536)
    size = table.size
    #print("frequency1", frequency)
    frequency = create_buffer(params, frequency)
    #print("frequency2", frequency)

    #print("amplitude1", frequency)
    amplitude = create_buffer(params, amplitude)
    #print("apmlitude2", frequency)
    
    #print("offset1", frequency)
    offset = create_buffer(params, offset)
    #print("offset2", frequency)
    
    index = np.floor((np.add.accumulate(frequency / params.get_sample_rate()) % 1) * size).astype(int)
    output = offset + amplitude * table[index]
    return output

def sync_table_wave(params, sync, frequency=400, amplitude=1,
                offset=0, table=None):
    '''
    Generate a wave from a wavetable, syncing with negative going transions of sync signal
    :param params: buffer parameters, controls length of signal created
    :param sync: sync signal
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :param table: table of values representing one full cycle of the waveform. Nominally the values
     should be between +/-1 (array). The array can be any size.
    :return: array of resulting signal
    '''
    if not table:
        table = create_sine_table(65536)
    size = table.size
    sync = create_buffer(params, sync)
    frequency = create_buffer(params, frequency)
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    output = create_buffer(params, 0)
    index = 0
    for i in range(1, params.length):
        if sync[i-1]>=0 and sync[i]<0:
            index = 0
        output[i] = table[index]
        index = index + (frequency[i] / params.get_sample_rate()) * size
        index = int(index % size)
    return output*amplitude

def sine_wave(params, frequency=400, amplitude=1.0, offset=0):
    '''
    Generate a sine wave
    Convenience function, table_wave generates a sine wave by default
    :param params: buffer parameters, controls length of signal created
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :return: array of resulting signal
    '''
    return table_wave(params, frequency, amplitude, offset)

def midi2f(params, midi=69):
    '''
    Convert a midi value to a frequency.
    Midi value 69 corresponds to A4 (440Hz). Changing the midi value by 1 corresponds to
    one semitone
    :param params: buffer parameters, controls length of signal created
    :param midi: midi value
    :return: array of resulting frequency
    '''
    midi = create_buffer(params, midi)
    output = 2**((midi - 69)/12)*440
    return output

