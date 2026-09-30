# **#CanYouSee**

## **#Approach**

Same as any other forensic chall with an image, I started with running exiftool on the image in kali, and got a base64 in Attribution URL, decoding which gave me the flag. This was pretty straightforward.

## **#SOLUTION**

We are given an image



!\[image](images/ukn\_reality.jpg)



Running exiftool on this image provides us with the metadata of the image. Of peculiar interest, is a specific field in this



!\[image](images/img1.png)



Attribution URL: has a a Base64 value, **YWNhZGVteXtXtNRTc0RDQ3QV9ISUREM05fYWViZThjMGZ9Cg==**



Decoding this using dcode.fr gives us the flag.

## **#FLAG**

**academy{ME74D47A\_HIDD3N\_aebe8c0f}**

## **TAKEAWAY**

Exiftool is a very helpful command as most challs in forensics with images will have something useful in their metadata.



