def receive():
    import socket
    import tqdm
    import os

    file_save_path = input("Enter file path to save the file : ")
    if os.name == 'posix':
        my_address = input("Enter Your IP Address : ")
        file_save_path = file_save_path + '/'
    elif os.name == 'nt':
        my_address = socket.gethostbyname(socket.gethostname())
        file_save_path = file_save_path + '\\'
    else:
        print('This Script does not work in your os!!!')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((my_address,888))
    print("[+] Waiting for a connection... ")
    s.listen(5)
    def receive_file(client):
        file_name = client.recv(1024).decode()
        file_size = client.recv(1024).decode()
        
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(file_size))
        
        with open(file_save_path + file_name,"wb") as file:
            c=0
            while c<=int(file_size):
                data = client.recv(1024)
                if not(data):
                    break
                file.write(data)
                c+=len(data)
                progress.update(1024)

        if c == int(file_size):
            print("File Transfer Completed.")
        else:
            print("Error! File Transfer not completed.")

    while True:
        client,addr = s.accept()
        print(f"We got a connection from {addr}")
        receive_file(client)
        client.close()
        s.close()
        print('')
        print('----------------------------------------------------------------------------')

