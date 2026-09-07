/* SmartLifeCalc - Core Calculator Math & Logic Engine */

const CalcEngine = {
  // Formatters
  formatCurrency(val) {
    if (isNaN(val) || !isFinite(val)) return "$0.00";
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(val);
  },

  formatNumber(val, decimals = 2) {
    if (isNaN(val) || !isFinite(val)) return "0";
    return new Intl.NumberFormat('en-US', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    }).format(val);
  },

  formatPercent(val, decimals = 2) {
    if (isNaN(val) || !isFinite(val)) return "0%";
    return this.formatNumber(val, decimals) + "%";
  },

  // Money Calculators
  calculateTip(bill, tipPercent, people) {
    if (bill <= 0 || tipPercent < 0 || people <= 0) {
      throw new Error("Please enter valid positive numbers.");
    }
    const tipAmount = bill * (tipPercent / 100);
    const totalBill = bill + tipAmount;
    const perPerson = totalBill / people;
    const tipPerPerson = tipAmount / people;

    return {
      tipAmount,
      totalBill,
      perPerson,
      tipPerPerson
    };
  },

  calculateDiscount(originalPrice, discountPercent) {
    if (originalPrice <= 0 || discountPercent < 0) {
      throw new Error("Please enter valid positive numbers.");
    }
    const discountAmount = originalPrice * (discountPercent / 100);
    const finalPrice = Math.max(0, originalPrice - discountAmount);

    return {
      discountAmount,
      finalPrice,
      savedAmount: discountAmount
    };
  },

  calculateSalesTax(price, taxRate) {
    if (price <= 0 || taxRate < 0) {
      throw new Error("Please enter a valid price and tax rate.");
    }
    const taxAmount = price * (taxRate / 100);
    const totalPrice = price + taxAmount;

    return {
      taxAmount,
      totalPrice
    };
  },

  calculateSplitBill(bill, people, tipPercent = 0) {
    if (bill <= 0 || people <= 0) {
      throw new Error("Please enter a valid bill amount and number of people.");
    }
    const tipAmount = bill * (tipPercent / 100);
    const total = bill + tipAmount;
    const perPersonTotal = total / people;
    const perPersonBill = bill / people;
    const perPersonTip = tipAmount / people;

    return {
      total,
      tipAmount,
      perPersonTotal,
      perPersonBill,
      perPersonTip
    };
  },

  calculatePercentage(val1, val2, mode = "of") {
    if (isNaN(val1) || isNaN(val2)) {
      throw new Error("Please enter valid numbers.");
    }
    if (mode === "of") {
      // What is val1% of val2?
      return (val1 / 100) * val2;
    } else if (mode === "is") {
      // val1 is what % of val2?
      if (val2 === 0) throw new Error("Cannot divide by zero.");
      return (val1 / val2) * 100;
    } else if (mode === "change") {
      // % increase/decrease from val1 to val2
      if (val1 === 0) throw new Error("Initial value cannot be zero.");
      return ((val2 - val1) / val1) * 100;
    }
    return 0;
  },

  calculateSimpleInterest(principal, rate, years) {
    if (principal <= 0 || rate < 0 || years <= 0) {
      throw new Error("Please enter positive values for principal, rate, and years.");
    }
    const interest = principal * (rate / 100) * years;
    const totalAmount = principal + interest;

    return {
      interest,
      totalAmount
    };
  },

  calculateCompoundInterest(principal, rate, frequency, years, monthlyContrib = 0) {
    if (principal < 0 || rate < 0 || years <= 0) {
      throw new Error("Please enter valid positive values.");
    }
    const r = rate / 100;
    const n = frequency; // compounds per year (12 = monthly, 1 = annually, 4 = quarterly)
    const t = years;

    let balance = principal * Math.pow(1 + r / n, n * t);

    // Future value of monthly contributions
    let contribBalance = 0;
    if (monthlyContrib > 0) {
      const pmts = 12 * t;
      const ratePerPmt = r / 12;
      if (ratePerPmt > 0) {
        contribBalance = monthlyContrib * ((Math.pow(1 + ratePerPmt, pmts) - 1) / ratePerPmt);
      } else {
        contribBalance = monthlyContrib * pmts;
      }
    }

    const totalValue = balance + contribBalance;
    const totalDeposits = principal + (monthlyContrib * 12 * years);
    const totalInterest = Math.max(0, totalValue - totalDeposits);

    return {
      totalValue,
      totalDeposits,
      totalInterest
    };
  },

  calculateLoanPayment(principal, annualRate, years) {
    if (principal <= 0 || annualRate <= 0 || years <= 0) {
      throw new Error("Please enter valid positive numbers for loan calculation.");
    }
    const monthlyRate = (annualRate / 100) / 12;
    const numberOfPayments = years * 12;

    const monthlyPayment = (principal * monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) /
                           (Math.pow(1 + monthlyRate, numberOfPayments) - 1);

    const totalPayment = monthlyPayment * numberOfPayments;
    const totalInterest = totalPayment - principal;

    return {
      monthlyPayment,
      totalPayment,
      totalInterest
    };
  },

  calculateHourlyToSalary(hourlyRate, hoursPerWeek = 40, weeksPerYear = 52) {
    if (hourlyRate <= 0 || hoursPerWeek <= 0 || weeksPerYear <= 0) {
      throw new Error("Please enter valid positive work parameters.");
    }
    const weekly = hourlyRate * hoursPerWeek;
    const biweekly = weekly * 2;
    const monthly = (weekly * weeksPerYear) / 12;
    const annual = weekly * weeksPerYear;

    return {
      hourly: hourlyRate,
      weekly,
      biweekly,
      monthly,
      annual
    };
  },

  calculateSalaryToHourly(annualSalary, hoursPerWeek = 40, weeksPerYear = 52) {
    if (annualSalary <= 0 || hoursPerWeek <= 0 || weeksPerYear <= 0) {
      throw new Error("Please enter a valid positive salary.");
    }
    const totalHours = hoursPerWeek * weeksPerYear;
    const hourly = annualSalary / totalHours;
    const daily = hourly * (hoursPerWeek / 5);
    const weekly = annualSalary / weeksPerYear;
    const monthly = annualSalary / 12;

    return {
      hourly,
      daily,
      weekly,
      monthly,
      annual: annualSalary
    };
  },

  // Home Calculators
  calculateMortgage(homePrice, downPayment, rate, termYears) {
    if (homePrice <= 0 || rate <= 0 || termYears <= 0) {
      throw new Error("Please enter valid loan details.");
    }
    const loanAmount = Math.max(0, homePrice - downPayment);
    const monthlyRate = (rate / 100) / 12;
    const totalPaymentsCount = termYears * 12;

    const monthlyPayment = (loanAmount * monthlyRate * Math.pow(1 + monthlyRate, totalPaymentsCount)) /
                           (Math.pow(1 + monthlyRate, totalPaymentsCount) - 1);

    const totalPayment = monthlyPayment * totalPaymentsCount;
    const totalInterest = totalPayment - loanAmount;

    return {
      loanAmount,
      monthlyPayment,
      totalInterest,
      totalPayment
    };
  },

  calculateHomeAffordability(income, monthlyDebt, downPayment, rate = 6.5) {
    if (income <= 0) throw new Error("Please enter a valid annual income.");
    // 28% front-end DTI rule
    const monthlyIncome = income / 12;
    const maxMonthlyMortgage = Math.max(0, (monthlyIncome * 0.28) - monthlyDebt);

    const monthlyRate = (rate / 100) / 12;
    const n = 360; // 30 yr mortgage

    let maxLoan = 0;
    if (monthlyRate > 0 && maxMonthlyMortgage > 0) {
      maxLoan = (maxMonthlyMortgage * (Math.pow(1 + monthlyRate, n) - 1)) /
                (monthlyRate * Math.pow(1 + monthlyRate, n));
    }

    const maxHomePrice = maxLoan + downPayment;

    return {
      maxHomePrice,
      maxLoan,
      maxMonthlyMortgage
    };
  },

  calculateRentVsBuy(monthlyRent, homePrice, downPayment, years = 7) {
    if (monthlyRent <= 0 || homePrice <= 0) throw new Error("Please enter valid rental and home price details.");

    // Simple comparison model over 'years'
    const totalRentCost = monthlyRent * 12 * years * 1.03; // assuming 3% annual rent inflation
    const loanAmount = Math.max(0, homePrice - downPayment);

    // 30 yr mortgage at 6.5% interest + maintenance + taxes (~2% total)
    const mortgageResult = this.calculateMortgage(homePrice, downPayment, 6.5, 30);
    const totalMortgagePayments = mortgageResult.monthlyPayment * 12 * years;
    const propertyTaxAndMaint = (homePrice * 0.02) * years;
    const totalOwnershipCost = downPayment + totalMortgagePayments + propertyTaxAndMaint;

    const recommendation = totalOwnershipCost < totalRentCost ? "Buying may build more equity!" : "Renting may keep your monthly costs lower!";

    return {
      totalRentCost,
      totalOwnershipCost,
      recommendation
    };
  },

  calculateElectricityCost(watts, hoursPerDay, rateKwh = 0.16) {
    if (watts <= 0 || hoursPerDay <= 0 || rateKwh <= 0) {
      throw new Error("Please enter positive device power and usage hours.");
    }
    const kwhPerDay = (watts * hoursPerDay) / 1000;
    const kwhPerMonth = kwhPerDay * 30;
    const kwhPerYear = kwhPerDay * 365;

    return {
      dailyCost: kwhPerDay * rateKwh,
      monthlyCost: kwhPerMonth * rateKwh,
      yearlyCost: kwhPerYear * rateKwh,
      kwhPerMonth
    };
  },

  calculateArea(shape, dim1, dim2 = 0) {
    if (dim1 <= 0) throw new Error("Please enter positive dimensions.");

    let sqFt = 0;
    if (shape === "rectangle") {
      if (dim2 <= 0) throw new Error("Please enter width and length.");
      sqFt = dim1 * dim2;
    } else if (shape === "circle") {
      // dim1 is radius
      sqFt = Math.PI * dim1 * dim1;
    } else if (shape === "triangle") {
      // dim1 is base, dim2 is height
      if (dim2 <= 0) throw new Error("Please enter base and height.");
      sqFt = 0.5 * dim1 * dim2;
    }

    const sqMeters = sqFt * 0.092903;
    const acres = sqFt / 43560;

    return {
      sqFt,
      sqMeters,
      acres
    };
  },

  // Car & Travel Calculators
  calculateGasCost(distance, mpg, gasPrice) {
    if (distance <= 0 || mpg <= 0 || gasPrice <= 0) {
      throw new Error("Please enter valid positive numbers for trip distance, MPG, and gas price.");
    }
    const gallonsNeeded = distance / mpg;
    const estimatedCost = gallonsNeeded * gasPrice;

    return {
      gallonsNeeded,
      estimatedCost
    };
  },

  calculateMPG(miles, gallons) {
    if (miles <= 0 || gallons <= 0) {
      throw new Error("Miles driven and gallons used must be greater than zero.");
    }
    const mpg = miles / gallons;
    const litersPer100km = 235.215 / mpg;

    return {
      mpg,
      litersPer100km
    };
  },

  calculateRoadTripCost(distance, mpg, gasPrice, tolls = 0, passengers = 1) {
    if (distance <= 0 || mpg <= 0 || gasPrice <= 0 || passengers < 1) {
      throw new Error("Please enter valid trip parameters.");
    }
    const gallons = distance / mpg;
    const fuelCost = gallons * gasPrice;
    const totalTripCost = fuelCost + tolls;
    const costPerPerson = totalTripCost / passengers;

    return {
      fuelCost,
      totalTripCost,
      costPerPerson
    };
  },

  calculateFuelCost(tankCapacity, currentLevelPercent, gasPrice) {
    if (tankCapacity <= 0 || gasPrice <= 0 || currentLevelPercent < 0 || currentLevelPercent > 100) {
      throw new Error("Please enter a valid tank size and current level %.");
    }
    const percentNeeded = (100 - currentLevelPercent) / 100;
    const gallonsToFill = tankCapacity * percentNeeded;
    const totalRefillCost = gallonsToFill * gasPrice;

    return {
      gallonsToFill,
      totalRefillCost
    };
  },

  calculateCarLoan(price, downPayment, rate, termMonths) {
    if (price <= 0 || rate <= 0 || termMonths <= 0) {
      throw new Error("Please enter valid vehicle loan parameters.");
    }
    const loanAmount = Math.max(0, price - downPayment);
    const monthlyRate = (rate / 100) / 12;

    const monthlyPayment = (loanAmount * monthlyRate * Math.pow(1 + monthlyRate, termMonths)) /
                           (Math.pow(1 + monthlyRate, termMonths) - 1);

    const totalPayment = monthlyPayment * termMonths;
    const totalInterest = totalPayment - loanAmount;

    return {
      loanAmount,
      monthlyPayment,
      totalInterest,
      totalPayment
    };
  },

  // Date & Time Calculators
  calculateAge(dobString, targetDateString = null) {
    const dob = new Date(dobString);
    if (isNaN(dob.getTime())) throw new Error("Please enter a valid date of birth.");

    const target = targetDateString ? new Date(targetDateString) : new Date();
    if (isNaN(target.getTime()) || target < dob) throw new Error("Target date must be after birth date.");

    let years = target.getFullYear() - dob.getFullYear();
    let months = target.getMonth() - dob.getMonth();
    let days = target.getDate() - dob.getDate();

    if (days < 0) {
      months--;
      const lastMonthDate = new Date(target.getFullYear(), target.getMonth(), 0);
      days += lastMonthDate.getDate();
    }
    if (months < 0) {
      years--;
      months += 12;
    }

    const diffTime = Math.abs(target - dob);
    const totalDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    const totalHours = totalDays * 24;

    return {
      years,
      months,
      days,
      totalDays,
      totalHours
    };
  },

  calculateDateDifference(startDateStr, endDateStr) {
    const start = new Date(startDateStr);
    const end = new Date(endDateStr);
    if (isNaN(start.getTime()) || isNaN(end.getTime())) throw new Error("Please enter valid start and end dates.");

    const diffMs = end - start;
    const totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    const totalWeeks = (totalDays / 7).toFixed(1);

    return {
      totalDays,
      totalWeeks,
      isPast: diffMs < 0
    };
  },

  calculateDaysUntil(targetDateStr) {
    const target = new Date(targetDateStr);
    const today = new Date();
    today.setHours(0,0,0,0);

    if (isNaN(target.getTime())) throw new Error("Please select a valid future date.");

    const diffMs = target - today;
    const daysLeft = Math.ceil(diffMs / (1000 * 60 * 60 * 24));

    return {
      daysLeft,
      targetDayOfWeek: target.toLocaleDateString('en-US', { weekday: 'long' })
    };
  },

  calculateWorkdays(startDateStr, endDateStr, excludeWeekends = true) {
    const start = new Date(startDateStr);
    const end = new Date(endDateStr);
    if (isNaN(start.getTime()) || isNaN(end.getTime()) || start > end) {
      throw new Error("Please enter a valid date range.");
    }

    let cur = new Date(start);
    let workdays = 0;
    let totalDays = 0;

    while (cur <= end) {
      totalDays++;
      const day = cur.getDay();
      const isWeekend = (day === 0 || day === 6);
      if (!excludeWeekends || !isWeekend) {
        workdays++;
      }
      cur.setDate(cur.getDate() + 1);
    }

    return {
      workdays,
      weekendDays: totalDays - workdays,
      totalDays
    };
  },

  calculateTimeDifference(startTimeStr, endTimeStr) {
    if (!startTimeStr || !endTimeStr) throw new Error("Please select start and end times.");

    const [h1, m1] = startTimeStr.split(':').map(Number);
    const [h2, m2] = endTimeStr.split(':').map(Number);

    let minutes1 = h1 * 60 + m1;
    let minutes2 = h2 * 60 + m2;

    if (minutes2 < minutes1) {
      // crossed midnight
      minutes2 += 24 * 60;
    }

    const diffMinutes = minutes2 - minutes1;
    const hours = Math.floor(diffMinutes / 60);
    const mins = diffMinutes % 60;

    return {
      hours,
      mins,
      totalMinutes: diffMinutes
    };
  },

  // Shopping Calculators
  calculateSalePrice(originalPrice, discountPercent, extraDiscount = 0) {
    if (originalPrice <= 0 || discountPercent < 0) throw new Error("Please enter valid prices and discounts.");

    const firstDiscount = originalPrice * (discountPercent / 100);
    const priceAfterFirst = originalPrice - firstDiscount;

    const secondDiscount = priceAfterFirst * (extraDiscount / 100);
    const finalPrice = Math.max(0, priceAfterFirst - secondDiscount);
    const totalSavings = originalPrice - finalPrice;

    return {
      finalPrice,
      totalSavings,
      effectiveDiscountPercent: ((totalSavings / originalPrice) * 100).toFixed(1)
    };
  },

  calculatePercentageOff(originalPrice, percentOff) {
    return this.calculateDiscount(originalPrice, percentOff);
  },

  calculateUnitPrice(price, quantity, unitName = "item") {
    if (price <= 0 || quantity <= 0) throw new Error("Price and quantity must be greater than zero.");

    const unitPrice = price / quantity;
    return {
      unitPrice,
      unitName
    };
  },

  calculateBOGO(itemPrice, buyQty = 1, getQty = 1, getDiscountPercent = 100) {
    if (itemPrice <= 0 || buyQty <= 0 || getQty <= 0) throw new Error("Please enter valid BOGO offer details.");

    const fullPriceItemsCost = itemPrice * buyQty;
    const discountedItemsCost = (itemPrice * (1 - getDiscountPercent / 100)) * getQty;

    const totalCost = fullPriceItemsCost + discountedItemsCost;
    const totalItems = buyQty + getQty;
    const regularTotal = itemPrice * totalItems;
    const savings = regularTotal - totalCost;
    const effectiveDiscount = (savings / regularTotal) * 100;
    const costPerItem = totalCost / totalItems;

    return {
      totalCost,
      savings,
      costPerItem,
      effectiveDiscount
    };
  },

  calculatePriceComparison(priceA, qtyA, priceB, qtyB) {
    if (priceA <= 0 || qtyA <= 0 || priceB <= 0 || qtyB <= 0) {
      throw new Error("Please enter valid prices and quantities for Option A and Option B.");
    }
    const unitPriceA = priceA / qtyA;
    const unitPriceB = priceB / qtyB;

    let winner = "Option A";
    let savingsPercent = 0;
    if (unitPriceB < unitPriceA) {
      winner = "Option B";
      savingsPercent = ((unitPriceA - unitPriceB) / unitPriceA) * 100;
    } else {
      savingsPercent = ((unitPriceB - unitPriceA) / unitPriceB) * 100;
    }

    return {
      unitPriceA,
      unitPriceB,
      winner,
      savingsPercent
    };
  },

  // Converters
  convertMilesToKm(miles) {
    if (isNaN(miles)) throw new Error("Please enter a valid number.");
    return miles * 1.60934;
  },

  convertKmToMiles(km) {
    if (isNaN(km)) throw new Error("Please enter a valid number.");
    return km / 1.60934;
  },

  convertPoundsToKg(lbs) {
    if (isNaN(lbs)) throw new Error("Please enter a valid number.");
    return lbs * 0.453592;
  },

  convertKgToPounds(kg) {
    if (isNaN(kg)) throw new Error("Please enter a valid number.");
    return kg / 0.453592;
  },

  convertFeetToInches(feet) {
    if (isNaN(feet)) throw new Error("Please enter a valid number.");
    return feet * 12;
  },

  convertFeetInchesToCm(feet, inches = 0) {
    if (isNaN(feet) || isNaN(inches)) throw new Error("Please enter valid numbers.");
    const totalInches = (feet * 12) + inches;
    return totalInches * 2.54;
  },

  convertFahrenheitToCelsius(f) {
    if (isNaN(f)) throw new Error("Please enter a valid number.");
    return (f - 32) * (5 / 9);
  },

  convertCelsiusToFahrenheit(c) {
    if (isNaN(c)) throw new Error("Please enter a valid number.");
    return (c * 9 / 5) + 32;
  },

  convertGallonsToLiters(gallons) {
    if (isNaN(gallons)) throw new Error("Please enter a valid number.");
    return gallons * 3.78541;
  },

  convertOuncesToGrams(oz) {
    if (isNaN(oz)) throw new Error("Please enter a valid number.");
    return oz * 28.3495;
  }
};

if (typeof window !== 'undefined') {
  window.CalcEngine = CalcEngine;
}
