# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that connects with the Binance Futures Testnet API and allows users to place, validate, and track trading orders.

## Features

- Place MARKET and LIMIT orders
- Binance Futures Testnet API integration
- Command-line interface (CLI)
- Order input validation
- Order status tracking
- Error handling
- Trading activity logging

## Project Structure

```
trading_bot/
│
├── cli.py
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

**Important:** Never upload your `.env` file or API credentials to GitHub.

## Usage

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Example Output

```
===== ORDER REQUEST =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

===== ORDER RESPONSE =====
Order ID      : 22291037302
Status        : NEW
Executed Qty  : 0.0000

===== ORDER STATUS CHECK =====
Current Status : NEW

✅ Order process completed!
```

## Logging

The bot maintains logs for:

- Order requests
- Successful orders
- Failed orders
- Order status checks

Logs are stored in:

```
logs/trading.log
```

## Tech Stack

- Python
- Binance Futures Testnet API
- python-binance
- argparse
- logging
- python-dotenv

## Future Improvements

- Cancel order functionality
- Unit testing
- Database storage for trade history
- Web dashboard for monitoring orders
