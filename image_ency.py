from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    data = np.array(image)
    
    # Encrypt the data by applying the XOR operation with the key
    encrypted_data = data ^ key
    
    # Convert the encrypted data back to an image
    encrypted_image = Image.fromarray(encrypted_data)
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    encrypted_image = Image.open(image_path)
    # Convert the image to a numpy array
    encrypted_data = np.array(encrypted_image)
    
    # Decrypt the data by applying the XOR operation with the key
    decrypted_data = encrypted_data ^ key
    
    # Convert the decrypted data back to an image
    decrypted_image = Image.fromarray(decrypted_data)
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
    output_path = input("Enter the output path for the processed image: ")

    if choice == 'encrypt':
        encrypt_image(image_path, key, output_path)
    elif choice == 'decrypt':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
