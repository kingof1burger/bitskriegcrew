# **#Autorev 1**

## **#APPROACH**

We have an instance, connecting to which gives us a big dump of hex hidden in which is our key, but just where exactly. This one was a tough nut to crack. first thing i did was convert the hex into something that can be broken down. Specifically, i need to find the point where 'key' is present in this dump. I know this because i tried entering the whole dump and it just kicked me off the connection, so the key isn't the whole dump, its some part of it.



so, i stored the dump in a hex file which i converted into an elf file, to run on ghidra. 

Finding the main() function in ghidra, we see that at a very specific location (which remains the same for each new dump), the key is present. All that was left was entering this digit. 



But when I entered it in its field of "Whats the secret?:", I found that my connection closes. This is because I can't humanely enter the secret key fast enough. And this is where the trouble started, because from this point on I had to do rev coding, which I don't even know. With the help of youtube, and learning how to use the **re** module, and with an hour of just slamming my head on python, I was finally able to write a concise solve.py, running which gave me the flag.

## **#SOLUTION**

First things first, we connect to the instance.



!\[image](images/img1.png)



and below the whole dump, it asks,


!\[image](images/img2.png)



First we will store the long dump in a file "**dump.hex**"



Then, we will convert that file into an ELF file, which is executable on Ghidra for disassembly.



**xxd -r -p dump.hex bin.elf**



In Ghidra, we find in main()



!\[image](images/img3.png)



Here local\_c is the secret key.



!\[image](images/img4.png)



This tells us that (in Little Endian Format), the secret key is always stored at **c7 45 fc**

In the next line is written **57 89 c7 db**

This is the value of secret hex that we need, so if idx starts at c7, we need idx+3 to idx+7.



To code, this can be set up as

**idx = binary\_bytes.find(b'\\xc7\\x45\\xfc')**

**return int.from\_bytes(binary\_bytes\[idx+3:idx+7], byteorder='little')**



Now that we have our secret hex stored, we just need to loop it as input



!\[image](images/img5.png)



Here, text is just anything that the instance provided after whats the secret, and hex\_data includes a classic way to search for large dumps and store them. This hex is converted to binary, on which we run our extract\_secret function. Then, to handle EOFError, inside the loop we will keep doing this until EOF is reached, after which we enter interactive mode to obtain the flag.



!\[image](images/img6.png)



## **#FLAG**

**academy{4u7o\_r3v\_g0\_brrr\_78c345aa}**

## **#TAKEAWAY**

re is a very helpful module when you need to search through large blobs of texts or store large blobs of texts which follow a specific order. Other than this, storing and disassembling text that seems incomprehensible usually provides logic to the chaos. Stick close to disassembly tools, they are your greatest friends. Also, learn how to code rev, lest you suffer :(.











