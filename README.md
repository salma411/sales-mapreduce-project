﻿📦 Sales Aggregation using MapReduce

📝 Description
This project implements a simple MapReduce system using Python to calculate total sales per day of the week from a sales dataset (sales.csv).
It mimics how big data frameworks like Hadoop process data behind the scenes.

📂 Files

File	Description
mapper.py	Reads CSV data, extracts (DayOfWeek, Amount)
reducer.py	Aggregates and sums the Amount by DayOfWeek
sales.csv	Example dataset used for testing
🚀 How to Run the Project
bash
Copy
Edit
# On Linux/Mac
cat sales.csv | python mapper.py | sort | python reducer.py

# On Windows (Command Prompt)
type sales.csv | python3 mapper.py | sort | python3 reducer.py
✅ Output:
You will see total sales amounts grouped by weekdays.

📊 Example Output mathematica
Copy
Edit
Friday     24500.00
Monday     32200.00
Saturday   28700.00
Sunday     26600.00
Thursday   25100.00
Tuesday    29000.00
Wednesday  30200.00
🛠️ Technologies Used
Python 3

Pandas

VS Code

Linux Terminal / Git Bash

🎯 Features
Simple and clear MapReduce implementation

Real-world use case: sales data aggregation

Good practice for Hadoop/Big Data concepts

💡 Future Improvements (Optional)
Add filtering by region or product

Parallelize the map-reduce process

Connect to Hadoop HDFS

📚 License
This project is licensed under the MIT License.

🤝 Contributing
Feel free to fork the repository and submit pull requests!

🔥 Happy Coding! 🚀
📸 Bonus Tip:
If you want it to look even better on GitHub, you can add a screenshot showing the result in your terminal.
(Just take a screenshot and upload it — GitHub allows that!)
