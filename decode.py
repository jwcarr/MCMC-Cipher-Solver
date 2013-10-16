from random import randrange, shuffle
from string import maketrans
from sys import argv

# Dictionary of common words and bigrams with their frequencies in Moby Dick
common = {'all': 2828, 'think': 180, 'just': 123, 'when': 577, 'over': 646, 'go': 1046, 'its': 548, 'ld': 2361, 'le': 8012, 'also': 85, 'had': 814, 'day': 296, 'to': 7020, 'only': 372, 'th': 29424, 'ti': 4866, 'has': 419, 'do': 1553, 'them': 530, 'his': 3907, 'get': 242, 'de': 4784, 'know': 331, 'they': 572, 'not': 1466, 'now': 1030, 'him': 1267, 'like': 685, 'this': 1273, 'good': 200, 'she': 523, 'because': 73, 'people': 42, 'ed': 9071, 'ea': 6270, 'back': 208, 'up': 1462, 'see': 1004, 'are': 1001, 'year': 116, 'et': 3069, 'es': 7922, 'out': 1429, 'even': 303, 'what': 510, 'for': 2448, 're': 11436, 'ra': 3305, 'then': 592, 'new': 123, 'be': 3825, 'we': 2533, 'who': 616, 'use': 372, 'come': 255, 'by': 1290, 'on': 8971, 'about': 310, 'ol': 2311, 'would': 427, 'of': 7119, 'could': 221, 'ou': 8303, 'or': 7667, 'first': 207, 'into': 529, 'one': 1640, 'en': 8647, 'cr': 1269, 'your': 275, 'he': 25586, 'from': 1039, 'her': 3411, 'there': 802, 'two': 289, 'been': 408, 'their': 610, 'way': 660, 'was': 1655, 'that': 2943, 'some': 888, 'but': 1167, 'hi': 9296, 'ha': 10966, 'with': 1907, 'than': 424, 'must': 289, 'me': 5591, 'made': 177, 'look': 322, 'these': 373, 'work': 122, 'say': 329, 'us': 3058, 'ur': 3135, 'will': 389, 'te': 6840, 'can': 528, 'were': 716, 'my': 738, 'and': 7377, 'give': 126, 'is': 8238, 'it': 7435, 'an': 14394, 'as': 6775, 'ar': 7611, 'at': 9948, 'have': 757, 'in': 19065, 'any': 591, 'if': 1222, 'want': 65, 'no': 3773, 'make': 157, 'nd': 10732, 'ng': 9771, 'how': 422, 'other': 632, 'take': 222, 'which': 623, 'you': 1204, 'er': 14419, 'nt': 5299, 'our': 941, 'after': 296, 'most': 532, 'the': 18475, 'well': 217, 'st': 7883, 'si': 2686, 'so': 3161, 'time': 570, 'sa': 2021, 'se': 6480}

#############################################################################
#   DECODES A SPECIFIED CIPHER TEXT FILE AND PRINTS THE PLAIN TEXT

def decode(filename, trials=30, swaps=3000):
    # Load the file.
    print "\n  * Loading file...\n"
    cipherText = load(filename)
    # Remove any spaces in the cipher text.
    cipherText = cipherText.replace(" ", "")
    # Ensure the cipher text is lower case.
    cipherText = cipherText.lower()
    # Find the best key to unlock the cipher text.
    print "  * Finding a good key to unlock the file...\n"
    key = search(cipherText, trials, swaps)
    # Transform the cipher text into plain text.
    plainText = transform(cipherText, key)
    # Print the plain text.
    print "  * File decoded:\n"
    print plainText

#############################################################################
#   PERFORMS A RANDOM WALK AROUND THE SPACE OF POSSIBLE KEYS AND RETURNS THE
#   BEST FITTING KEY

def search(cipherText, trials, swaps):
    # Set up default key.
    key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Set bestScore to zero.
    bestScore = 0
    # For each trial...
    for i in range(0, trials):
        # Shuffle key into a random permutation,
        shuffle(key)
        # Set bestTrialScore to zero,
        bestTrialScore = 0
        # For each swap...
        for j in range(0, swaps):
            # Swap two letters in the key and call this newKey,
            newKey = swap(key[:])
            # Measure how good newKey is and call this newScore,
            newScore = score(newKey, cipherText)
            # If newScore is better than bestTrialScore...
            if newScore > bestTrialScore:
                # ...then make key equal to newKey...
                key = newKey[:]
                # ...and make bestTrialScore equal to newScore.
                bestTrialScore = newScore
            # But if newScore is the same as bestTrialScore...
            elif newScore == bestTrialScore:
                # ...and if the flip of a coin comes up tails...
                if randrange(0,2) == 1:
                    # ...then accept newKey anyway.
                    key = newKey[:]
        # If the best score for that trial was better than the all time best score...
        if bestTrialScore > bestScore:
            # ...then make key the bestKey... 
            bestKey = key[:]
            # ...and make bestScore equal to bestTrialScore.
            bestScore = bestTrialScore
    # Return the best key found in this random walk.
    return bestKey

#############################################################################
#   TAKES A KEY AND SWAPS TWO OF ITS VALUES AT RANDOM

def swap(key):
    # Pick a random number between 0 and 25.
    i = randrange(0, 26)
    # Now pick another random number between 0 and 25.
    j = randrange(0, 26)
    # If and while the two numbers happen to be the same...
    while i == j:
        # ...keep trying to pick a second random number that's not equal to the first.
        j = randrange(0, 26)
    # Swap the two items in the key that are indexed by these random numbers.
    key[i], key[j] = key[j], key[i]
    # Return the new key.
    return key

#############################################################################
#   SCORES THE QUALITY OF A KEY FOR A GIVEN TEXT

def score(key, cipherText):
    # Transform the text using the key.
    candidate = transform(cipherText, key)
    # Set initial score to zero.
    scr = 0
    # For each item in the dictionary of common words and bigrams...
    for item in common.iterkeys():
        # ...count the number of times the item occurs, multiply by its frequency
        # in Moby Dick, and add to the running score.
        scr = scr + candidate.count(item) * common[item]
    # Return the overall score.
    return scr

#############################################################################
#   TRANSFORMS AN ENCRYPTED TEXT USING A GIVEN KEY

def transform(cipherText, key):
    return cipherText.translate(maketrans("".join(key), 'abcdefghijklmnopqrstuvwxyz'))

#############################################################################
#   OPENS A FILE AND RETURNS ITS CONTENT

def load(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text

#############################################################################
#   ON RUN, IMPORT ARGUMENTS FROM THE COMMAND LINE AND PASS TO DECODE()

if __name__ == '__main__':
    arguments = len(argv)
    
    if arguments == 4:
        decode(str(argv[1]), int(argv[2]), int(argv[3]))
        
    elif arguments == 3:
        decode(str(argv[1]), int(argv[2]))
        
    elif arguments == 2:
        decode(str(argv[1]))
        
    elif arguments == 1:
        print "Error: Please specify a file to decode."
        
    else:
        print "Error: Too many arguments. This program takes a maximum of 3 arguments - the file name, number of trials, and number of swaps."
