---
title: "Polished Amethyst"
author: "bcon"
description: "second iteration of my keyboard with more features"
created_at: "2025-07-04"
---
Total Time Spent: 15 Hours

## **7/4/2025-7/5/2025 Log 1: A Fresh Start**

I decided that I was not happy with my original keyboard design, and while I liked the aesthetic of the keyboard, it had a lot of flaws. So, I decided to start completely fresh. 

In this new design, I wanted to make a few changes.

Cleaner silkscreen: No mess of random numbers and labels everywhere, if there is silkscreen it is either decorative or has a real purpose

OLED Screen: I want an OLED screen built in along with the rest of the features in the first version

Better Case: I want a case that is more than a rectangle. Something open frame perhaps.

I opened KiCAD and dove right into the schematic.

![Screenshot 2025-07-05 110432](https://github.com/user-attachments/assets/c036f356-49f8-4827-bf38-0892f09ada30)

This has north facing per key LEDs, a 10x10 matrix, rotary encoder, and screen all set with footprints. A Pi Pico is the controller for this entire project.

From there, I went to the PCB editor.

![Screenshot 2025-07-05 111722](https://github.com/user-attachments/assets/88834748-e672-4b54-9b50-63d93c535258)

I laid out my keyboard layout, and started putting the leds on the board, but only made it halfway. 

Time Spent: 5 Hours

## **7/6/2025 Log 2: Finishing the PCB**:

I did more work on the PCB, including adding a few new things, along with routing the entire PCB. This took me the WHOLE DAY. 

![image](https://github.com/user-attachments/assets/265cd7b2-ea95-464d-a6b7-0258a4c38637)

I added in a ground pour to better connect my ground lines, and added in a 330 Ohm resistor in the LED data line to improve the signal integrity of the data line. I also added in a 1000uF capacitor to stabilize the power going into the LEDs. I did end up having to restart everything halfway through to redo the traces for the pico as I wanted to flip it to the other side. 

From there, I exported the board and started putting it into CAD. 

![image](https://github.com/user-attachments/assets/6e82dfc9-7515-47d6-b45a-c57d3e581e7f)

After exporting the board in, I started to populate the board with switches and keycaps, along with my board. I am going to mount my board from the bottom to work with the case style I am thinking of. 

TIme Spent: 6 Hours

## **7/6/2025 Log 3: Finishing Touches**

I finished up both my case and added on some nice silkscreen to my PCB. 

![image](https://github.com/user-attachments/assets/e70c8df7-1a85-42e4-9d1c-8ad9237584dd)
![image](https://github.com/user-attachments/assets/1117a05c-eb57-4645-b721-9eadb7d98bec)

These decals add a little bit of personal branding into the pcb and will help it stand out in the case.

Regarding the case, I went for an open air design to really show off the pcb. 

![image](https://github.com/user-attachments/assets/dcf1756f-c86c-4249-89f5-4b5e938a9c41)

The PCB bolts in with 6 brass standoffs at the edges. However, due to concerns of the PCB bending in the middle during heavy use, I added spots to place more standoffs that, while do not bolt into the pcb, still support it from force from above. I have added many places to put said standoffs to spread the load from use. The case itself will be printed in hopefully one part on a belt printer, and has a 5 degree slope to permit better typing posture.

![image](https://github.com/user-attachments/assets/27edfd91-3a42-49ee-9c5e-428bdac01bad)

The best thing about this being printed is I can easily reprint it to tweak the angle. Not pictures here, but there will also be some friction feet to keep the keyboard in its location. I also put the raspberry pi pico upside down for better packaging. 

Without further ado, here is the finished product.
![Polished Amethyst](https://github.com/user-attachments/assets/8dd95bd7-966e-42f5-b11d-b68fa0f9e53b)

TIme Spent: 4 Hours
