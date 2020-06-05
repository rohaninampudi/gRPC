import grpc
from concurrent import futures
import time

# import the generated classes
import sha1_pb2_grpc, sha1_calculator, sha1_pb2


# import the original sha1_calculator.py


# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class Sha1CheckerServicer(sha1_pb2_grpc.Sha1CheckerServicer):

    def CheckSha1(self, request, context):
        response = sha1_pb2.Result()
        response.result, response.correct_sha1, response.calculated_sha1 = sha1_calculator.calculate_and_compare_sha1(request.filename, request.checksum)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
sha1_pb2_grpc.add_Sha1CheckerServicer_to_server(
    Sha1CheckerServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 6666.')
server.add_insecure_port('[::]:6666')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
