// Loops
let foods = ["pizza", "burger", "sushi"]

let foodFact = {
    name: "Pizza",
    calories: 20
}

// basic for loop
const forLoop = (foods) => {
    for (let i = 0; i < foods.length; i++){
        console.log(foods[i]);
    };
};

forLoop(foods)

// let of loop (for arrays)
const letOfLoop = (foods) => {
    for (let food of foods) {
        console.log(food);
    };
};

letOfLoop(foods)

// let in loop (for objects)
const letInLoop = (foodFact) => {
    for (let key in foodFact) {
        console.log(key);
        console.log(foodFact[key]);
    };
};

letInLoop(foodFact)

//While Loop
const whileLoop = () => {
    let i = 0
    while (i < 5) {
        i += 1
        console.log(i)
    };
};

whileLoop()