import grpc
import fileUploader
# import the generated classes
import sha1_pb2_grpc, sha1_pb2
import os

# open a gRPC channel
channel = grpc.insecure_channel('localhost:6666')

# create a stub (client)
stub = sha1_pb2_grpc.Sha1CheckerStub(channel)

# create a valid request message

file_name = ".txt_files/upload_this_file.txt"

generator_of_chunks = fileUploader.file_chunker(file_name)
response = stub.upload(generator_of_chunks)
print("Task  1: uploading a file")
print("SERVER_REPLY(size of file):", response)
print(
    "Check folder .txt_files for uploaded_file.txt. This is a replica of the the text file passed in by the client. \n")
print("---------------------------------------------------------------------------------------------------------------")
assert response.length == os.path.getsize(file_name)

inputData = sha1_pb2.FileData(filename=".txt_files/convert_to_sha1.txt", checksum=".txt_files/sha1_val.txt")

# make the call
response = stub.CheckSha1(inputData)
print("Task 2: calculate sha1 val of file and compare \n")
print("A result of 1 means the sha1 codes match")
print("A reuslt of 0 means the sha1 values dont match")
print("Calculated sha1: ", response.calculated_sha1)
print("CORRECT sha1: ", response.correct_sha1)
print("RESULT: ", response.result)
if response.result == 1:
    print("MATCH!\n")
else:
    print("NO MATCH\n")
