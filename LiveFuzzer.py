import socket
import random
import string

# Kullanıcıdan hedef sistem bilgilerini alma
target_host = input("Enter the target host IP address: ")
target_port = int(input("Enter the target port number: "))

# Fuzzing için rastgele veri üretimi
def generate_random_data(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Fuzzing işlemi
def perform_fuzzing():
    num_tests = 100
    vuln_count = 0
    
    for _ in range(num_tests):
        try:
            # Bağlantı kurma
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_host, target_port))

            # Rastgele veri oluşturup gönderme
            input_data = generate_random_data(random.randint(1, 100))
            client.send(input_data.encode())

            # Yanıtı al
            response = client.recv(4096)
            response_str = response.decode()
            
            if "VULNERABLE" in response_str:
                vuln_count += 1
                print(f"Sent: {input_data}, Received: {response_str}")
            else:
                print(f"Sent: {input_data}, Received: Success")

            client.close()

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    print(f"Total vulnerabilities found: {vuln_count}")

if __name__ == "__main__":
    perform_fuzzing()
