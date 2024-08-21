<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Finance Tracker Mini Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 10px 0;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
    </style>
</head>
<body>

    <h1>Personal Finance Tracker</h1>

    <h2>Problem Statement</h2>
    <p>Managing personal finances can be challenging without a clear record of income and expenses. This project aims to help users track their financial transactions, providing a simple way to monitor income, expenses, and savings over time.</p>

    <h2>Description</h2>
    <p>The Personal Finance Tracker is a Python-based application designed to help users practice and apply key Python concepts while managing their finances. The app offers the following features:</p>
    <ul>
        <li><strong>Track Income and Expenses</strong>: Users can enter details of their financial transactions.</li>
        <li><strong>View Past Transactions</strong>: The app displays a history of income and expense transactions.</li>
        <li><strong>Summary of Finances</strong>: It calculates and shows the total income, total expenditure, and net savings.</li>
        <li><strong>Time Series Plot</strong>: Users can generate a time series plot to visualize their income and expenditure over time.</li>
    </ul>

    <h2>Usage</h2>

    <h3>Step 1: Navigate to the Project Directory and Activate the Virtual Environment</h3>
    <pre><code>cd your_project_directory
venv\Scripts\activate</code></pre>

    <h3>Step 2: Install Dependencies</h3>
    <pre><code>python install_requirements.py</code></pre>
    <img src="https://github.com/23MD/Personal-Finance-Tracker/blob/6971a1811079c226f735321fa6e2082a2a6a3239/images/output1.PNG" alt="Output1">

    <h3>Step 3: Run the Application</h3>
    <pre><code>python main.py</code></pre>

    <h3>Step 4: Enter Transaction Details</h3>
    <p>To enter details of new transactions, select option '1'.</p>
    <img src="https://github.com/23MD/Personal-Finance-Tracker/blob/6971a1811079c226f735321fa6e2082a2a6a3239/images/output2.PNG" alt="Output2">

    <h3>Step 5: View Transactions and Summary</h3>
    <p>To view past transactions and summary, select option '2'. Then enter the start date and end date in the correct format.</p>
    <img src="https://github.com/23MD/Personal-Finance-Tracker/blob/6971a1811079c226f735321fa6e2082a2a6a3239/images/output3.PNG" alt="Output3">

    <p>If you want to generate a time series plot of income and expenditure over time, enter 'y'.</p>
    <img src="https://github.com/23MD/Personal-Finance-Tracker/blob/6971a1811079c226f735321fa6e2082a2a6a3239/images/Timeserieschart.png" alt="Timeseries Plot">

    <h2>Technology Stack</h2>
    <ul>
        <li><strong>Programming Language</strong>: Python</li>
        <li><strong>Development Environment</strong>: Visual Studio Code</li>
    </ul>

    <h2>Libraries Used</h2>
    <ul>
        <li><strong>Pandas</strong>: Data manipulation</li>
        <li><strong>NumPy</strong>: Numerical computations</li>
        <li><strong>Matplotlib</strong>: Data visualization</li>
        <li><strong>Logging</strong>: Logging for debugging</li>
    </ul>

    <h2>Contact Information</h2>
    <ul>
        <li><strong>LinkedIn</strong>: <a href="https://www.linkedin.com/in/mihirdamania/" target="_blank">Mihir Damania</a></li>
        <li><strong>Email</strong>: <a href="mailto:mihir.d1234@gmail.com">mihir.d1234@gmail.com</a></li>
    </ul>

</body>
</html>
