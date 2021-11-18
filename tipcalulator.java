public class TipCalculator {
    private double bill;
    private double tip;
    private int people;
    private double tax;

    public TipCalculator(double newBill, double newTip, int newPeople) {
        setBill(newBill);
        setTip(newTip);
        setPeople(newPeople);
        setTax(tax);
    }

    public void setBill (double newBill){
        if (newBill > 0) {
            bill = newBill;
        }
    }

    public void setTip(double newTip) {
        if (newTip > 0) {
            tip = newTip;
        }
    }

    public void setPeople(int newPeople){
        if (newPeople > 0) {
            people = newPeople;
        }
    }

    public void setTax(double newTax) {
        if (newTax > 0) {
            tax = newTax;
        }
    }

    public double getBill() {
        return bill;
    }

    public double getTip() {
        return tip;
    }

    public int getPeople() {
        return people;
    }

    public double getTax() {
        return ((bill-(bill/1.0813)));
    }

    public double taxAmount() {
        return (bill * tax);
    }

    public double tipAmount() {
        return (bill * tip);
    }

    public double tipAmountEach() {
        return ((bill * tip)/people);
    }


    public double totalAmount() {
        return (bill);
    }

    public double totalAmountEach() {
        return ((bill + tipAmount() )/people);
    }
}