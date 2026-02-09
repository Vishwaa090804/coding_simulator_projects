# Interactive Multiplication Table using micro:bit

## 📌 Project Overview
This project demonstrates an interactive multiplication table using a micro:bit.  
Users can explore number patterns, multiples, and positive/negative integers through button inputs and motion sensing.

---

## 🎯 Objectives
- To understand multiplication tables and number patterns
- To explore positive and negative integers
- To use event-driven programming with micro:bit
- To simulate an interactive math tool using Tinkercad

---

## 🧩 Components Used
- micro:bit (simulated)
- Button A
- Button B
- Accelerometer (Shake gesture)
- 5×5 LED display

---

## 🛠️ Tools & Technologies
- Tinkercad Circuits
- micro:bit
- MicroPython
- GitHub

---

## ⚙️ Working Principle
- **Button A**: Decreases the multiplier value  
- **Button B**: Increases the multiplier value  
- **Shake Gesture**: Toggles between positive and negative results  
- The LED display shows the result of **N × k**

---

## 🧮 Mathematical Concepts Used
- Multiplication tables
- Integers (positive and negative)
- Number patterns

---

## 🖼️ Circuit Design (Screenshot)


![Circuit Design](./Screenshot%202026-02-09%20133945.png)
![Code Blocks](./Screenshot%202026-02-09%20133629.png)

---
## How to Build the Project Using Blocks (Step-by-Step)

### Step 1: Refer the above diagram
Refer to the above diagram to see the micro:bit placed in the Tinkercad circuit.
No extra components or wires are needed because the micro:bit already has buttons and sensors.

---

### Step 2: Open Tinkercad and add micro:bit
1. Open the Tinkercad website.(https://www.tinkercad.com/)
2. Click on **Circuits**.
3. Click **Create New Circuit**.
4. From the components list, drag a **micro:bit** into the workspace.

---

### Step 3: Open the Code section and choose Blocks
1. Click on the **Code** button.
2. Select **Blocks** as the coding option.
3. You will see colorful coding blocks on the screen.

---

### Step 4: Create variables
1. Click on the **Variables** section.
2. Create three variables:
   - `N` (table number)
   - `k` (multiplier)
   - `sign` (positive or negative)

These variables help the micro:bit remember numbers.

---

### Step 5: Set starting values (On Start block)
1. Drag the **on start** block.
2. Set:
   - `N` to **5**
   - `k` to **1**
   - `sign` to **1**
3. Add a **show number** block to display the first result.

This shows the starting value of the multiplication table.

---

### Step 6: Program Button B (Next value)
1. Drag the **on button B pressed** block.
2. Inside it:
   - Change `k` by **+1**
   - If `k` is greater than **10**, set `k` back to **1**
3. Add a **show number** block to display the new result.

This helps move forward in the multiplication table.

---

### Step 7: Program Button A (Previous value)
1. Drag the **on button A pressed** block.
2. Inside it:
   - Change `k` by **-1**
   - If `k` is less than **1**, set `k` to **10**
3. Add a **show number** block to display the new result.

This helps move backward in the multiplication table.

---

### Step 8: Program Shake gesture (Positive / Negative)
1. Drag the **on shake** block.
2. Inside it:
   - Set `sign` to `sign × -1`
3. Add a **show number** block to display the updated result.

This changes the answer from positive to negative or negative to positive.

---

### Step 9: Understand the calculation
The number shown on the display is calculated as:
- `N × k × sign`

This means:
- `N` is the table number
- `k` is the multiplier
- `sign` decides positive or negative

---

### Step 10: Start the simulation
1. Click **Start Simulation**.
2. Press **Button A** or **Button B** to change values.
3. Shake the micro:bit to change the sign.
4. Watch the numbers appear on the display.

---
