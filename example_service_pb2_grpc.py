# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_service_pb2 as example__service__pb2


class StreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamDecode = channel.stream_stream(
                '/StreamService/StreamDecode',
                request_serializer=example__service__pb2.DecodeRequest.SerializeToString,
                response_deserializer=example__service__pb2.DecodeResult.FromString,
                )


class StreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamDecode(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamDecode': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamDecode,
                    request_deserializer=example__service__pb2.DecodeRequest.FromString,
                    response_serializer=example__service__pb2.DecodeResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamDecode(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/StreamService/StreamDecode',
            example__service__pb2.DecodeRequest.SerializeToString,
            example__service__pb2.DecodeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)