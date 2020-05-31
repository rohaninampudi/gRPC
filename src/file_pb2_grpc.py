# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import file_pb2 as file__pb2


class FileActionStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.stream_unary(
                '/FileAction/Upload',
                request_serializer=file__pb2.Chunk.SerializeToString,
                response_deserializer=file__pb2.Reply.FromString,
                )


class FileActionServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileActionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.stream_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=file__pb2.Chunk.FromString,
                    response_serializer=file__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileAction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileAction(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FileAction/Upload',
            file__pb2.Chunk.SerializeToString,
            file__pb2.Reply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
