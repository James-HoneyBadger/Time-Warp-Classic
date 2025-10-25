#!/usr/bin/env node
/**
 * JavaScript Example Program - Interactive Quiz Game
 * This program demonstrates JavaScript syntax, objects, and interactive programming
 */

// Simple quiz game data
const quizQuestions = [
    {
        question: "What is 2 + 2?",
        options: ["3", "4", "5", "6"],
        correct: 1,
        explanation: "2 + 2 equals 4"
    },
    {
        question: "Which programming language is this written in?",
        options: ["Python", "JavaScript", "Java", "C++"],
        correct: 1,
        explanation: "This is JavaScript code!"
    },
    {
        question: "What does 'DOM' stand for?",
        options: ["Document Object Model", "Data Object Manager", "Dynamic Object Method", "Digital Output Module"],
        correct: 0,
        explanation: "DOM stands for Document Object Model"
    }
];

class QuizGame {
    constructor() {
        this.score = 0;
        this.currentQuestion = 0;
        this.questions = quizQuestions;
    }

    displayQuestion() {
        const q = this.questions[this.currentQuestion];
        console.log(`\n📝 Question ${this.currentQuestion + 1}: ${q.question}`);

        q.options.forEach((option, index) => {
            console.log(`${index + 1}. ${option}`);
        });
    }

    checkAnswer(userAnswer) {
        const q = this.questions[this.currentQuestion];
        const isCorrect = (userAnswer - 1) === q.correct;

        if (isCorrect) {
            console.log("✅ Correct!");
            this.score++;
        } else {
            console.log("❌ Wrong!");
            console.log(`The correct answer was: ${q.options[q.correct]}`);
        }

        console.log(q.explanation);
        return isCorrect;
    }

    play() {
        console.log("🎮 Welcome to the JavaScript Quiz Game!");
        console.log("=====================================");

        // Use readline for input (if available)
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        const askQuestion = () => {
            if (this.currentQuestion >= this.questions.length) {
                this.showResults();
                rl.close();
                return;
            }

            this.displayQuestion();

            rl.question("Enter your answer (1-4): ", (answer) => {
                const userAnswer = parseInt(answer);

                if (isNaN(userAnswer) || userAnswer < 1 || userAnswer > 4) {
                    console.log("Please enter a number between 1 and 4.");
                    askQuestion();
                    return;
                }

                this.checkAnswer(userAnswer);
                this.currentQuestion++;
                askQuestion();
            });
        };

        askQuestion();
    }

    showResults() {
        console.log("\n🎉 Quiz Complete!");
        console.log(`Your score: ${this.score}/${this.questions.length}`);

        const percentage = (this.score / this.questions.length) * 100;
        if (percentage >= 80) {
            console.log("🏆 Excellent! You're a JavaScript expert!");
        } else if (percentage >= 60) {
            console.log("👍 Good job! Keep learning!");
        } else {
            console.log("📚 Keep practicing JavaScript!");
        }
    }
}

// Function to demonstrate JavaScript features
function demonstrateJS() {
    console.log("🚀 JavaScript Feature Demonstration");
    console.log("-".repeat(40));

    // Variables and data types
    const name = "TimeWarp";
    let version = 1.0;
    const features = ["Multi-language", "Turtle Graphics", "Interactive"];

    console.log(`IDE Name: ${name}`);
    console.log(`Version: ${version}`);
    console.log(`Features: ${features.join(", ")}`);

    // Array methods
    const doubled = features.map(feature => feature.length * 2);
    console.log(`Feature name lengths doubled: ${doubled}`);

    // Object destructuring
    const user = { username: "student", level: "beginner" };
    const { username, level } = user;
    console.log(`${username} is a ${level} programmer`);

    // Template literals and arrow functions
    const greet = (person) => `Hello, ${person}! Welcome to JavaScript programming!`;
    console.log(greet("Programmer"));
}

// Run the program
console.log("🟨 JavaScript Example Program");
console.log("This demonstrates JavaScript syntax and interactive programming\n");

demonstrateJS();

const game = new QuizGame();
game.play();