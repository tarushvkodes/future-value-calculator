document.getElementById('calculate').addEventListener('click', function() {
    const initialInvestment = parseFloat(document.getElementById('initial-investment').value);
    const annualContribution = parseFloat(document.getElementById('annual-contribution').value);
    const years = parseFloat(document.getElementById('years').value);
    const interestRate = parseFloat(document.getElementById('interest-rate').value) / 100;

    if (isNaN(initialInvestment) || isNaN(annualContribution) || isNaN(years) || isNaN(interestRate)) {
        document.getElementById('result').innerText = 'Please enter valid numbers in all fields.';
        return;
    }

    let futureValue = initialInvestment;
    for (let i = 0; i < years; i++) {
        futureValue = (futureValue + annualContribution) * (1 + interestRate);
    }

    document.getElementById('result').innerText = 'Future Value: $' + futureValue.toFixed(2);
});
