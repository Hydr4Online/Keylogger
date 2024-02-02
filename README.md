# Keylogger
A script to capture the keys in Python

<h1> Recommendations </h1>

- Modify and verify that the IP is correct
- Modifying the Linux Machine Port in Listening
- Check your network connection type on the attacking linux machine if it doesn't capture the keys in nc
  according to the one that best suits your network with the keylogger Example: briged,Nat,Host-only 

<h2> Steps to make the script work </h2>

1- Open your linux machine connected to the same network as the victim machine where the keylogger is hosted

2- Check that the ip and port in the script are correct and run nc before starting the scrypt

direccion_ip_destino = '127.12.12.10' --> Attacker's IP
puerto_destino = 8000 --> Listen port with NetCat

3- Once listening, run the script and type any text should appear on the screen,
everything that is being written should appear on the screen




