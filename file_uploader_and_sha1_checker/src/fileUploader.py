import sha1_pb2_grpc
import sha1_pb2

size_of_chunk = 1024 * 1024


def file_chunker(file_name):
    with open(file_name, 'rb') as file:
        while True:
            part_of_file = file.read(size_of_chunk)
            if len(part_of_file) == 0:
                return
            yield sha1_pb2.Chunk(buffer=part_of_file)


def save_to_file(chunks, file_name):
    with open(file_name, 'wb') as file:
        for chunk in chunks:
            file.write(chunk.buffer)
