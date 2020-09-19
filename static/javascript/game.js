let terms = {"Investor": "Person purchasing the stock",
"Shareholder": "Person selling the stock",
"Previous Close": "The last price of the stock from when the market closed on the previous trading day",
"Open": "The starting price of trading for this trading day",
"Change": "How many points the stock rose/fell during the trading day",
"Percent Change": "How much the stock rose/fell during the trading day compared to its value given as a percentage",
"Bid": "The highest price an investor is willing to pay for a share",
"Ask": "The lowest price at which a shareholder is willing to sell their shares",
"Day's Range": "The difference between the highest and lowest price traded during the trading day",
"52 Week Range": "The difference between the highest and lowest price traded during the past 52 weeks",
"Volume": "The amount of an asset or security that changes hands over a specific period of time",
"Average Volume": "The totol volume in the specified period divided by the number of bars",
"Market Capitalization": "The total value of all a company's shares of stock",
"Beta": "A measure of the stock's volatility",
"P/E ratio": "The ratio of the Company's stock price to its earnings per share. This ratio is used to value the company and find out if its overvalued or undervalued",
"Earnings Per Share": "The portion of a company's profit that that is allocated to every share of the stock",
"Earnings Date": "The date of the next release of the company's financial report",
"Forward Dividend and Yield": "An estimation of the year's dividend expressed as a percentage of the current stock price",
"Ex-Dividend Date": "Set 1 day before the record date and determines who earns the dividend the seller or the buyer",
"Target Estimate": "Reflects what analysts think the stock will be worth after a certain period of time"
}

let gameArea = document.getElementById('game-area');
let playGame;
//creating main menu

function createMainMenu(){
    let gameChildren = Array.from(gameArea.children)
    gameChildren.forEach(child =>{
        gameArea.removeChild(child);
    })
    playGame = document.createElement('button');
    playGame.id = 'play-game'
    playGame.textContent = 'Play Game';
    playGame.addEventListener('click', e => {
        playInterior();
    })
    gameArea.appendChild(playGame);
}
createMainMenu();


function playInterior(){
    gameArea.removeChild(playGame);

    let dictLength = Object.keys(terms).length
    let definition = Object.values(terms)[Math.floor(Math.random()*dictLength)];
    console.log(definition);

    //holds the form
    let containerDiv = document.createElement('div');
    containerDiv.id = 'container-div';

    let prompt = document.createElement('h3');
    prompt.id = 'prompt';
    prompt.innerHTML = "What term does the following defnition correspond to?"


    let displayDefinition = document.createElement('p');
    displayDefinition.id = 'definition';
    displayDefinition.textContent = definition;

    let submitBundle = document.createElement('div');
    submitBundle.id = 'submit-bundle';

    let answer = document.createElement('input');
    answer.id = 'answer';
    answer.placeholder = 'Type your answer here';
    answer.addEventListener('keypress', e =>{
        if(e.key == 'Enter'){
            answerCheckInterior(answer, definition);
        }
    })

    let submit = document.createElement('button');
    submit.id = 'quiz-submit';
    submit.textContent  = 'Submit';
    submit.addEventListener('click', e =>{
        answerCheckInterior(answer);
    })

    submitBundle.appendChild(answer);
    submitBundle.appendChild(submit);

    containerDiv.appendChild(prompt);
    containerDiv.appendChild(displayDefinition);
    containerDiv.appendChild(submitBundle);


    gameArea.appendChild(containerDiv)
}


function answerCheckInterior(answer){
    console.log(answer.value);
}