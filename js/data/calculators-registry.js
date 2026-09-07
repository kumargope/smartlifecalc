/* SmartLifeCalc - 40 Calculators Registry Data */
const CALCULATORS_REGISTRY = [
  // Money (10)
  {
    id: "tip-calculator",
    title: "Tip Calculator",
    category: "Money",
    url: "/calculators/tip-calculator.html",
    description: "Calculate tip amounts, total bills, and split per person instantly.",
    keywords: ["tip", "restaurant", "gratuity", "split bill", "dining", "waiter"]
  },
  {
    id: "discount-calculator",
    title: "Discount Calculator",
    category: "Money",
    url: "/calculators/discount-calculator.html",
    description: "Find your final sale price and savings amount after percentage discounts.",
    keywords: ["discount", "sale", "savings", "percentage off", "shopping"]
  },
  {
    id: "sales-tax-calculator",
    title: "Sales Tax Calculator",
    category: "Money",
    url: "/calculators/sales-tax-calculator.html",
    description: "Calculate total cost with state or local US sales tax included.",
    keywords: ["sales tax", "tax rate", "total price", "vat", "us tax"]
  },
  {
    id: "split-bill-calculator",
    title: "Split Bill Calculator",
    category: "Money",
    url: "/calculators/split-bill-calculator.html",
    description: "Split group restaurant bills, party expenses, and tips evenly.",
    keywords: ["split bill", "group pay", "per person", "tip split", "dinner split"]
  },
  {
    id: "percentage-calculator",
    title: "Percentage Calculator",
    category: "Money",
    url: "/calculators/percentage-calculator.html",
    description: "Calculate percentage increases, decreases, and fractions of numbers.",
    keywords: ["percentage", "percent", "math", "fraction", "ratio", "change"]
  },
  {
    id: "simple-interest-calculator",
    title: "Simple Interest Calculator",
    category: "Money",
    url: "/calculators/simple-interest-calculator.html",
    description: "Compute simple interest growth on principal investments or loans.",
    keywords: ["simple interest", "principal", "interest rate", "yield", "investment"]
  },
  {
    id: "compound-interest-calculator",
    title: "Compound Interest Calculator",
    category: "Money",
    url: "/calculators/compound-interest-calculator.html",
    description: "Calculate how compound interest grows your investments over time.",
    keywords: ["compound interest", "growth", "savings", "wealth", "401k", "investment"]
  },
  {
    id: "loan-payment-calculator",
    title: "Loan Payment Calculator",
    category: "Money",
    url: "/calculators/loan-payment-calculator.html",
    description: "Calculate monthly payments and total interest for personal loans.",
    keywords: ["loan", "monthly payment", "interest rate", "personal loan", "finance"]
  },
  {
    id: "hourly-to-salary-calculator",
    title: "Hourly to Salary Calculator",
    category: "Money",
    url: "/calculators/hourly-to-salary-calculator.html",
    description: "Convert hourly pay rate into annual, monthly, and weekly salary totals.",
    keywords: ["hourly rate", "salary", "annual wage", "paycheck", "income", "wage"]
  },
  {
    id: "salary-to-hourly-calculator",
    title: "Salary to Hourly Calculator",
    category: "Money",
    url: "/calculators/salary-to-hourly-calculator.html",
    description: "Convert annual salary into equivalent hourly wage rate.",
    keywords: ["salary to hourly", "wage equivalent", "annual pay", "working hours"]
  },

  // Home (5)
  {
    id: "mortgage-calculator",
    title: "Mortgage Calculator",
    category: "Home",
    url: "/calculators/mortgage-calculator.html",
    description: "Calculate estimated monthly mortgage principal, interest, and loan totals.",
    keywords: ["mortgage", "home loan", "housing", "down payment", "monthly payment"]
  },
  {
    id: "home-affordability-calculator",
    title: "Home Affordability Calculator",
    category: "Home",
    url: "/calculators/home-affordability-calculator.html",
    description: "Estimate maximum home price you can afford based on income and debt.",
    keywords: ["home affordability", "how much home", "buying a house", "budget"]
  },
  {
    id: "rent-vs-buy-calculator",
    title: "Rent vs Buy Calculator",
    category: "Home",
    url: "/calculators/rent-vs-buy-calculator.html",
    description: "Compare total long-term costs of renting vs purchasing a home.",
    keywords: ["rent vs buy", "renting", "homeownership", "housing comparison"]
  },
  {
    id: "electricity-cost-calculator",
    title: "Electricity Cost Calculator",
    category: "Home",
    url: "/calculators/electricity-cost-calculator.html",
    description: "Calculate energy consumption cost for household appliances and devices.",
    keywords: ["electricity", "power bill", "kwh", "energy cost", "appliance"]
  },
  {
    id: "area-calculator",
    title: "Area Calculator",
    category: "Home",
    url: "/calculators/area-calculator.html",
    description: "Calculate square footage and area for rectangular, circular, and triangular rooms.",
    keywords: ["area", "square feet", "sq ft", "room size", "dimensions", "flooring"]
  },

  // Car & Travel (5)
  {
    id: "gas-cost-calculator",
    title: "Gas Cost Calculator",
    category: "Car & Travel",
    url: "/calculators/gas-cost-calculator.html",
    description: "Calculate fuel expenses for any driving trip distance.",
    keywords: ["gas cost", "fuel cost", "trip cost", "gasoline", "driving expense"]
  },
  {
    id: "mpg-calculator",
    title: "MPG Calculator",
    category: "Car & Travel",
    url: "/calculators/mpg-calculator.html",
    description: "Determine your vehicle's fuel efficiency in Miles Per Gallon.",
    keywords: ["mpg", "miles per gallon", "fuel economy", "gas efficiency", "mileage"]
  },
  {
    id: "road-trip-cost-calculator",
    title: "Road Trip Cost Calculator",
    category: "Car & Travel",
    url: "/calculators/road-trip-cost-calculator.html",
    description: "Calculate total gas, tolls, and split costs per person for road trips.",
    keywords: ["road trip", "travel cost", "split gas", "tolls", "car travel"]
  },
  {
    id: "fuel-cost-calculator",
    title: "Fuel Cost Calculator",
    category: "Car & Travel",
    url: "/calculators/fuel-cost-calculator.html",
    description: "Calculate full tank refill cost based on current gas price.",
    keywords: ["fuel refill", "gas tank", "fill up cost", "gas station", "petrol"]
  },
  {
    id: "car-loan-calculator",
    title: "Car Loan Calculator",
    category: "Car & Travel",
    url: "/calculators/car-loan-calculator.html",
    description: "Calculate monthly auto loan payments, interest fees, and total vehicle cost.",
    keywords: ["car loan", "auto loan", "vehicle financing", "car payment", "down payment"]
  },

  // Date & Time (5)
  {
    id: "age-calculator",
    title: "Age Calculator",
    category: "Date & Time",
    url: "/calculators/age-calculator.html",
    description: "Calculate your exact age in years, months, days, and total days.",
    keywords: ["age", "date of birth", "how old am i", "birthday", "exact age"]
  },
  {
    id: "date-difference-calculator",
    title: "Date Difference Calculator",
    category: "Date & Time",
    url: "/calculators/date-difference-calculator.html",
    description: "Calculate exact number of days, weeks, and months between two dates.",
    keywords: ["date difference", "days between", "time span", "calendar duration"]
  },
  {
    id: "days-until-calculator",
    title: "Days Until Date Calculator",
    category: "Date & Time",
    url: "/calculators/days-until-calculator.html",
    description: "Count down days remaining until holidays, birthdays, or target events.",
    keywords: ["days until", "countdown", "target date", "event timer", "days left"]
  },
  {
    id: "workdays-calculator",
    title: "Workdays Calculator",
    category: "Date & Time",
    url: "/calculators/workdays-calculator.html",
    description: "Count total business workdays between dates excluding weekends.",
    keywords: ["workdays", "business days", "working days", "days excluding weekends"]
  },
  {
    id: "time-difference-calculator",
    title: "Time Difference Calculator",
    category: "Date & Time",
    url: "/calculators/time-difference-calculator.html",
    description: "Calculate hours and minutes elapsed between two clock times.",
    keywords: ["time difference", "hours worked", "time duration", "clock difference"]
  },

  // Shopping (5)
  {
    id: "sale-price-calculator",
    title: "Sale Price Calculator",
    category: "Shopping",
    url: "/calculators/sale-price-calculator.html",
    description: "Calculate final price after double discounts and promotional sales.",
    keywords: ["sale price", "store sale", "double discount", "shopping deal"]
  },
  {
    id: "percentage-off-calculator",
    title: "Percentage Off Calculator",
    category: "Shopping",
    url: "/calculators/percentage-off-calculator.html",
    description: "Quickly figure out how much you save with percentage off deals.",
    keywords: ["percent off", "savings", "shopping deal", "bargain", "discount"]
  },
  {
    id: "unit-price-calculator",
    title: "Unit Price Calculator",
    category: "Shopping",
    url: "/calculators/unit-price-calculator.html",
    description: "Determine cost per ounce, pound, gram, or count to compare store deals.",
    keywords: ["unit price", "grocery cost", "cost per oz", "bulk buy comparison"]
  },
  {
    id: "buy-one-get-one-calculator",
    title: "Buy One Get One Calculator",
    category: "Shopping",
    url: "/calculators/buy-one-get-one-calculator.html",
    description: "Calculate true savings and per-item cost on BOGO promotional deals.",
    keywords: ["bogo", "buy one get one", "free item", "promo deal", "bogo math"]
  },
  {
    id: "price-comparison-calculator",
    title: "Price Comparison Calculator",
    category: "Shopping",
    url: "/calculators/price-comparison-calculator.html",
    description: "Compare two package options to find which item offers the best value.",
    keywords: ["price comparison", "best deal", "grocery savings", "value comparison"]
  },

  // Converters (10)
  {
    id: "miles-to-km",
    title: "Miles to Kilometers Converter",
    category: "Converters",
    url: "/calculators/miles-to-km.html",
    description: "Convert distance from US Miles to Metric Kilometers instantly.",
    keywords: ["miles to km", "mi to km", "distance converter", "metric conversion"]
  },
  {
    id: "km-to-miles",
    title: "Kilometers to Miles Converter",
    category: "Converters",
    url: "/calculators/km-to-miles.html",
    description: "Convert distance from Kilometers to US Miles instantly.",
    keywords: ["km to miles", "km to mi", "distance converter", "us unit conversion"]
  },
  {
    id: "pounds-to-kg",
    title: "Pounds to Kilograms Converter",
    category: "Converters",
    url: "/calculators/pounds-to-kg.html",
    description: "Convert bodyweight and mass from Pounds (lbs) to Kilograms (kg).",
    keywords: ["pounds to kg", "lbs to kg", "weight converter", "mass conversion"]
  },
  {
    id: "kg-to-pounds",
    title: "Kilograms to Pounds Converter",
    category: "Converters",
    url: "/calculators/kg-to-pounds.html",
    description: "Convert mass from Kilograms (kg) to Pounds (lbs) instantly.",
    keywords: ["kg to pounds", "kg to lbs", "weight converter", "weight conversion"]
  },
  {
    id: "feet-to-inches",
    title: "Feet to Inches Converter",
    category: "Converters",
    url: "/calculators/feet-to-inches.html",
    description: "Convert height or length measurements from Feet to Inches.",
    keywords: ["feet to inches", "ft to in", "length converter", "height conversion"]
  },
  {
    id: "feet-inches-to-cm",
    title: "Feet/Inches to Centimeters",
    category: "Converters",
    url: "/calculators/feet-inches-to-cm.html",
    description: "Convert height in Feet and Inches to Metric Centimeters (cm).",
    keywords: ["feet inches to cm", "ft in to cm", "height to cm", "centimeters"]
  },
  {
    id: "fahrenheit-to-celsius",
    title: "Fahrenheit to Celsius Converter",
    category: "Converters",
    url: "/calculators/fahrenheit-to-celsius.html",
    description: "Convert weather and cooking temperature from °F to °C.",
    keywords: ["fahrenheit to celsius", "f to c", "temperature converter", "degrees f"]
  },
  {
    id: "celsius-to-fahrenheit",
    title: "Celsius to Fahrenheit Converter",
    category: "Converters",
    url: "/calculators/celsius-to-fahrenheit.html",
    description: "Convert temperature from Metric Celsius (°C) to US Fahrenheit (°F).",
    keywords: ["celsius to fahrenheit", "c to f", "temperature converter", "degrees c"]
  },
  {
    id: "gallons-to-liters",
    title: "Gallons to Liters Converter",
    category: "Converters",
    url: "/calculators/gallons-to-liters.html",
    description: "Convert US liquid volume from Gallons to Metric Liters.",
    keywords: ["gallons to liters", "gal to l", "volume converter", "liquid conversion"]
  },
  {
    id: "ounces-to-grams",
    title: "Ounces to Grams Converter",
    category: "Converters",
    url: "/calculators/ounces-to-grams.html",
    description: "Convert weight from US Ounces (oz) to Metric Grams (g).",
    keywords: ["ounces to grams", "oz to g", "cooking measurement", "weight converter"]
  }
];

if (typeof window !== 'undefined') {
  window.CALCULATORS_REGISTRY = CALCULATORS_REGISTRY;
}
