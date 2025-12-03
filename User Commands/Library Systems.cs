using Final_Project_CSCI_1250_201.Classes;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project_CSCI_1250_201.User_Commands //This one is a bit of a mess
{
    internal class Library_Systems
    {
        static List<LibraryItem> LibaryList = new List<LibraryItem>();
        static List<CheckoutItem> checkoutList = new List<CheckoutItem>();

        static string ListFile = "LibaryList.txt";
        static string checkoutFile = "myCheckouts.txt";
        public void Run()
        {
            LoadItem;

            bool running = true;
            while (running)
            {
                Console.WriteLine("\n----- Library Checkout System -----");
                Console.WriteLine("1. Add an item");
                Console.WriteLine("2. View current items");
                Console.WriteLine("3. Checkout an item");
                Console.WriteLine("4. Return an item");
                Console.WriteLine("5. View receipt");
                Console.WriteLine("6. Save my checkout list to a file");
                Console.WriteLine("7. Load my previous checkout list from a file");
                Console.WriteLine("8. Exit");
                Console.Write("Choose any of the above: ");

                string choice = Console.ReadLine();
                Console.WriteLine();

                switch (choice)
                {
                    case "1": AddLibraryItem(); break;
                    case "2": ViewAvailableItems(); break;
                    case "3": CheckoutItemMenu(); break;
                    case "4": ReturnItem(); break;
                    case "5": ViewReceipt(); break;
                    case "6": SaveCheckoutList(); break;
                    case "7": LoadCheckoutList(); break;
                    case "8": running = false; break;
                    default: Console.WriteLine("Invalid choice."); break;
                }
            }
        }