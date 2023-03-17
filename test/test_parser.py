"""
edge cases:
- new line in the middle of a chunk
- chunk length could be multiple bytes
- in hexadecimal
"""

CHUNK_DELIMITER_LENGTH = 2

def parse_chunked_input(input_string: str):
    next_chunk_start_index = 0
    full_message = ""
    while True:
        first_chunk_length_end = input_string.find("\r\n", next_chunk_start_index)
        chunk_length = input_string[next_chunk_start_index:first_chunk_length_end]
        chunk_length_as_int = int(chunk_length, 16)
        if chunk_length_as_int == 0:
            break
        chunk_index_beginning = first_chunk_length_end+2
        chunk_index_end = chunk_index_beginning + chunk_length_as_int
        chunked_message = input_string[chunk_index_beginning:chunk_index_end]
        full_message += chunked_message
        next_chunk_start_index = chunk_index_end + CHUNK_DELIMITER_LENGTH
    return full_message


input_string_example = "7\r\nAtomic \r\nA\r\nis hiring \r\n8\r\nawesome \r\n9\r\nengineers\r\n0\r\n\r\n"

second_string_input = "7\r\nAtomic \r\nB\r\nis hiring\r\n\r\n8\r\nawesome \r\n9\r\nengineers\r\n0\r\n\r\n"

poem_input = "8F\r\nA venture studio with a dream,\r\nAtomic Labs is the perfect team.\r\nThey found and fund companies you see,\r\nAnd offer a great engineering team.\r\n\r\n2\r\n\r\n\r\nA1\r\nA group of techies, great and bold,\r\nTheir ideas are worth more than gold.\r\nTheir knowledge and experience will unfold,\r\nMaking the best of what they are told.\r\n\r\n2\r\n\r\n\r\n96\r\nThey offer tools to start anew,\r\nHelping entrepreneurs to make it through.\r\nTheir tech know-how and skills are true,\r\nForging a path that is so new.\r\n\r\n2\r\n\r\n\r\n8F\r\nA place of dreams, a place of hope,\r\nAtomic Labs provides a way to cope.\r\nTo build on ideas and to elope,\r\nForging futures that can't be broke.\r\n0\r\n"

def test_parse():
    response = parse_chunked_input(poem_input)
    print(response)