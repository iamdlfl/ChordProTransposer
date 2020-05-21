"""
Transposes a ChordPro file from one key to another.

This program first identifies the user's intended transposition. It then tests
whether this file uses sharps or flats for the chords. Further development
identifying the actual key of the song will remove the necessity for this test.
The program then uses either a list of chords with sharps or chords with flats
to transpose the original file into a new key. It then writes this to a new
file.
"""

import os.path
from os import path

"""Definitions

This section defines various functions and variables.

Functions
    file_name()
    determine_direction()
    determine_halfsteps()
    open_file()
    key_test()
    transposition_function()

Variables
    newsong
    \S+chordsharps
    \S+chordflats
    fname
    updown
    halfsteps
    songfile
    songraw
    song
    chordtype
    writesongfile
"""
def file_name():
    """
    Defines the file name to be transposed

    variables
        filename
    """
    filename = input('What is the file name for the song you want to convert?')
    if len(filename) < 1: filename = 'songeasy.txt' #For ease in testing
    return filename
def determine_direction():
    """
    Determines direction to transpose

    variables:
        upordown
    """
    while True:
        upordown = input('Would you like to transpose up or down? '
                       'Please input either "up" or "down".')
        if len(upordown) < 1:
                upordown = 'down' #For ease in testing
                return upordown
                break
        elif (upordown != 'up'
                and upordown != 'down'
                and upordown != 'Up'
                and upordown != 'Down'):
            pass
        else:
            return upordown
            break
def determine_halfsteps():
    """
    Determines number of halfsteps to transpose

    variables
        halfsteptest
        halfstep
    """
    halfsteptest = None
    while halfsteptest != 0:
        halfstep = input('How many halfsteps would you like to transpose? '
                          'Please input a number.')
        try:
            int(halfstep)
        except:
            continue
        halfstep = int(halfstep)
        if halfstep < 12:
            return halfstep
            halfsteptest = 0
        else:
            print('Please input a number less than 12.')
def key_test():
    """
    Currently tests whether original file uses sharps.

    If original file uses sharps, returns 'sharp' as chordtypes.
    If original file does not use sharps, returns 'flat' as chordtypes.

    variables
        chordtypes
        sharpstest
        iteration
    """
    sharpstest = ['#]', '#m]', '#7]', '#m7]', '#dim]', '#aug']
    for iteration in sharpstest:
        if iteration in songraw:
            chordtypes = 'sharp'
        else:
            chordtypes = 'flat'
        return chordtypes
def new_song_file():
    """
    This function will test whether or not the file name has already been
    created with a transposed tag.

    If it has been, it will create a file with incrementing numbers
    for each transposition.

    variables
        counter
        newwsongfile
    """
    counter = 1
    while True:
        if path.exists(fname.strip('.txt')
                        + 'Transposed'
                        + str(counter)
                        + '.txt'):
            counter +=1
        else:
            newsongfile = open(fname.strip('.txt')
                                + 'Transposed'
                                + str(counter)
                                + '.txt', 'w+')
            return newsongfile
            break


newsong = ''
majchordsharps = [
    '[A]', '[A#]', '[B]',
    '[C]', '[C#]', '[D]',
    '[D#]', '[E]', '[F]',
    '[F#]', '[G]', '[G#]',
    ]
majchordflats = [
    '[A]', '[Bb]', '[B]',
    '[C]', '[Db]', '[D]',
    '[Eb]', '[E]', '[F]',
    '[Gb]', '[G]', '[Ab]',
    ]
minchordsharps = [
    '[Am]', '[A#m]', '[Bm]',
    '[Cm]', '[C#m]', '[Dm]',
    '[D#m]', '[Em]', '[Fm]',
    '[F#m]', '[Gm]', '[G#m]',
    ]
minchordflats = [
    '[Am]', '[Bbm]', '[Bm]',
    '[Cm]', '[Dbm]', '[Dm]',
    '[Ebm]', '[Em]', '[Fm]',
    '[Gbm]', '[Gm]', '[Abm]',
    ]
seventhchordsharps = [
    '[A7]', '[A#7]', '[B7]',
    '[C7]', '[C#7]', '[D7]',
    '[D#7]', '[E7]', '[F7]',
    '[F#7]', '[G7]', '[G#7]',
    ]
seventhchordflats = [
    '[A7]', '[Bb7]', '[B7]',
    '[C7]', '[Db7]', '[D7]',
    '[Eb7]', '[E7]', '[F7]',
    '[Gb7]', '[G7]', '[Ab7]',
    ]
minorseventhchordsharps = [
    '[Am7]', '[A#m7]', '[Bm7]',
    '[Cm7]', '[C#m7]', '[Dm7]',
    '[D#m7]', '[Em7]', '[Fm7]',
    '[F#m7]', '[Gm7]', '[G#m7]',
    ]
minorseventhchordflats = [
    '[Am7]', '[Bbm7]', '[Bm7]',
    '[Cm7]', '[Dbm7]', '[Dm7]',
    '[Ebm7]', '[Em7]', '[Fm7]',
    '[Gbm7]', '[Gm7]', '[Abm7]',
    ]
augmentedchordsharps = [
    '[Aaug]', '[A#aug]', '[Baug]',
    '[Caug]', '[C#aug]', '[Daug]',
    '[D#aug]', '[Eaug]', '[Faug]',
    '[F#aug]', '[Gaug]', '[G#aug]',
    ]
