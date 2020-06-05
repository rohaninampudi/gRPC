# SHA-1 gRPC OVERVIEW:
    This program takes in input from the client:
        file name of file that incluedes some data
        file name of file that that has the correct sha1 value
        
    The server will return:
        An integer (0 or 1) indicating whether the sha1 hash matches or not
        The calculated sha1 hash of the file given
        The actual sha1 hash (the hash it was compared to)
        
# To compile 
    Generate the gRPC files using: (must be in proto directory)
        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sha1.proto
        
    Compile the server and client (in src directory):
        python server.py
        python client.py 
     
        