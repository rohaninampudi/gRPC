
import file_pb2, file_pb2_grpc

size_of_chunk = 1024 * 1024  # = 1MB


def get_chunks(filename):  # gets part of file
    with open(filename, 'rb') as file:
        while True:
            part_of_file = file.read(size_of_chunk)
            if len(part_of_file) == 0:
                return
            yield file_pb2.Chunk(buffer=part_of_file)
            # use yield bc it suspends func execution and send back value but retains enough ste to enable function to resume where it let off. This allows the funtion to continue execution after the last yield run, producing a series of values overtime.


def save_chunks_to_file(chunks, filename):
    with open(filename, 'wb') as file:
        for chunk in chunks:
            file.write(chunk.buffer)