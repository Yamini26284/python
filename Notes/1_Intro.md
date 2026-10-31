### 🧠 Core Computer Concepts


**1. High-Level Language**

• What it is: Programming languages written in a way that humans can easily read and write using real English words (like if, while, print).   

• Why we need it: Humans cannot easily think in binary code. High-level languages let us write instructions comfortably.  

• Examples: Python, Java, JavaScript, C++.

**2. The Three Types of Code**

Computers only understand 1s and 0s. The journey from human thought to computer action goes through three stages:

• Source Code: This is the raw text you type directly into your text editor or IDE. It uses human-readable English words (like if, while, and print) and is meant for human programmers to read and write.  

• Bytecode: This is a half-translated, intermediate code. An internal compiler creates it from your source code. It is far too complex and unreadable for humans to understand, but it is not quite ready for raw computer hardware either. Instead, it is read and run by special virtual software (like the Java Virtual Machine or Python Virtual Machine).  

• Machine Code: This is the ultimate final destination. It consists entirely of raw 1s and 0s (binary code). It is the only language that the computer's CPU (the physical hardware) can actually understand and use to control electricity.


### 🏎️ The Translators: Compiler vs. Interpreter

To turn human-readable source code into machine code, the computer uses a translator.

**📜 The Compiler (The "Book Translator")**  
• How it works: Translates your entire program all at once before you run it. It spits out a finished executable file (like a .exe file).  
• Strong Points:  
	• Blazing Speed: The code runs as fast as the hardware allows because the translation is already finished.  
	• Efficiency: Doesn't waste computer memory or battery translating things while running.  
	• Security: Harder for others to steal your source code from a finished executable file.  
• Weak Point: If you have even one tiny syntax mistake, the compiler refuses to build the program at all.  

**🎧 The Interpreter (The "Live Translator")**

• How it works: Translates and runs your code line by line, in real time as the program is running.  

• Strong Points:  
	1.  Fast Development: You can change a line of code and instantly click run without waiting for a slow compilation process.  
	2.  Cross-Platform: The exact same file can run on Windows, Mac, or Linux as long as they have the interpreter installed.  
	3. Easy Debugging: The program runs smoothly until it hits the exact line with the error, making it easy to see where things went wrong. 

• Weak Point: It runs slower because the computer has to translate the code while running it.  

🐍 The Python Hybrid Model  

• Why Python is called "Interpreted" even though it compiles: Python actually uses both. When you click run, a built-in compiler instantly turns your source code into bytecode. 

However, it is still classified as an interpreted language because that bytecode cannot run on its own; a software interpreter (the Python Virtual Machine) must read and execute that bytecode line-by-line at runtime.  

🧩 Programming Philosophy: Multi-Paradigm  

A paradigm is a style or mindset for organizing code. A multi-paradigm language is like a Swiss Army knife—it lets you mix and match different styles depending on the problem you are solving.  

**The Three Main Coding Styles:**  
1. Procedural (Imperative): Writing code as a simple, step-by-step recipe ("First do this, then change that variable, then repeat").  
2. Object-Oriented (OOP): Grouping data and actions together into structural units called "Objects" (e.g., creating a User object that holds a name, email, and a login() function).  
3. Functional: Treating code like pure mathematical equations. You pass data through functions to get new data without changing the original variables.  

### 🤖 AI Evaluations & AI Security (AI Sec)


🥇 Why Python Comes First

If you want to work in AI Evals (testing AI models for safety and bias) or AI Sec (defending AI systems), Python is the absolute king.  

• The Ecosystem: The standard industry toolkits for AI security—such as Microsoft PyRIT (Python Risk Identification Tool), Garak (vulnerability scanner), and Guardrails AI—are all built natively in Python.

• The Workflow: AI security requires fast text manipulation, processing massive amounts of data, and talking to machine learning APIs. Python's interpreted nature makes this rapid scripting possible.

⚙️ Where Compiled Languages (C++ / Rust) Fit In  

AI Security is split into two layers:  
1. Behavioral Security (Python): Stopping prompt injection, jailbreaks, and logical manipulation of the AI.  
2. Infrastructure Security (C++ / Rust): Because AI models require massive processing power, the low-level engines and GPU frameworks are written in compiled languages. Hackers targeting the hardware or trying to cause memory overflows at the server level must be defended against using C++ and Rust knowledge.  
-------------------
### variable rules

