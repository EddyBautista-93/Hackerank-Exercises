using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;


class triplets {

  // Complete the compareTriplets function below.
    static List<int> compareTriplets(List<int> a, List<int> b) {
        //vreates a score list to compare the two
        List<int> scores = new List<int>() { 0, 0 };
        //loops throygh both arrays
        for(int i = 0; i < a.Count; i++ )
        {
            if(a[i] > b[i]) scores[0]++;
            else if(a[i] < b[i]) scores[1]++;
            
        }
        return scores;
    }

    static void Main(string[] args)
    {
        List<int> alice = new List<int>() { 5, 6, 7 };
        List<int> bob = new List<int>() { 3, 6, 10 };
        Console.WriteLine(compareTriplets(alice,bob));
    }

}