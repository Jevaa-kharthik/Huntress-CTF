import socket
import time

def connect_to_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def send_move(sock, move):
    sock.sendall(move.encode('utf-8'))
    time.sleep(1)  # Allow time for the server to process the move

def receive_response(sock):
    response = sock.recv(4096).decode('utf-8')
    print("Raw response:", response)  # Print raw response for debugging
    return response.splitlines()  # Split response into individual lines

def parse_opponent_move(lines):
    for line in lines:
        if "Opponent move:" in line:
            return line.split("Opponent move:")[1].strip()
    return None

def main():
    host = 'challenge.ctf.games'
    port = 31880  # Replace with the actual port from your challenge
    sock = connect_to_server(host, port)

    try:
        while True:
            # Get the opponent's move
            lines = receive_response(sock)
            parsed_move = parse_opponent_move(lines)

            # Default your_move in case of unknown opponent move
            your_move = 'block'  # Default move can be adjusted

            # Determine your move based on the opponent's move
            if parsed_move == "advance":
                your_move = 'retreat'
            elif parsed_move == "retreat":
                your_move = 'advance'
            elif parsed_move == "strike":
                your_move = 'block'
            elif parsed_move is None:
                print("Received unexpected message. Defaulting your move to 'block'.")

            send_move(sock, your_move)
            print(f"Your move: {your_move}")

            # Check for game-over conditions or disconnection
            for line in lines:
                if "You have been disconnected" in line:
                    print("Disconnected from the server.")
                    return
                if "死" in line:  # Indicates game over or similar message
                    print("Game over!")
                    return

    finally:
        sock.close()

if __name__ == "__main__":
    main()
