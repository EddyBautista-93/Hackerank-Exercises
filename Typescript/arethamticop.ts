// The first line contains the first integer, . The second line contains the second integer, .

// Constraints



// Output Format

// Print the three lines as explained above.

// Sample Input 0

// 3
// 2
// Sample Output 0

// 5
// 1
// 6

const areOp = (x: number, y:any) => {
    let plus = (x + y);
    let minus = (x - y);
    let mul = (x * y);
    console.log(`${plus} \n ${minus} \n ${mul}`);
}

areOp(3,2);