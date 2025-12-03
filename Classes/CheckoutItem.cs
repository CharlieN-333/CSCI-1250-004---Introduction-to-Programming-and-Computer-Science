using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project_CSCI_1250_201.Classes
{
    public class CheckoutItem
    {
        public LibraryItem Item { get; set; }
        public int LoanDays { get; set; }

        public CheckoutItem(LibraryItem item)
        {
            Item = item;

            if (item.Type.ToLower() == "book")  //Time of loan for
                LoanDays = 7;             //Books
            else
                LoanDays = 3;             //Anything else
        }
        public double CalculateLateFee(int daysLate)  //Late Fee calulation
        {
            if (daysLate <= 0) return 0;
            return daysLate * Item.DailyLateFee;
        }
    }
}