Here are the crisp, essential rules for naming and using variables in Python, rewritten without any tables:

🏛️ **The Structural Rules (Naming Restrictions)**

Python is strict about what characters can go into a variable name. If you break these rules, your code will crash before it runs.  

• Allowed Starting Characters: A variable name must strictly start with either a letter (a-z, A-Z) or an underscore (_). 
For example, user_name or _system_id are perfectly fine.

• Forbidden Starting Characters: A name can never start with a number. For example, writing 1st_place or 4sale will cause an error.  

• Allowed Body Characters: The rest of the variable name can only contain letters, numbers, and underscores (A-z, 0-9, _).  

• Forbidden Body Characters: You cannot use spaces, hyphens, or symbols anywhere in the name. For example, user-name, my age, and price$ are completely illegal. 

• Reserved Keywords: You cannot use Python Keywords (built-in commands like if, else, while, import, def, or return) as variable names because Python already uses them to run its own core logic.  

⚙️ **The Execution Rules (Behavior)**

• Case Sensitivity: Python treats lowercase and uppercase letters as completely different variables. 

For example, age, Age, and AGE are treated as three separate variables that can hold entirely different values.  

• Dynamic Typing: You do not need to declare what type of data a variable holds (like specifying it's an integer or text ahead of time). Python figures it out automatically at runtime. 

You can write x = 5, and then immediately write x = "Hello" on the next line; the variable will change its type on the fly without issue.  

• No Blank Spaces: Variables must be written as continuous text blocks. To mimic spaces, you must use underscores (like total_price). 

🎨 **The Stylistic Rules (Best Practices / PEP 8)**

While your code will still run if you ignore these, following them makes your code clean and professional:  

• The Snake Case Standard: Always write your variable names in all lowercase letters and separate the words with underscores. For example, use user_login_count instead of UserLoginCount or userlogincount.

• Be Descriptive: A variable name should clearly explain what data it holds. Use remaining_attempts = 3 instead of a cryptic shortcut like ra = 3.  

• Constants: If a variable is a "constant" (a value that should never change while your program is running), write the entire variable name in ALL CAPS. For example, use PI = 3.14159 or MAX_LOGIN_ATTEMPTS = 5.

### Naming Conventions

**Camel Case**

• How it works: The very first word starts with a lowercase letter. Every following word starts with an uppercase letter. There are no spaces or underscores between words.  

• Example: userLoginCount, totalPrice, remainingAttempts.  

• Python Usage: Rarely used in Python. You will mostly see this style when working in JavaScript or Java.

📐 **Pascal Case (PascalCase)**

• How it works: Every single word starts with an uppercase letter, including the very first word. There are no spaces or underscores.  

• Example: UserLoginCount, TotalPrice, CalculateSquare.  

• Python Usage: Highly Important. Python strictly uses Pascal Case for naming Classes (which are the blueprints used in Object-Oriented Programming).

🐍 **Snake Case (snake_case)**  

• How it works: Every word is written in all lowercase letters, and words are separated by an underscore (_).  

• Example: user_login_count, total_price, calculate_square.  

• Python Usage: The Gold Standard. Python uses Snake Case for almost everything: regular variable names, function names, and file names (main_script.py).

**Upper Snake Case (UPPER_SNAKE_CASE)**

The most important missing style you must know for Python is Upper Snake Case (also known as Screaming Snake Case).  

• How it works: Every word is written in ALL CAPS, and words are separated by an underscore (_).  

• Example: MAX_LOGIN_ATTEMPTS = 5, PI = 3.14159, DATABASE_URL = "localhost".  

• Python Usage: Crucial for Constants. Python does not have a built-in safety feature to lock a variable and stop it from changing. Instead, Python programmers use Upper Snake Case as a visual warning sign that says: "This value is a constant. Do not change it anywhere else in the code!"  

💡 **Bonus: Kebab Case (kebab-case)**

• How it works: Every word is written in lowercase, separated by a hyphen (-).  
• Example: user-login-count.  
• Python Usage: Completely Illegal. 

