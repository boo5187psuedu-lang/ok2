"""
TASI - Tadawul All Share Index (أسهم تاسي)
Saudi Stock Market stocks information fetcher.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime


TASI_STOCKS = [
    {"symbol": "2222", "name_ar": "أرامكو السعودية", "name_en": "Saudi Aramco", "sector": "الطاقة"},
    {"symbol": "1180", "name_ar": "الأهلي السعودي", "name_en": "Al Rajhi Bank", "sector": "البنوك"},
    {"symbol": "1120", "name_ar": "مصرف الراجحي", "name_en": "Al Rajhi Bank", "sector": "البنوك"},
    {"symbol": "2010", "name_ar": "سابك", "name_en": "SABIC", "sector": "البتروكيماويات"},
    {"symbol": "2350", "name_ar": "المتقدمة", "name_en": "Advanced Petro. Industries", "sector": "البتروكيماويات"},
    {"symbol": "7010", "name_ar": "الاتصالات السعودية", "name_en": "Saudi Telecom (STC)", "sector": "الاتصالات"},
    {"symbol": "7020", "name_ar": "موبايلي", "name_en": "Mobily", "sector": "الاتصالات"},
    {"symbol": "4200", "name_ar": "المملكة القابضة", "name_en": "Kingdom Holding", "sector": "التنويع"},
    {"symbol": "8010", "name_ar": "شركة الكهرباء", "name_en": "Saudi Electricity", "sector": "المرافق"},
    {"symbol": "4030", "name_ar": "بدجت السعودية", "name_en": "Budget Saudi", "sector": "النقل"},
]


def fetch_stock_data(symbol: str) -> dict:
    """
    Fetch stock data for a given symbol from Tadawul API.
    Falls back to placeholder data if the request fails.
    """
    url = f"https://www.saudiexchange.sa/wps/portal/saudiexchange/trading/market-summary/company-security?symbol={symbol}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read().decode("utf-8")
            return {"symbol": symbol, "raw": data[:200]}
    except Exception:
        return {"symbol": symbol, "price": "N/A", "change": "N/A", "change_pct": "N/A"}


def display_stocks(stocks: list) -> None:
    """Display TASI stocks in a formatted table."""
    print("=" * 75)
    print(f"{'أسهم تاسي - Tadawul All Share Index (TASI)':^75}")
    print(f"{'تاريخ: ' + datetime.now().strftime('%Y-%m-%d %H:%M'):^75}")
    print("=" * 75)
    print(f"{'الرمز':<8} {'الاسم العربي':<25} {'الاسم الإنجليزي':<30} {'القطاع':<15}")
    print("-" * 75)
    for stock in stocks:
        print(
            f"{stock['symbol']:<8} {stock['name_ar']:<25} {stock['name_en']:<30} {stock['sector']:<15}"
        )
    print("=" * 75)
    print(f"إجمالي الأسهم المعروضة: {len(stocks)}")
    print()


def main() -> None:
    """Main entry point."""
    print()
    display_stocks(TASI_STOCKS)
    print("للحصول على بيانات حية، يرجى زيارة: https://www.saudiexchange.sa")
    print("For live data, please visit: https://www.saudiexchange.sa")
    print()


if __name__ == "__main__":
    main()
