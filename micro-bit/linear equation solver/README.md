# Linear Equation Solver using micro:bit

## 📌 Project Overview
This project solves linear equations of the form **ax + b = c** using a micro:bit.  
Users input the coefficients a, b, and c using buttons, then the micro:bit solves for x using the formula **x = (c − b) / a**.

---

## 🎯 Objectives
- To understand solving one-variable linear equations
- To apply the formula x = (c − b) / a
- To use event-driven programming with micro:bit
- To simulate a variable manipulator using Tinkercad

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
- **Button A**: Decreases the current variable value (a, b, or c)
- **Button B**: Increases the current variable value
- **Shake Gesture**: Moves to next step (a → b → c → solve) or resets after result
- The LED display shows **a**, **b**, **c** values or the result **x**

---

## 🧮 Mathematical Concepts Used
- Linear equations: ax + b = c
- Algebra: isolating the variable and solving for x
- Formula: x = (c − b) / a
- Division by zero: If a = 0, display shows "Err"

---

## 🖼️ Circuit Design (Screenshot)


![Circuit Design](./Screenshot%202026-02-14%20005320.png)
![Code Blocks](./Screenshot%202026-02-14%20005554.png)

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
2. Create four variables:
   - `a` (coefficient of x)
   - `b` (constant term)
   - `c` (right-hand side value)
   - `state` (0=setting a, 1=setting b, 2=setting c, 3=showing result)

These variables help the micro:bit remember the equation and which step the user is on.

---

### Step 5: Set starting values (On Start block)
1. Drag the **on start** block.
2. Set:
   - `a` to **1**
   - `b` to **0**
   - `c` to **0**
   - `state` to **0**
3. Add **show string** block with **"a"** and **show number** block with `a`.

This shows the starting value when setting the coefficient a.

---

### Step 6: Program the forever block (Display logic)
1. Drag the **forever** block.
2. Add **if / else if** blocks inside:
   - **If** `state` = 0: show string **"a"**, then show number `a`
   - **Else if** `state` = 1: show string **"b"**, then show number `b`
   - **Else if** `state` = 2: show string **"c"**, then show number `c`
   - **Else** (state = 3): if `a` = 0, show string **"Err"**; else set `x` to `(c − b) / a` and show number `x`

This displays the current variable or the solved result on the LED screen.

---

### Step 7: Program Button A (Decrease value)
1. Drag the **on button A pressed** block.
2. Inside it, add **if / else if** blocks:
   - **If** `state` = 0: change `a` by **-1**; if `a` < -9, set `a` to **10**
   - **Else if** `state` = 1: change `b` by **-1**; if `b` < -9, set `b` to **10**
   - **Else if** `state` = 2: change `c` by **-1**; if `c` < -9, set `c` to **10**
   - **Else** (state = 3): set `state` to **0**

This decreases the current variable or resets to start over.

---

### Step 8: Program Button B (Increase value)
1. Drag the **on button B pressed** block.
2. Inside it, add **if / else if** blocks:
   - **If** `state` = 0: change `a` by **+1**; if `a` > 10, set `a` to **-9**
   - **Else if** `state` = 1: change `b` by **+1**; if `b` > 10, set `b` to **-9**
   - **Else if** `state` = 2: change `c` by **+1**; if `c` > 10, set `c` to **-9**
   - **Else** (state = 3): set `state` to **0**

This increases the current variable or resets to start over.

---

### Step 9: Program Shake gesture (Next step / Reset)
1. Drag the **on shake** block.
2. Inside it:
   - **If** `state` < 3: change `state` by **+1**
   - **Else**: set `state` to **0**
3. This moves from setting a → b → c → solve, or resets after showing the result.

This advances to the next input step or restarts the solver.

---

### Step 10: Understand the calculation
The result shown on the display is calculated as:
- `x = (c − b) / a`

This means:
- `a` is the coefficient of x
- `b` is the constant on the left side
- `c` is the value on the right side
- Example: For 2x + 3 = 7, set a=2, b=3, c=7 → x = 2

---

### Step 11: Start the simulation
1. Click **Start Simulation**.
2. Press **Button A** or **Button B** to set values for a, b, and c.
3. Shake the micro:bit to move to the next variable or to solve.
4. Watch the result x appear on the display.

---

## 🖼️ Simulate: Variable Manipulator (Create Your Own)
Create your own variable manipulator in Tinkercad:
1. Use the same micro:bit setup (no extra components).
2. Change the formula to explore other equations (e.g., ax − b = c).
3. Add more variables or operations.

---
