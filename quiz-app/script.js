const questions = [
    {
        question: "What is the chemical formula for water?",
        option1: "H2O2",
        option2: "CO2",
        option3: "H2O",
        option4: "O2",
        correctOption: 3,
    },
    {
        question: "Which gas is most abundant in Earth's atmosphere?",
        option1: "Oxygen",
        option2: "Nitrogen",
        option3: "Carbon Dioxide",
        option4: "Helium",
        correctOption: 2,
    },
    {
        question: "How many planets are in our solar system?",
        option1: "9",
        option2: "7",
        option3: "8",
        option4: "10",
        correctOption: 3,
    },
    {
        question: "What is the main gas that plants absorb from the air?",
        option1: "Oxygen",
        option2: "Carbon Dioxide",
        option3: "Nitrogen",
        option4: "Hydrogen",
        correctOption: 2,
    },
    {
        question: "Which planet is known as the 'Blue Planet'?",
        option1: "Venus",
        option2: "Neptune",
        option3: "Earth",
        option4: "Uranus",
        correctOption: 3,
    },
    {
        question: "Who was the first Prime Minister of India?",
        option1: "Dr. Rajendra Prasad",
        option2: "Sardar Vallabhbhai Patel",
        option3: "Jawaharlal Nehru",
        option4: "Indira Gandhi",
        correctOption: 3,
    },
    {
        question: "In which year did India become a republic?",
        option1: "1947",
        option2: "1950",
        option3: "1962",
        option4: "1971",
        correctOption: 2,
    },
    {
        question: "Who was known as the 'Iron Man of India'?",
        option1: "Bhagat Singh",
        option2: "Sardar Vallabhbhai Patel",
        option3: "Subhas Chandra Bose",
        option4: "Lala Lajpat Rai",
        correctOption: 2,
    },
    {
        question: "Who discovered the sea route to India?",
        option1: "Christopher Columbus",
        option2: "Vasco da Gama",
        option3: "Marco Polo",
        option4: "Ferdinand Magellan",
        correctOption: 2,
    },
    {
        question: "Who was the first woman Prime Minister of India?",
        option1: "Sarojini Naidu",
        option2: "Indira Gandhi",
        option3: "Pratibha Patil",
        option4: "Sonia Gandhi",
        correctOption: 2,
    },
    {
        question: "What is the largest continent by area?",
        option1: "Africa",
        option2: "Asia",
        option3: "Europe",
        option4: "Antarctica",
        correctOption: 2,
    },
    {
        question: "Which river is the longest in the world?",
        option1: "Amazon",
        option2: "Ganges",
        option3: "Nile",
        option4: "Mississippi",
        correctOption: 3,
    },
    {
        question: "Which country has the highest population?",
        option1: "China",
        option2: "India",
        option3: "USA",
        option4: "Indonesia",
        correctOption: 2,
    },
    {
        question: "Which is the smallest country in the world?",
        option1: "Monaco",
        option2: "Vatican City",
        option3: "San Marino",
        option4: "Liechtenstein",
        correctOption: 2,
    },
    {
        question: "What is the capital of Australia?",
        option1: "Sydney",
        option2: "Melbourne",
        option3: "Canberra",
        option4: "Perth",
        correctOption: 3,
    },
    {
        question: "How many players are on a basketball team?",
        option1: "6",
        option2: "7",
        option3: "5",
        option4: "11",
        correctOption: 3,
    },
    {
        question: "Who is known as the 'God of Cricket'?",
        option1: "Virat Kohli",
        option2: "Sachin Tendulkar",
        option3: "MS Dhoni",
        option4: "Kapil Dev",
        correctOption: 2,
    },
    {
        question: "Which sport is associated with Wimbledon?",
        option1: "Tennis",
        option2: "Cricket",
        option3: "Football",
        option4: "Hockey",
        correctOption: 1,
    },
    {
        question: "How many rings are there on the Olympic flag?",
        option1: "4",
        option2: "5",
        option3: "6",
        option4: "7",
        correctOption: 2,
    },
    {
        question: "Which country hosted the 2020 Summer Olympics?",
        option1: "China",
        option2: "Brazil",
        option3: "Japan",
        option4: "USA",
        correctOption: 3,
    },
    {
        question: "Who is the President of the United States as of 2024?",
        option1: "Donald Trump",
        option2: "Joe Biden",
        option3: "Barack Obama",
        option4: "Kamala Harris",
        correctOption: 2,
    },
    {
        question: "Which day is celebrated as World Environment Day?",
        option1: "June 5",
        option2: "April 22",
        option3: "March 8",
        option4: "October 2",
        correctOption: 1,
    },
    {
        question: "What is the currency of Japan?",
        option1: "Yuan",
        option2: "Won",
        option3: "Yen",
        option4: "Peso",
        correctOption: 3,
    },
    {
        question: "What does UNESCO stand for?",
        option1: "United Nations Educational, Scientific, and Cultural Organization",
        option2: "United Nations Energy and Security Council Organization",
        option3: "United Nations Environmental and Scientific Council Organization",
        option4: "Universal Education and Science Committee Organization",
        correctOption: 1,
    },
    {
        question: "Which animal is known as the 'King of the Jungle'?",
        option1: "Tiger",
        option2: "Lion",
        option3: "Elephant",
        option4: "Cheetah",
        correctOption: 2,
    },
    {
        question: "Who was the first man to walk on the moon?",
        option1: "Buzz Aldrin",
        option2: "Neil Armstrong",
        option3: "Yuri Gagarin",
        option4: "Michael Collins",
        correctOption: 2,
    },
    {
        question: "What is the largest planet in our solar system?",
        option1: "Saturn",
        option2: "Earth",
        option3: "Jupiter",
        option4: "Neptune",
        correctOption: 3,
    },
    {
        question: "Which spacecraft was the first to land on the Moon?",
        option1: "Sputnik",
        option2: "Apollo 11",
        option3: "Challenger",
        option4: "Voyager",
        correctOption: 2,
    },
    {
        question: "What is the primary language used for coding websites?",
        option1: "Python",
        option2: "Java",
        option3: "HTML",
        option4: "C++",
        correctOption: 3,
    },
    {
        question: "What is the full form of Wi-Fi?",
        option1: "Wireless Fidelity",
        option2: "Wide Frequency",
        option3: "Web Frequency Interface",
        option4: "Wireless Framework",
        correctOption: 1,
    },
    {
        question: "Which festival is known as the 'Festival of Colors'?",
        option1: "Diwali",
        option2: "Holi",
        option3: "Dussehra",
        option4: "Eid",
        correctOption: 2,
    },
    {
        question: "Which Indian classical dance form is from Tamil Nadu?",
        option1: "Kathak",
        option2: "Bharatanatyam",
        option3: "Kuchipudi",
        option4: "Odissi",
        correctOption: 2,
    },
    {
        question: "What is the national animal of India?",
        option1: "Lion",
        option2: "Tiger",
        option3: "Elephant",
        option4: "Peacock",
        correctOption: 2,
    },
    {
        question: "Who wrote the Indian national anthem?",
        option1: "Bankim Chandra Chatterjee",
        option2: "Rabindranath Tagore",
        option3: "Sarojini Naidu",
        option4: "Subhas Chandra Bose",
        correctOption: 2,
    },
    {
        question: "What is the capital city of France?",
        option1: "Berlin",
        option2: "Madrid",
        option3: "Paris",
        option4: "Rome",
        correctOption: 3,
    },
    {
        question: "Which country is famous for the Great Wall?",
        option1: "India",
        option2: "China",
        option3: "Japan",
        option4: "Vietnam",
        correctOption: 2,
    },
    {
        question: "What is the currency of the United Kingdom?",
        option1: "Dollar",
        option2: "Euro",
        option3: "Pound Sterling",
        option4: "Yen",
        correctOption: 3,
    },
    {
        question: "Which instrument is used to measure temperature?",
        option1: "Barometer",
        option2: "Thermometer",
        option3: "Anemometer",
        option4: "Hygrometer",
        correctOption: 2,
    },
    {
        question: "Who is the author of the Harry Potter series?",
        option1: "J.R.R. Tolkien",
        option2: "J.K. Rowling",
        option3: "C.S. Lewis",
        option4: "George R.R. Martin",
        correctOption: 2,
    },
    {
        question: "What is the hardest natural substance on Earth?",
        option1: "Gold",
        option2: "Iron",
        option3: "Diamond",
        option4: "Quartz",
        correctOption: 3,
    },
    {
        question: "Which is the largest ocean on Earth?",
        option1: "Atlantic Ocean",
        option2: "Indian Ocean",
        option3: "Arctic Ocean",
        option4: "Pacific Ocean",
        correctOption: 4,
    },
    {
        question: "What is the boiling point of water in Celsius?",
        option1: "50°C",
        option2: "100°C",
        option3: "0°C",
        option4: "25°C",
        correctOption: 2,
    },
    {
        question: "Which planet is known as the 'Red Planet'?",
        option1: "Mars",
        option2: "Venus",
        option3: "Jupiter",
        option4: "Saturn",
        correctOption: 1,
    },
];

