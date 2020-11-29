import argparse
import socket

BUFFSIZE = 1024


def get_cli_args():
    parser = argparse.ArgumentParser(description="Enumerate an FTP endpoint for valid users")
    parser.add_argument('hostname', type=str, metavar='Hostname', help='Host IP of the FTP server')
    parser.add_argument('userfile', type=str, metavar='userfile', help='List of users to enumerate')
    parser.add_argument('-p', '--port', type=int, metavar='Port', default=21,
                        help='FTP server Port (defaults to %(default))')

    return parser.parse_args()


def read_socket_response(socket):
    response = ""
    while response[-2:] != '\r\n':
        data = socket.recv(BUFFSIZE)
        response = response + data.decode('ascii')

    return response


def create_control_socket(address):
    control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_socket.connect(address)
    return control_socket


def main():
    args = get_cli_args()
    control_socket = create_control_socket((args.hostname, args.port))
    read_socket_response(control_socket)
    with open(args.userfile) as f:
        for username in f:
            control_socket.send(f"USER {username}\r\n".encode())
            resp = read_socket_response(control_socket)
            if resp.startswith('331'):
                print(f"{username} --> found")


if __name__ == '__main__':
    main()
