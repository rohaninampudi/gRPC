import grpc

# import the generated classes
import sha1_pb2_grpc, sha1_pb2


# open a gRPC channel
channel = grpc.insecure_channel('localhost:6666')

# create a stub (client)
stub = sha1_pb2_grpc.Sha1CheckerStub(channel)

# create a valid request message

inputData = sha1_pb2.FileData(filename="src/.txt_files/convert_to_sha1.txt", sha1_val="src/.txt_files/sha1_val.txt")

# make the call
response = stub.CheckSha1(inputData)


print("A result of 1 means the sha1 codes match")
print("A reuslt of 0 means the sha1 values dont match")
print("Calculated sha1: ", response.calculated_sha1)
print("CORRECT sha1: ", response.correct_sha1)
print("RESULT: ", response.result)
if response.result == 1:
    print("MATCH!\n")
else:
    print("NO MATCH\n")


