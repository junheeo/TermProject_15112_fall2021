This app is a text editor that supports two types of encryption - AES and RSA.

Run this app by running app.ui_py on python3

There are no external libraries to be installed to use this app.

Documents only in the TermProject directory are editable.

There are no shortcut commands available. However, one could usually return back to the text editor by clicking 'x' on the keyboard



How to use the app:

Run app.ui.py as python3

The user may extend the size of the app both horizontally and vertically with a cursor.


Change Edit point : Use cursor to click onto position to make edit. Obviously, editing is only possible where characters are previously placed. The editing point is colored in black. If there is a word under editing point, the character will be colored in white.


Temporary Highlight : Use arrow keys (left, right, up, down) to highlight text temporarily. Combinations of arrow keys are not supported. Highlighting on \n enter spaces are not supported. User can exit highlight mode by clicking on a desired editing point.


Copy & Paste : When character(s) are highlighted, if the user presses c on the keyboard, copy&paste mode starts. In this mode, text editing does not work. However, if the user desires to exit copy&paste mode, the user can press x on the keyboard. If the user wants to proceed with the copy&paste mode, the user may or may not change the editing position by clicking onto a position and then press v on the keyboard. This would result in pasting the copied text and the editor would return back to text editing mode.


Save text : If the user wants to save the text currently in the text editor, the user can simply click the Save button in the upper right corner of the app. Then, the user have to type in file name. In cases where the file is a opened preexisting file or if the file has been saved previously, the previously given name will appear as default. The user may or may not change the file name. If file name has been typed, the user can press enter and the file will be saved.


Open file : If the user hopes to open a text file, the user can simply click the Open button at the top. If the user wants to exit the open menu, the user can press x. If the user wants to open a file, the user can press the yellow folder icon at the left of the file name. This will open the file in the test editor.


Encryption with AES : If the user hopes to encrypt the text file with AES encryption, the user can simply click the aesEncrypt button at the top of the app. Then the user should press at least 16 keys from the keyboard as encryption key. Characters beyond that will not count, string below that will cause an error. Press Enter to encrypt, press x to return back to the editor. The encrypted text will appear on the text editor if the encryption is done.

Decryption with AES : If the user hopes to decrypt a text with AES, the user can click aesDecrypt on the top. The key used previously will be shown by default. If there is need to change the key, user can delete and type the key user wants. Press Enter to decrypt, press x to return back to editor.

Create keys for RSA : new keys for RSA can be created by clicking create rsaKeys button at the top. User cannot exit once the user clicks this button as the app starts creating new keys. Once the new keys are shown on the app, user may press x to return back to editor. These new keys are stored in the app.

Encrypt plain text with RSA : click rsaEncrypt button at the top. Once the app shows the keys, the user can press Enter to encrypt or press x to exit back to the editor. If pressed Enter, the encrypted text will appear on the text editor.

Decrypt plain text with RSA : click rsaDecrypt button at the top. Once the app shows the keys, the user can press Enter or press x to return back to the editor. If press Enter, the cipher text will be decrypted back to plain text.

Send public key to another app : click send rsa PublicK button at the top. Edit hostname is needed, and then press Enter. Then edit port number. Port number should almost always be changed in order to avoid "Address already in use" error, then press enter. The app will wait until the app finds a receiver of the keys. If verified that another app is connected, then press enter to return back to editor.

Receive public key from another app : click receive rsa PublicK button at the top. Edit hostname so that it is the DNS address or IP address of the server app that this app is retrieving public key from. Press Enter. Edit port number so that it matches the port number of the server app that this app is retrieving the public key from. Then press Enter. If verified that the app has received the message, press enter to return back to editor.
