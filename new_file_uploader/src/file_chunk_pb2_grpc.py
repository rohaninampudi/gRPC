# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import file_chunk_pb2 as file__chunk__pb2


class FileUploaderStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.upload = channel.stream_unary(
                '/FileUploader/upload',
                request_serializer=file__chunk__pb2.Chunk.SerializeToString,
                response_deserializer=file__chunk__pb2.Reply.FromString,
                )


class FileUploaderServicer(object):
    """Missing associated documentation comment in .proto file"""

    def upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileUploaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'upload': grpc.stream_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=file__chunk__pb2.Chunk.FromString,
                    response_serializer=file__chunk__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileUploader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileUploader(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FileUploader/upload',
            file__chunk__pb2.Chunk.SerializeToString,
            file__chunk__pb2.Reply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)