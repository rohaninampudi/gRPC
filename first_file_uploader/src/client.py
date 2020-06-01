import grpc
import file_pb2
import file_pb2_grpc
import file_transfer
import os


# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = file_pb2_grpc.FileActionStub(channel)

file_name = "upload_this_file.txt"

# generate chunks of file to stream
generated_chunks = file_transfer.get_chunks(file_name)

# create a valid request message
response = stub.Upload(generated_chunks)
assert response.length == os.path.getsize(file_name)
# print(response)

