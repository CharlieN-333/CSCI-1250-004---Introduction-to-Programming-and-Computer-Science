using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project_CSCI_1250_201.Classes
{
    public class LibraryItem
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Type { get; set; }
        public double DailyLateFee { get; set; }
        public LibraryItem(int id, string title, string type, double lateFee)  //Thanks visual studio code for
                                                                               //yelling at me for my formatting
        {
            Id = id;
            Title = title;
            Type = type;
            DailyLateFee = lateFee;
        }
        public override string ToString()
        {
            return $"{Id} - {Title} ({Type}) - Late Fee: ${DailyLateFee:F2}/day";
        }
    }
}
