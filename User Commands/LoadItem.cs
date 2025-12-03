using Final_Project_CSCI_1250_201.Classes;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final_Project_CSCI_1250_201.User_Commands
{
    internal class LoadItem         //Thanks file for not embedding for some reason so i cant figure out if this will work
    {
        public void LoadItems()
        {
            if (!File.Exists(LibaryItems.txt))
            {
                File.WriteAllText(LibaryItems.txt, "");
                return;
            }

            foreach (var line in File.ReadAllLines(LibaryItems.txt))
            {
                if (string.IsNullOrWhiteSpace(line)) continue; //Makes sure that there is actually something in the line

                var p = line.Split(',');
                LibaryList.Add(new LibraryItem(
                    int.Parse(p[0]), p[1], p[2], double.Parse(p[3])  
                ));
            }
        }