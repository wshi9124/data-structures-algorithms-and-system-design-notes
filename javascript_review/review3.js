let favoriteFood = [
    {
        name: "Pizza",
        calories: 10,
        price: 10
    },
    {
        name: "Chicken",
        calories: 20,
        price: 15
    },
    {
        name: "Steak",
        calories: 20,
        price: 20
    },
    {
        name: "Fries",
        calories: 40,
        price: 25
    }
]

// Difference between map and forEach is that map returns a value
const foodName = favoriteFood.map(food => food.name);
const newPrice = favoriteFood.map(food => {
    food.price += 2
    return food.price
});

const addToPrice = favoriteFood.forEach( food => {
    food.price += 10
})

// .find finds only the match and returns the value
const findCaloriesFind = favoriteFood.find(food => food.calories === 20);
//.filter shows all the results 
const findCaloriesFilter = favoriteFood.filter(food => food.calories === 20);




console.log(foodName);
console.log(newPrice);
console.log(findCaloriesFind);
console.log(findCaloriesFilter);