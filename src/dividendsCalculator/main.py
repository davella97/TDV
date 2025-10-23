import sys
from dividendsCalculator.reader import loadCompanyData
from dividendsCalculator.calculator import calculateDividends

def main():
    if len(sys.argv) < 4:
        print("Usage: python -m dividend_calc.main <company> <start_date> <end_date>")
        sys.exit(1)

    company = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    data = loadCompanyData(company, start_date, end_date)
    calculateDividends(data, company, start_date, end_date)

if __name__ == "__main__":
    main()

