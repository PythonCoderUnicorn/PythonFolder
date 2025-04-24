

import pickle
import json

# Sample Python data structures
data = {
    "name": "Alice",
    "age": 30,
    "city": "Toronto",
    "hobbies": ["reading", "hiking", "coding"],
    "nested_data": {
        "occupation": "Engineer",
        "salary": 75000
    }
}

# --- Serialization Demos ---

print("--- Serialization Demos ---")

# 1. Using pickle (Python-specific serialization)
pickle_filename = "data.pkl"
try:
    with open(pickle_filename, "wb") as f:
        pickle.dump(data, f)
    print(f"Data serialized to {pickle_filename} using pickle.")
except Exception as e:
    print(f"Error during pickle serialization: {e}")

# 2. Using json (Language-independent serialization)
json_filename = "data.json"
try:
    with open(json_filename, "w") as f:
        json.dump(data, f, indent=4)  # indent for pretty printing
    print(f"Data serialized to {json_filename} using json.")
except Exception as e:
    print(f"Error during json serialization: {e}")

print("\n--- Deserialization Demos ---")

# --- Deserialization Demos ---

# 1. Using pickle
try:
    with open(pickle_filename, "rb") as f:
        loaded_data_pickle = pickle.load(f)
    print(f"Data deserialized from {pickle_filename} using pickle:")
    print(loaded_data_pickle)
    assert data == loaded_data_pickle, "Pickle: Original and loaded data do not match!"
    print("Pickle: Deserialization successful and data matches original.")
except FileNotFoundError:
    print(f"Error: {pickle_filename} not found for pickle deserialization.")
except Exception as e:
    print(f"Error during pickle deserialization: {e}")

# 2. Using json
try:
    with open(json_filename, "r") as f:
        loaded_data_json = json.load(f)
    print(f"\nData deserialized from {json_filename} using json:")
    print(loaded_data_json)
    assert data == loaded_data_json, "JSON: Original and loaded data do not match!"
    print("JSON: Deserialization successful and data matches original.")
except FileNotFoundError:
    print(f"Error: {json_filename} not found for json deserialization.")
except Exception as e:
    print(f"Error during json deserialization: {e}")


"""
Serialization (Writing data to a file):

pickle:

We import the pickle module.
We define a sample Python dictionary data.
We open a file in binary write mode ("wb") with the filename data.pkl.
pickle.dump(data, f) writes the data object to the file f in a binary format specific to Python. This format can preserve complex Python objects, including custom classes.
json:

We import the json module.
We open a file in write mode ("w") with the filename data.json.
json.dump(data, f, indent=4) writes the data object to the file f in JSON (JavaScript Object Notation) format.
JSON is a text-based, language-independent format, making it suitable for data exchange between different systems and languages.
The indent=4 argument makes the JSON output more human-readable with indentation.
JSON has limitations in the types of Python objects it can directly serialize. It primarily supports basic data types like dictionaries, lists, strings, numbers, and booleans.
Deserialization (Reading data from a file):

pickle:

We open the data.pkl file in binary read mode ("rb").
loaded_data_pickle = pickle.load(f) reads the data object from the file. The pickle.load() function reconstructs the Python object that was previously serialized.
We then print the loaded data and assert that it's equal to the original data.
json:

We open the data.json file in read mode ("r").
loaded_data_json = json.load(f) reads the JSON data from the file and parses it into Python dictionaries and lists.
We print the loaded data and assert that it's equal to the original data.


You will see output in the console showing the serialization and deserialization processes, and two files (data.pkl and data.json) will be created in the same directory. You can open these files to inspect the serialized data.

Key Differences between Pickle and JSON:

Language Dependence: Pickle is Python-specific. Data serialized with pickle can generally only be deserialized by Python. JSON is language-independent and widely supported across different programming languages and platforms.
Human Readability: JSON is text-based and human-readable. Pickle produces a binary format that is not easily understandable by humans.
Object Type Support: Pickle can serialize a wider range of Python objects, including custom classes, functions, and more complex structures. JSON has limitations on the types of objects it can directly handle.
Security: Deserializing data from untrusted sources using pickle can be a security risk, as it can execute arbitrary Python code. JSON is generally safer in this regard as it only deals with data structures.
Use Cases:
Pickle: Best for serializing and deserializing Python objects within Python applications, especially when preserving the exact state and type of objects is important.
JSON: Ideal for data exchange between different systems, web APIs, configuration files, and when human readability and language independence are required.


==========================
In summary, the best way to deal with potential cybersecurity issues of a pickle file 
is to avoid loading them from untrusted sources altogether. If you must handle data 
from external sources, prefer safer, text-based formats like JSON or structured binary 
formats like Protocol Buffers or Avro. If you absolutely have to work with pickle files 
from less trusted origins, do so in isolated environments and with extreme caution.



 how to check for and deal with potential cybersecurity issues related to pickle files:

1. Recognize the Risk:

Arbitrary Code Execution: The primary risk is that a malicious pickle file can be crafted to execute arbitrary code on your machine when it's loaded using pickle.load(). This code could do anything, from stealing data to installing malware.
Object State Manipulation: A carefully crafted pickle file could also be used to manipulate the state of existing objects in your program in unintended and potentially harmful ways.

2. Source of the Pickle File is Paramount:

Only Load from Trusted Sources: The absolute most crucial rule is to only load pickle files that you have created yourself or that come from a completely trusted and verified source. Treat pickle files from unknown or untrusted origins as potentially dangerous executables.   

3. Static Analysis (Limited Effectiveness):

Inspecting the File (Difficult): Unlike text-based formats like JSON, pickle files are in a binary format, making manual inspection very difficult and generally not helpful for identifying malicious content.   
Scanning with Security Tools (Limited): While some general-purpose security scanners might flag certain suspicious binary patterns, they are unlikely to have specific signatures for malicious pickle payloads. Relying solely on antivirus or malware scanners is not sufficient.

4. Sandboxing and Isolation (More Effective but Complex):

Virtual Machines or Containers: If you absolutely must inspect a pickle file from a less trusted source, do so within a tightly controlled and isolated environment like a virtual machine or a container (e.g., Docker). This limits the potential damage if the file contains malicious code.   
Restricted Python Environments: You could try loading the pickle file in a Python environment with severely restricted permissions and limited access to system resources. However, setting this up correctly can be complex.

5. Alternatives to Pickle for Data Exchange:

JSON: For general data serialization and exchange, especially with external systems or when security is a concern, JSON is a much safer alternative. It's text-based and doesn't allow for arbitrary code execution during deserialization.   
CSV: For tabular data, CSV (Comma Separated Values) is a simple and safe format.
Protocol Buffers (protobuf) or Apache Avro: For more structured and efficient data serialization with schema definitions, consider using libraries like protobuf or avro. These formats are designed for data exchange and don't inherently pose the same code execution risks as pickle.   
Database Systems: If you are dealing with persistent data, using a proper database system provides much better security and data management capabilities.

6. Secure Practices if You Must Use Pickle (Within Trusted Environments):

Integrity Checks (Hashing): If you are transferring pickle files even within a trusted environment, consider generating a cryptographic hash (e.g., SHA-256) of the file after serialization. Before deserialization, recalculate the hash and compare it to the original to ensure the file hasn't been tampered with.   
Code Reviews: If your application relies heavily on pickle, have the serialization and deserialization code reviewed by security-conscious developers.
Minimize Deserialization of Untrusted Input: Avoid deserializing data directly from user input or external, potentially compromised sources into pickle format.   


"""