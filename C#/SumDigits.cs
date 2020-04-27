public static int SumDigits(int number)
        {
            int a = System.Math.Abs(number);
            int b = a / 10;
            int c = a % 10;

            return b + c;

        }