# gRPC file uploader instructions:
    USE THE PROJECT IN "new_file_uploader"
    
    Change directory to "proto" before executing the statement below
    
    Use the following command to create the pb2 files:

        python -m grpc_tools.protoc -I. --python_out=../src --grpc_python_out=../src ./file_chunk.proto

    Change directory to "src" to run the server and client
    
        python test_server.py
        
        OPEN a new terminal then run the client:
    
        python test_client.py


# What the program does:
    The client passes the contents of "upload_this_file.txt" to the server and the server will upload it.

    To prove that it has been uploaded, the server should create a another file named "temp_file.txt"
    Server will also return the size of file to validate.


# This is the bug in the first_file_uploader project (i'm not sure how to fix)
    Currently there is a bug when running the client (shown below):


    Traceback (most recent call last):
    File "/Users/rohaninampudi/PycharmProjects/grcp/gRPC_File_Uploader/src/client.py", line 19, in <module>
        response = stub.Upload(generated_chunks)
    File "/Users/rohaninampudi/PycharmProjects/grcp/venv/lib/python3.8/site-packages/grpc/_channel.py", line 1011, in __call__
        return _end_unary_response_blocking(state, call, False, None)
    File "/Users/rohaninampudi/PycharmProjects/grcp/venv/lib/python3.8/site-packages/grpc/_channel.py", line 729, in _end_unary_response_blocking
        raise _InactiveRpcError(state)
    grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.UNKNOWN
        details = "Exception calling application: 'FileServicer' object has no attribute 'tmp_file_name'"
        debug_error_string = "{"created":"@1590898466.709939000","description":"Error received from peer ipv6:[::1]:50061","file":"src/core/lib/surface/call.cc","file_line":1056,"grpc_message":"Exception calling application: 'FileServicer' object has no attribute 'tmp_file_name'","grpc_status":2}"


# Because of this bug make sure to use the "new_file_uploader"


## TODO
  [] Final Backend server to be implemented in c++/golang
     - Python is fine for initial version
  [] Client component can be any lanugage python/c++/golan

## Flow
  []  Client to send file data, filename, file checksum(sha1 value of content)
  []  Server recieves, calculates sha1 value and compares with the sha1 recieved
  []  test the flow with images and binary files
  []  Bring seesions into flow. cleints start a session, server responds with session id. 
      clients uses sessionid for further processing of api calls. 
      client at the end closes the sessions.
      expiry of each session.
      
## Inference flow
  - create session -
  - send image / model file 
  - infer image
  - get inference result
  - repeat 
  - close session
  
