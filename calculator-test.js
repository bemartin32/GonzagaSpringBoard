it("should calculate the monthly rate correctly", function () {
  const values = {
    amount: 10000,
    years: 5,
    rate: 5,
  };
  const result = calculateMonthlyPayment(values);
  expect(result).toEqual("188.71");
});

it("should return a result with 2 decimal places", function () {
  const values = {
    amount: 10000,
    years: 5,
    rate: 5,
  };
  const result = calculateMonthlyPayment(values);
  expect(result).toBeCloseTo("188.71", 2);
});
