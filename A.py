import os
import sys

# (i) Process Management
print("Process Management:")

pid = os.fork()

if pid == 0:
    # Child Process
    print("Child Process ID:", os.getpid())
    print("Child Parent ID:", os.getppid())

    print("Executing ls -l command:")
    os.execlp("ls", "ls", "-l")

else:
    # Parent Process
    print("Parent Process ID:", os.getpid())
    print("Parent's Parent ID:", os.getppid())

    os.wait()
    print("Child process completed.")


# (ii) File Management
print("\nFile Management:")

fd = os.open("sample.txt", os.O_CREAT | os.O_RDWR | os.O_TRUNC, 0o644)

data = b"Hello Linux!\nSystem Calls in Python.\n"

os.write(fd, data)

os.lseek(fd, 0, os.SEEK_SET)

content = os.read(fd, 100)

print("File Contents:")
print(content.decode())

os.close(fd)


# (iii) Input / Output
print("Input / Output:")

os.write(1, b"Enter a string: ")

string = os.read(0, 100)

os.write(1, b"You entered: ")
os.write(1, string)