augmentedchordflats = [
    '[Aaug]', '[Bbaug]', '[Baug]',
    '[Caug]', '[Dbaug]', '[Daug]',
    '[Ebaug]', '[Eaug]', '[Faug]',
    '[Gbaug]', '[Gaug]', '[Abaug]',
    ]
diminishedchordsharps = [
    '[Adim]', '[A#dim]', '[Bdim]',
    '[Cdim]', '[C#dim]', '[Ddim]',
    '[D#dim]', '[Edim]', '[Fdim]',
    '[F#dim]', '[Gdim]', '[G#dim]',
    ]
diminishedchordflats = [
    '[Adim]', '[Bbdim]', '[Bdim]',
    '[Cdim]', '[Dbdim]', '[Ddim]',
    '[Ebdim]', '[Edim]', '[Fdim]',
    '[Gbdim]', '[Gdim]', '[Abdim]',
    ]
sus4chordsharps = [
    '[Asus4]', '[A#sus4]', '[Bsus4]',
    '[Csus4]', '[C#sus4]', '[Dsus4]',
    '[D#sus4]', '[Esus4]', '[Fsus4]',
    '[F#sus4]', '[Gsus4]', '[G#sus4]',
    ]
sus4chordflats = [
    '[Asus4]', '[Bbsus4]', '[Bsus4]',
    '[Csus4]', '[Dbsus4]', '[Dsus4]',
    '[Ebsus4]', '[Esus4]', '[Fsus4]',
    '[Gbsus4]', '[Gsus4]', '[Absus4]',
    ]
add9chordsharps = [
    '[Aadd9]', '[A#add9]', '[Badd9]',
    '[Cadd9]', '[C#add9]', '[Dadd9]',
    '[D#add9]', '[Eadd9]', '[Fadd9]',
    '[F#add9]', '[Gadd9]', '[G#add9]',
    ]
add9chordflats = [
    '[Aadd9]', '[Bbadd9]', '[Badd9]',
    '[Cadd9]', '[Dbadd9]', '[Dadd9]',
    '[Ebadd9]', '[Eadd9]', '[Fadd9]',
    '[Gbadd9]', '[Gadd9]', '[Abadd9]',
    ]
fname = file_name()
updown = determine_direction()
halfsteps = determine_halfsteps()
songfile = open(fname, 'r+')
songraw = songfile.read()
song = songraw.split('\n')
songfile.close()
chordtype = key_test()
writesongfile = new_song_file()

"""
This will reverse the lists of chords if the direction of transposition
is 'up', to simplify transposition.
"""
if updown == 'up' or updown == 'Up':
    majchordflats.reverse()
    majchordsharps.reverse()
    minchordflats.reverse()
    minchordsharps.reverse()
    seventhchordsharps.reverse()
    seventhchordflats.reverse()
    minorseventhchordsharps.reverse()
    minorseventhchordflats.reverse()
    augmentedchordflats.reverse()
    augmentedchordsharps.reverse()
    diminishedchordflats.reverse()
    diminishedchordsharps.reverse()
    sus4chordflats.reverse()
    sus4chordsharps.reverse()
    add9chordflats.reverse()
    add9chordsharps.reverse()
else:
    pass

def transposition_function(chordlist):
    """
    Transposes the song and writes it to string 'newsong'

    arguments
        chordlist
    variables
        line
        count
        item
        linelist
        newlinelist
        word
        newword
        replaced
    """
    global song
    global newsong
    newsong = '' #To reset newsong when running this function multiple times.
    for line in song:
        newword = ''
        newlinelist = []
        linelist = line.split('[')
        for word in linelist:
            count = 0
            replaced = None
            word = '[' + word
            for item in chordlist:
                if item in word and replaced is None:
                    newword = word.replace(item, chordlist[count - halfsteps])
                    replaced = 'replaced'
                    count += 1
                elif replaced is not None:
                    break
                else:
                    newword = word
                    count += 1
            newlinelist.append(newword)
        line = ''.join(newlinelist)
        newsong += line.lstrip('[')
        newsong += '\n'

"""
Transposition

This section will use the function defined above to transpose the song
and write it to a new file using subsequent lists of different kinds of chords.
"""
if chordtype == 'flat':
    transposition_function(majchordflats)
    song = newsong.split('\n')
    transposition_function(minchordflats)
    song = newsong.split('\n')
    transposition_function(seventhchordflats)
    song = newsong.split('\n')
    transposition_function(minorseventhchordflats)
    song = newsong.split('\n')
    transposition_function(augmentedchordflats)
    song = newsong.split('\n')
    transposition_function(diminishedchordflats)
    song = newsong.split('\n')
    transposition_function(sus4chordflats)
    song = newsong.split('\n')
    transposition_function(add9chordflats)
else:
    transposition_function(majchordsharps)
    song = newsong.split('\n')
    transposition_function(minchordsharps)
    song = newsong.split('\n')
    transposition_function(seventhchordsharps)
    song = newsong.split('\n')
    transposition_function(minorseventhchordsharps)
    song = newsong.split('\n')
    transposition_function(augmentedchordsharps)
    song = newsong.split('\n')
    transposition_function(diminishedchordsharps)
    song = newsong.split('\n')
    transposition_function(sus4chordsharps)
    song = newsong.split('\n')
    transposition_function(add9chordsharps)

writesongfile.write(newsong)
writesongfile.close()
