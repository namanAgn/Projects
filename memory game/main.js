const gameBoard = document.getElementById('gameBoard');
const statusDisplay = document.getElementById('status');
let darkMode = false;

// Dark mode toggle
document.querySelector('.dark-mode').addEventListener('click', () => {
    darkMode = !darkMode; // Toggle dark mode
    document.querySelectorAll('.card').forEach((card) => {
        if (darkMode) {
            card.classList.add('dark');
            card.classList.add('flipped-dark'); // Add class for dark mode flipped state
        } else {
            card.classList.remove('dark');
            card.classList.remove('flipped-dark'); // Remove dark mode flipped state class
        }
    });
    document.querySelector('.heading').classList.toggle('dark', darkMode);
    document.querySelector('body').classList.toggle('dark', darkMode);
});

// Set up the cards (2 of each value for pairs)
const cardsArray = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'];

// Shuffle the cards
function shuffle(array) {
    return array.sort(() => 0.5 - Math.random());
}

let turns = 15;
let firstCard = null;
let secondCard = null;
let matchesFound = 0;

// Create and display the shuffled cards
function createCards() {
    const shuffledCards = shuffle(cardsArray);
    shuffledCards.forEach((cardValue) => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.value = cardValue;
        card.innerHTML = cardValue;
        card.addEventListener('click', handleCardClick);
        gameBoard.appendChild(card);
    });
}

// Handle card clicks
function handleCardClick(event) {
    const clickedCard = event.target;

    // Don't allow clicking the same card twice or if already matched
    if (clickedCard === firstCard || clickedCard.classList.contains('flipped')) {
        return; // Exit if clicked card is the same or already flipped
    }

    // Flip the card
    if (!darkMode) {
        clickedCard.classList.add('flipped');
    } else {
        clickedCard.classList.remove('dark');
        clickedCard.classList.add('dark-flipped');
    }

    // Check if it's the first or second card clicked
    if (!firstCard) {
        firstCard = clickedCard; // Select the first card
    } else {
        secondCard = clickedCard; // Select the second card

        // Check for a match
        if (firstCard.dataset.value === secondCard.dataset.value) {
            matchesFound++;
            resetCards(); // Reset selected cards if they match
        } else {
            // If they do not match, flip them back after a delay
            setTimeout(() => {
                if (!darkMode) {
                    firstCard.classList.remove('flipped');
                    secondCard.classList.remove('flipped');
                } else {
                    firstCard.classList.remove('dark-flipped');
                    secondCard.classList.remove('dark-flipped');
                }
                resetCards(); // Reset selected cards
            }, 1000); // Delay of 1 second
        }

        // Check if the game is won
        if (matchesFound === cardsArray.length / 2) {
            statusDisplay.classList.add('victory');
            statusDisplay.innerHTML = 'You win!';
        }
    }
}

// Reset the selected cards
function resetCards() {
    firstCard = null;
    secondCard = null;
}

// Initialize the game
createCards();
