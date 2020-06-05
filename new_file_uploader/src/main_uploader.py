import grpc
import os
import file_chunk_pb2, file_chunk_pb2_grpc
import time
from concurrent import futures

size_of_chunk = 1024 * 1024


def file_chunker(file_name):
    with open(file_name, 'rb') as file:
        while True:
            part_of_file = file.read(size_of_chunk)
            if len(part_of_file) == 0:
                return
            yield file_chunk_pb2.Chunk(buffer=part_of_file)


def save_to_file(chunks, file_name):
    with open(file_name, 'wb') as file:
        for chunk in chunks:
            file.write(chunk.buffer)

class Client:
    def __init__(self, client_address):
        channel = grpc.insecure_channel(client_address)
        self.stub = file_chunk_pb2_grpc.FileUploaderStub(channel)

    def upload(self, file_name):
        generator_of_chunks = file_chunker(file_name)
        response = self.stub.upload(generator_of_chunks)
        print("SERVER_REPLY(size of file):", response)
        print(
            "Check folder for temp_file.txt. This is a replica of the the text file passed in by the client. \n")
        assert response.length == os.path.getsize(file_name)


class ServerForFile(file_chunk_pb2_grpc.FileUploaderServicer):
    def __init__(self):
        self.temp_file = "temp_file.txt"

    def upload(self, request_iterator, context):
        save_to_file(request_iterator, self.temp_file)
        size_of_file = os.path.getsize(self.temp_file)
        return file_chunk_pb2.Reply(length=os.path.getsize(self.temp_file))

    def startServer(self):

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        file_chunk_pb2_grpc.add_FileUploaderServicer_to_server(ServerForFile(), server)

        print('Starting server. Listening on port 8888.\n')
        server.add_insecure_port('[::]:8888')
        server.start()

        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            server.stop(0)
