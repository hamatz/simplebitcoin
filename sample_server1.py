import signal
import sys

from core.server_core import ServerCore

my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()

def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def main(my_port, p_phrase, my_pem_path):
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server
    # 始原のCoreノードとして起動する
    if my_pem_path != 'None':
        my_p2p_server = ServerCore(my_port, None, None, p_phrase, my_pem_path) 
    else:
        my_p2p_server = ServerCore(my_port, None, None, p_phrase)
    my_p2p_server.start()


if __name__ == '__main__':
    args = sys.argv
 
    if len(args) == 4:
        my_port = int(args[1])
        p_phrase = args[2]
        my_pem_path = args[3]
    else:
        print('Param Error')
        print('$ SmpleServer1.py <my_port> <pass_phrase_for_keys> <path_for_pem_file>')
        quit()

    main(my_port, p_phrase, my_pem_path)