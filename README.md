BasicHoney is a honeypot used to display blocks of text to whomever is connected. The script takes the following inputs:

* Port
* Filename
* Delimiter

Once the inputs have been entered the script will do the following:

1. Create a socket with the provided port
2. Open and read the provided file
3. Split the file contents with the provided delimiter
4. Listen for connections

When a user connects to the socket the script will send a block of text and wait for a response before sending more.