let score = 0;
let questionNumber = 1;

let questionHtml = '';
questions.forEach((question, index) => {
    questionHtml += 
    `
    <div class="question">
        <h2>Question ${index + 1}:</h2>
        <h3>${question.question}</h3>
        <div class="flex">
            <div class="options">
                <button class="option" data-answer='${question.correctOption === 1 ? 'correct' : 'incorrect'}'>${question.option1}</button>
                <button class="option" data-answer='${question.correctOption === 2 ? 'correct' : 'incorrect'}'>${question.option2}</button>
                <button class="option" data-answer='${question.correctOption === 3 ? 'correct' : 'incorrect'}'>${question.option3}</button>
                <button class="option" data-answer='${question.correctOption === 4 ? 'correct' : 'incorrect'}'>${question.option4}</button>
            </div>
            <p class="answer-display"></p>
        </div>
    </div>
    `;
});

document.querySelector('.questions').innerHTML = questionHtml;

const options = document.querySelectorAll('.option');
options.forEach(option => {
    option.addEventListener('click', function() {
        const answerDisplay = this.parentElement.nextElementSibling;

        if (this.dataset.answer === 'correct') {
            answerDisplay.textContent = '✅';
            answerDisplay.classList.add('correct');
            answerDisplay.classList.remove('incorrect');
        } else {
            answerDisplay.textContent = '❌';
            answerDisplay.classList.add('incorrect');
            answerDisplay.classList.remove('correct');
        }
        answerDisplay.style.display = 'block'; // Show answer display

        setTimeout(() => {answerDisplay.style.display = 'none';}, 1000)
    });

});
