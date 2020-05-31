import grpc
from concurrent import futures
import time
import os
import file_pb2, file_pb2_grpc, file_transfer


class FileServicer(file_pb2_grpc.FileActionServicer):
    def __init__(self):
        self.temp_file_name = 'temp_file.txt'

    def Upload(self, request_iterator, context):
        file_transfer.save_chunks_to_file(request_iterator, self.temp_file_name)
        return file_pb2.Reply(length=os.path.getsize(self.tmp_file_name))


def serve():
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # use the generated function `add_....._to_server`
    # to add the defined class to the server
    file_pb2_grpc.add_FileActionServicer_to_server(FileServicer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50061.')
    server.add_insecure_port('[::]:50061')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
