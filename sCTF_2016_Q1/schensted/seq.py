# Code adapted from: http://codereview.stackexchange.com/questions/33291/improving-efficiency-for-finding-longest-contiguous-non-decreasing-substring

def get_longest_non_decreasing(lowercase_str):
    '''
        Finds the longest non-decreasing sequence of
        characters within the given [lowercase] string.
    '''
    # Both the current sequence and result is the first character, for now.
    result = current_sequence = lowercase_str[0]

    # Start from the second character
    for character in lowercase_str[1:]:
        # If a character is greater or equal to the previous one
	# 89011356781923 => 01135678
        # if character >= current_sequence[-1]:
        #
        # OR
        #
	# If character is greater than the previous one
        # 89011356781923 => 135678
        # if character > current_sequence[-1]:

        # If a character is less than or equal to the previous one
        # 02349985543928 => 9985543
        # if character <= current_sequence[-1]:
        #
        # OR
        #
	# If a character is less than the previous one
	# 02348962191 => 9621
	# if character < current_sequence[-1]:

        if character >= current_sequence[-1]:
            # Append the character to the sequence
            current_sequence += character
        else:
            # Old sequence has been broken; new one begins
            current_sequence = character

        # Current non-decreasing sequence is longer than previous one
        if len(current_sequence) > len(result):
            # Update the result
            result = current_sequence

    # Return the longest non-decreasing substring
    print result

if __name__ == '__main__':
    with open("seq.dat") as file:
         seqNum = file.read()

    seq = list(seqNum)

    get_longest_non_decreasing(seq)
